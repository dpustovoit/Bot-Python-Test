import telebot
import requests
from bs4 import BeautifulSoup

r=requests.get('https://ua.sinoptik.ua/погода-чернігів')
html = BeautifulSoup(r.content, 'html.parser')

bot = telebot.TeleBot('5681988844:AAE7_7Du6FQQc5Zht9r8QoFdrxrDSreeg9s')

for el in html.select('#content'):
    t_min = el.select('.temperature .min')[0].text
    t_max = el.select('.temperature .max')[0].text
    desc = el.select('.wDescription.clearfix .description')[0].text

@bot.message_handler(commands=['start'])

def start(message):
    himessage = f'Привіт, <b>{message.from_user.first_name}.</b> Хочеш дізнатися про погоду в Чернігові? Пиши будь-яке слово нижче:'
    bot.send_message(message.chat.id, himessage, parse_mode='html')

@bot.message_handler()

def get_calculations(message):
    bot.send_message(message.chat.id,t_min + ' '+ t_max + '\n' +desc, parse_mode='html')


bot.polling(none_stop=True)