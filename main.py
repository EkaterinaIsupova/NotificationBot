import telebot
from config import load_configuration
from commands import bot
from threading import Thread
import time
from TODO import *


def send_notifications():
    while True:
        receivers = get_notification_receivers()
        for username, message in receivers.items():
            chat_id = get_chat_id(username)
            if get_chat_id(username) is not None:
                try:
                    bot.send_message(chat_id, message)
                except telebot.apihelper.ApiException as e:
                    print(f"Не удалось отправить сообщение пользователю {username}: {str(e)}")
        time.sleep(60)  # Пауза между проверками уведомлений


notification_thread = Thread(target=send_notifications)
notification_thread.start()

bot.polling(none_stop=True)


