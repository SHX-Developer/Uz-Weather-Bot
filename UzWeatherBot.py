import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup as BS

r = requests.get('https://world-weather.ru/pogoda/uzbekistan/tashkent')
html = BS(r.content, 'html.parser')
bot = telebot.TeleBot("TELEGRAM_API_TOKEN")

for el in html.select('#content'):
    day_t = el.select('.day-temperature')[0].text
    night_t = el.select('.night-temperature')[0].text
    day_d = el.select('.description-weather')[0].text
    print( day_t + night_t + '\n\n' + day_d )

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Андижан','Бухара', 'Джизак','Кашкадарья','Навои','Наманган','Самарканд','Сурхандарья','Сырдарья','Ташкент','Фергана','Хорезм')

@bot.message_handler(commands=['start', 'help'])
def Main(message):
        bot.send_message(message.chat.id, 'Вот погода в Ташкенте:\n' +  "Max  "  + day_t + " ☀" + "    Min  " + night_t + " ❄️" '\n\n' + day_d, reply_markup = keyboard1)

    
@bot.message_handler(content_types=['text'])
def buttons(message):

    markup = types.ReplyKeyboardMarkup(row_width=3)

    button_1 = types.KeyboardButton("Фергана")
    button_2 = types.KeyboardButton("Самарканд")
    button_3 = types.KeyboardButton("Бухара")
    button_4 = types.KeyboardButton("Андижан")

    markup.add(button_1, button_2)

    if message.text == "Андижан":
        bot.send_message(message.chat.id, "Вот погода в Андижане: СКОРО \n" + "Пока что доступен только - Ташкент", reply_markup = keyboard1)
    elif message.text == "Бухара":
        bot.send_message(message.chat.id, "Вот погода в Бухаре: СКОРО \n" + "Пока что доступен только - Ташкент", reply_markup = keyboard1)
    elif message.text == "Джизак":
        bot.send_message(message.chat.id, "Вот погода в Джизаке: СКОРО \n" + "Пока что доступен только - Ташкент", reply_markup = keyboard1)
    elif message.text == "Кашкадарья":
        bot.send_message(message.chat.id, "Вот погода в Кашкадарье: СКОРО \n" + "Пока что доступен только - Ташкент", reply_markup = keyboard1)
    elif message.text == "Навои":
        bot.send_message(message.chat.id, "Вот погода в Навои: СКОРО \n" + "Пока что доступен только - Ташкент", reply_markup = keyboard1)
    elif message.text == "Наманган":
        bot.send_message(message.chat.id, "Вот погода в Намангане: СКОРО \n" + "Пока что доступен только - Ташкент", reply_markup = keyboard1)
    elif message.text == "Самарканд":
        bot.send_message(message.chat.id, "Вот погода в Самарканде: СКОРО \n" + "Пока что доступен только - Ташкент", reply_markup = keyboard1)
    elif message.text == "Сурхандарья":
        bot.send_message(message.chat.id, "Вот погода в Сурхандарье: СКОРО \n" + "Пока что доступен только - Ташкент", reply_markup = keyboard1)
    elif message.text == "Сырдарья":
        bot.send_message(message.chat.id, "Вот погода в Сырдарье: СКОРО \n" + "Пока что доступен только - Ташкент", reply_markup = keyboard1)
    elif message.text == "Ташкент":
        bot.send_message(message.chat.id, 'Вот погода в Ташкенте:\n' +  "Max  "  + day_t + " ☀" + "    Min  " + night_t + " ❄️" '\n\n' + day_d, reply_markup = keyboard1)
    elif message.text == "Фергана":
        bot.send_message(message.chat.id, "Вот погода в Фергане: СКОРО \n" + "Пока что доступен только - Ташкент", reply_markup = keyboard1)
    elif message.text == "Хорезм":
        bot.send_message(message.chat.id, "Вот погода в Хорезме: СКОРО \n" + "Пока что доступен только - Ташкент", reply_markup = keyboard1)


if __name__ == '__main__':
    bot.polling(none_stop=True)