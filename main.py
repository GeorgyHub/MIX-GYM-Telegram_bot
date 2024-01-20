import telebot
from telebot import types

#plug in Token
bot = telebot.TeleBot("6970971993:AAGmSbXt-zyhmNZdUsDV2Q3CE02Tw3oAFZ4", parse_mode=None)

#functions
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Hello, world?")

#buttons
@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Кнопка")
    markup.add(item1)
    bot.send_message(message.chat.id,'Выберите что вам надо', reply_markup=markup)