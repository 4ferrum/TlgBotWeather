# Телеграм бот
import pyowm
import telebot

owm = pyowm.OWM("04288af9666a79abd3a565b5028a54bd", language='ru')
bot = telebot.TeleBot("840679200:AAGvoQ0LYO7BsJE4iB7XmAOmEfSd8qFteQs")



@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    temp = w.get_temperature('celsius')['temp']
    status = w.get_detailed_status()
    answer = 'В городе ' + message.text + ' сейчас ' + status + "\n"
    answer += 'Температура сейчас в районе ' + str(temp) + '\n\n'
    bot.send_message(message.chat.id, answer)

bot.infinity_polling(True)
# bot.polling( none_stop = True )
