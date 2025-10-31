import telebot

bot = telebot.TeleBot("ВАШ КОД СЮДА НАДО")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я простой эхо-бот. Буду повторять все твои сообщения!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, message.text)

bot.polling()
