import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import telebot
from telebot import types
from scripts.main import Main

scripts = Main() # Наследник скриптов


bot = telebot.TeleBot("5209292573:AAFocNzim1MFe5Q_KYokBNOzOLysuCpvSpo") # Бот


# Старт 
@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    passGen = types.KeyboardButton("/Сгенирировать_пароль")
    startTests = types.KeyboardButton("/Запуск_теста")
    markup.add(passGen)
    markup.add(startTests)
    bot.send_message(message.chat.id, "Привет", reply_markup=markup)


# Генератор пароля
from scripts.main import passwordGenerator as passwordGenerator
@bot.message_handler(commands=["Сгенирировать_пароль"])
def password_generator(message):
    scripts.passwordGenerator(8)
    bot.send_message(message.chat.id, "Генератор пароля: " + scripts.passwordGenerator(8))


# Тесты
from tests.test_main import *
@bot.message_handler(commands=["Запуск_теста"])
def tests(message):
    pass


bot.polling(none_stop=True, interval=0)  # Старт бота



# https://thecode.media/python-bot/