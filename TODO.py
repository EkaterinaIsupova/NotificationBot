def format_excel_file(file_id, event_name):
    # Заглушка для функции обработки файла
    # Сюда будет вставлена реальная функция обработки файла
    pass


def get_event_list_for_user(user_tag):
    # Заглушка для функции, которая должна быть реализована для работы с базой данных
    # Возвращаем тестовые данные
    return {
        'Курс по тестированию': {
            'дедлайн1': '2024-04-30 23:59',
            'дедлайн2': '2024-05-15 23:59'
        },
        'Проект по программированию': {
            'дедлайн3': '2024-06-01 12:00'
        }
    }

# Предполагаем, что функции для взаимодействия с базой данных уже существуют
def add_participants(event_name, user_tags):
    # Добавляет список участников к событию в базе данных
    pass

def remove_participants(event_name, user_tags):
    # Удаляет список участников из события в базе данных
    pass

def set_reminder_time(event_name, time_before):
    # Устанавливает время для отправки уведомлений перед дедлайном
    pass