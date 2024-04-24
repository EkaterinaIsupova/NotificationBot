def format_excel_file(file_id):
    # Заглушка для функции обработки файла
    # Сюда будет вставлена реальная функция обработки файла
    task = file_id['task']
  if not isinstance(task, str):
    raise TypeError("поле 'task' должно быть типа str")
  
  descr = file_id['description']
  if not isinstance(descr, str):
    raise TypeError("поле 'description' должно быть типа int")
  
  date_time_obj = datetime.datetime.strptime(str(file_id['date/time']), '%Y-%m-%d %H:%M:%S')
  if not isinstance(date_time_obj, datetime.date):
    raise TypeError("поле 'date_time_obj' должно быть типа datetime")
  
  deadline = int(file_id['time_before_the_deadline'])
  if not isinstance(deadline, int):
    raise TypeError("поле 'time_before_the_deadline' должно быть типа int")
  if deadline <= 0:
    raise ValueError("В поле 'time_before_the_deadline' должно храниться положительное число")
  
  for sentence in file_id['receiverse']: 
    words = sentence.split()
  particip = file_id['receiverse'].split()
  if not isinstance(particip, list):
    raise TypeError("поле 'receiverse' должно быть типа list")
  
  return {'task': task, 'description': descr, 'date/time': date_time_obj, 'time_before_the_deadline': deadline, 'receiverse': particip}


def get_event_list_for_user(user_tag) -> dict | None:
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


def save_user(username, chat_id):
    # сохранение соответствия между тегом пользователя и номером чата для будущих рассылок.
    # сохранение происходит когда пользователь первый раз пишет /start боту
    return


def save_event(event_name, parsed_file_data):
    #сохраняем в БД полную информацию о событии, включая получателей
    return


def get_events_info(username) -> str | None:
    #вернуть информацию о всех ивентах созданных пользователем (команда listme)
    return None


def get_notification_receivers() -> dict | None:
    # Заглушка, возвращающая список ближайших уведомлений которые уже пора отправлять
    return {
        '@user71424': 'скоро дедлайн "отправка теста 1", осталось 30 минут',
        '@user2': 'скоро дедлайн "подготовка отчета", осталось 45 минут'
    }


def get_chat_id(tg_tag) -> int | None:
    # получаем чат id по тегу
    return None

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
