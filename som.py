import telebot
import time

token = '6826330942:AAGc1eS6WDuJKGpwNQ2QS-5P5P_AHqX0l58'


bot = telebot.TeleBot(token)


@bot.message_handler(commands = ['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Заебумба')


@bot.message_handler(commands = ['timer'])
def say(message):
    for i in range(100):
        time.sleep(1)
        bot.send_message(message.chat.id, i + 1)


@bot.message_handler(commands = ['say'])
def say(message):
    text = ' '.join(message.text.split(' ')[1:])
    bot.reply_to((message, f'***{text.upper()}!***')

@bot.message_handler(content_types=['text'])
def reverse_text(message):
    if 'иди' in message.text.lower():
        bot.reply_to(message, 'Наверни гавна олух')
            return
        text = message.text[::-1]
        bot.reply_to(message, text)


bot.polling()