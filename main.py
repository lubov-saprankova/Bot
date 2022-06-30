import telebot

bot = telebot.TeleBot('5418028364:AAHmoqBwack5F-6QAPhCqKHxGKdWiduIcZ0')


@bot.message_handler(func=lambda message: 'привет' == message.text)
def привет(message):
    bot.send_message(message.from_user.id, 'Привет')


@bot.message_handler(func=lambda message: 'пока' == message.text)
def пока(message):
    bot.send_message(message.from_user.id, 'Пока')

@bot.message_handler(func=lambda message:True)
def другое_сообщение(message):
    bot.send_message(message.from_user.id, 'Я тебя не понимаю')



bot.polling(none_stop=True, interval=0)

