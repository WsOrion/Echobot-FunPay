import telebot

bot = telebot.TeleBot("8255465956:AAHSPEBzYc4yE-Zkj4mj7tfopsTjFUZ2QOc")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я простой эхо-бот. Буду повторять все твои сообщения!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, message.text)

bot.polling()