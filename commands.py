import telebot
from telebot import types
from config import load_configuration
from TODO import *

# Путь к файлу конфигурации
config_path = './config.ini'
try:
    config_data = load_configuration(config_path)
    admins = set(config_data['admins'])  # Преобразуем список в множество для ускорения проверки
    print("Конфигурация успешно загружена.")
    print("Токен бота:", config_data['token'])
    print("Администраторы:", config_data['admins'])
    bot = telebot.TeleBot(config_data['token'])
except Exception as e:
    print("Ошибка:", str(e))
    exit(1)


# ДЕКОРАТОР ADMIN ONLY COMMAND
def admin_required(func):
    def wrapped(message):
        user_username = message.from_user.username
        if not(user_username in admins or '@' + user_username in admins):
            bot.send_message(message.chat.id, "Извините, но эта команда только для администраторов.")
            return
        return func(message)

    return wrapped


@bot.message_handler(commands=['start'])
def handle_start(message):
    # Получаем username пользователя в виде строки, если он есть
    user_username = message.from_user.username
    welcome_text = "Добро пожаловать в нашего бота!"

    if user_username:
        welcome_text += f" Ваш телеграм тег: @{user_username}."
        if user_username in admins or '@' + user_username in admins:
            welcome_text += " Вы являетесь администратором этого бота."
        else:
            welcome_text += " Наслаждайтесь использованием!"
    else:
        welcome_text += " Внимание: у вас не установлен телеграм тег, некоторые функции могут быть недоступны."

    bot.send_message(message.chat.id, welcome_text)


@bot.message_handler(commands=['listme'])
def list_events_for_user(message):
    # Получаем тег пользователя
    user_tag = message.from_user.username
    if not user_tag:
        bot.send_message(message.chat.id, "Ваш профиль не имеет тега (username), который необходим для использования этой функции.")
        return

    # Вызываем функцию, которая возвращает список событий и дедлайны из базы данных
    events = get_event_list_for_user(user_tag)  # Предположим, что функция принимает тег пользователя

    if not events:
        bot.send_message(message.chat.id, "Вы пока не подписаны ни на одно событие.")
        return

    response_message = "Вы подписаны на следующие события и дедлайны:\n"
    for event_name, deadlines in events.items():
        response_message += f"\n📅 {event_name}:\n"
        for deadline_name, deadline_time in deadlines.items():
            response_message += f"   - {deadline_name}: {deadline_time}\n"

    bot.send_message(message.chat.id, response_message)


# Словарь для управления состояниями пользователей и их данными
user_data = {}

# Получение текущего состояния пользователя
def get_user_step(user_tag):
    if user_tag in user_data:
        return user_data[user_tag]['step']
    else:
        return "AWAITING_COMMAND"



# Команда для начала создания или редактирования события
@bot.message_handler(commands=['newevent'])
@admin_required
def new_event(message):
    user_tag = message.from_user.username
    if user_tag not in user_data:
        user_data[user_tag] = {'step': None, 'file_id': None, 'event_name': None}
    markup = types.ForceReply(selective=False)
    bot.send_message(message.chat.id, "Отправьте файл Excel с дедлайнами. После отправки файла введите название мероприятия.", reply_markup=markup)
    user_data[user_tag]['step'] = "AWAITING_FILE"


# Обработчик для получения файла
@bot.message_handler(func=lambda message: get_user_step(message.from_user.username) == "AWAITING_FILE", content_types=['document'])
def handle_document(message):
    user_tag = message.from_user.username
    file_name = message.document.file_name
    if not (file_name.endswith('.xls') or file_name.endswith('.xlsx')):
        bot.send_message(message.chat.id, "Пожалуйста, отправьте файл в формате Excel.")
        return
    user_data[user_tag]['file_id'] = message.document.file_id
    user_data[user_tag]['step'] = "AWAITING_EVENT_NAME"
    bot.send_message(message.chat.id, "Файл принят. Теперь введите уникальное название мероприятия.")


# Обработчик для получения названия события
@bot.message_handler(func=lambda message: get_user_step(message.from_user.username) == "AWAITING_EVENT_NAME")
def event_name_received(message):
    user_tag = message.from_user.username
    event_name = message.text
    #TODO Проверка на уникальность названия и редактирование события, РАБОТА С БД
    user_data[user_tag]['event_name'] = event_name
    user_data[user_tag]['step'] = "AWAITING_COMMANDS"
    bot.send_message(message.chat.id, f"Событие '{event_name}' создано/отредактировано. Используйте команды для управления событием.")


