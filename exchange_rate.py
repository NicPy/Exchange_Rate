# token:  670031071:AAHrQnnXwVUWn9XUHwcqCeRovhL8_jII2iA

import telebot
import parser
import urllib.request
import json
from urllib.request import Request, urlopen

req = Request('http://resources.finance.ua/ru/public/currency-cash.json', headers={'User-Agent': 'Mozilla/5.0'})
file = urlopen(req)
jsn = file.read()
decoded = (json.loads(jsn))
dollar = decoded['organizations'][1]['currencies']['USD']['ask']
euro = decoded['organizations'][1]['currencies']['EUR']['ask']
rubl = decoded['organizations'][1]['currencies']['RUB']['ask']
# print(json.JSONEncoder().encode(str(jsn)))
# dic = json.load(jsn)



TOKEN = "670031071:AAHrQnnXwVUWn9XUHwcqCeRovhL8_jII2iA"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == "привет":
        bot.send_message(chat_id, 'Привет, я бот - парсер доллара.')
    elif text == "доллар":
        bot.send_message(chat_id, 'Доллар сегодня по ' + str(dollar))
    elif text == "евро":
        bot.send_message(chat_id, 'Евро сегодня по ' + str(euro))
    elif text == "рубль":
        bot.send_message(chat_id, 'Рубль сегодня по ' + str(rubl))
    else:
        bot.send_message(chat_id, 'Простите, я вам не понял :(')

bot.polling()