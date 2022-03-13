import telebot
import config

stis_bot = telebot.TeleBot(config.stis_bot_token)
@stis_bot.message_handler(commands=['start'])
def Start(message):
    stis_bot.send_message(message.chat.id, "Привет! Рады вас видеть!")


stis_bot.polling(non_stop=True)
