import pyowm
import telebot
from telebot import types


token = '830151101:AAEkELYrza6crizQFIMsDft_VKIIzQVNtCs'
bot = telebot.TeleBot(token)
owm = pyowm.OWM('0fc87cf103fb64ec880d2b8fb3ecf0d4', language = 'ru')


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Привет, Я бот Погодки!' + '\nЯ знаю погоду на всей планете!!' + '\n\nПодробнее - /help')
    bot.send_message(message.chat.id, 'Введи город: ', reply_markup=keyboard())

def keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button_1 = types.KeyboardButton('Санкт-Петербург')
    button_2 = types.KeyboardButton('Барселона')
    markup.add(button_1)
    markup.add(button_2)
    return markup
@bot.message_handler(commands=['help'])
def handle_start(message):
    bot.send_message(message.chat.id,'Чтобы узнать погоду, введи город' + '\nНапример: "Москва"' + '\n\nБот создал Рома Рахлин')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Барселона':
        observation = owm.weather_at_place('barcelona')
        w = observation.get_weather()
        temp = w.get_temperature('celsius')['temp']
        answear = 'В городе Барселона' + ' сейчас ' + w.get_detailed_status() + '\n' + 'Температура: ' + str(temp) + ' градусов'
        bot.send_message(message.chat.id, answear)
    elif message.text == 'Санкт-Петербург':
        observation = owm.weather_at_place('санкт-петербург')
        w = observation.get_weather()
        temp = w.get_temperature('celsius')['temp']
        answear = 'В городе Санкт-Петербург' + ' сейчас ' + w.get_detailed_status() + '\n' + 'Температура: ' + str(temp) + ' градусов'
        bot.send_message(message.chat.id, answear)
    else:
        observation = owm.weather_at_place(message.text)
        w = observation.get_weather()
        temp = w.get_temperature('celsius')['temp']
        answear = 'В городе ' + message.text + ' сейчас ' + w.get_detailed_status() + '\n' + 'Температура: ' + str(temp) + ' градусов'
        bot.send_message(message.chat.id, answear)


bot.polling(none_stop=True, timeout=60)
