import os

import telebot
from flask import Flask, request

TOKEN = '616278926:AAHKgVpqO8vo1kSPyTmFE76X7h3AIE6meII'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://curserabot.herokuapp.com/' + TOKEN)
    return "!", 200


if __name__ == "__main__":
    my_port = int(os.environ.get('PORT', 5000))
    server.run(host="0.0.0.0", port=my_port)