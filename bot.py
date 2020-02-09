import telebot
import config
import pyowm
import random
import ntplib
from time import ctime
from time import gmtime
from time import localtime
 
from telebot import types
 
bot = telebot.TeleBot(config.TOKEN)
rating = []

@bot.message_handler(commands=['start'])
def welcome(message):
    start_sticker = open('sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, start_sticker)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Рандомное число")
    item2 = types.KeyboardButton("🌡Температура")
    item3 = types.KeyboardButton("🕘Время")
    item4 = types.KeyboardButton("📜Цитата")
    item5 = types.KeyboardButton("🤖Что я могу?")
    item6 = types.KeyboardButton("📟Калькулятор")

 
    markup.add(item1, item2, item3, item4, item5, item6)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот призванный помочь тебе!".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)

 
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
############        
        if message.text == '🎲 Рандомное число' or message.text.lower() == 'рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0,100)))
############
        elif message.text.lower() == 'кто твой создатель?' or message.text.lower() == 'кто твой батя?' or message.text.lower() == 'кто твой отец?':
            cool_sticker = open('sticker2.webp', 'rb')
            cool_sticker2 = open('sticker3.webp', 'rb')
            cool_sticker3 = open('coolsticker4.tgs', 'rb')
            cool_stick_list = [cool_sticker, cool_sticker2, cool_sticker3]
            anwser_list = [
            'Мой создатель @SK_300085!'
            ]
            a1 = random.choice(cool_stick_list)
            a2 = random.choice(anwser_list)
            bot.send_sticker(message.chat.id, a1)
            bot.send_message(message.chat.id, a2)

############      
        elif message.text.lower() == 'как тебя зовут?' or message.text.lower() =='как зовут?' or message.text.lower() =='скажи свое имя' or message.text.lower() =='как тебя зовут' or message.text.lower() =='как зовут':
            nameanwsers = [
            'Бонд, Джеймс Бонд!\nА если честно мое имя Kizi',
            'Меня зовут Kizi!',
            'Мое имя Kizi!',
            'Mi nombre es kizi!\n(пс, если не понял, меня зовут Kizi)'
            ]
            nameanws = random.choice(nameanwsers)
            bot.send_message(message.chat.id, random.choice(nameanwsers))
############
        elif message.text == '😊 Как дела?' or message.text.lower() == 'как дела?' or message.text.lower() == 'как твои дела?':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')
 
            markup.add(item1, item2)
            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
############
        elif message.text == '🌡Температура' or message.text.lower() == 'какая сейчас температура?' or message.text.lower() =='какова температура' or message.text.lower() =='скажи температуру' or message.text.lower() =='температура':
            bot.send_message(message.chat.id, 'Какой город вам нужен?\n==========================\nВведите "!" и город который вам нужен\nНапример !Москва')
        elif message.text[0] == '!':
            city = message.text[1:]
            owm = pyowm.OWM('99c544c30e3a7c7d4d2670d7611b36e8')

            try:
                observation = owm.weather_at_place(city)
                w = observation.get_weather()
                temperature = w.get_temperature('celsius')['temp']
                bot.send_message(message.chat.id, '🌡В городе {0} сейчас температура: {1} C'.format(city, str(temperature)))
            except:
                bot.send_message(message.chat.id, 'Вы ввели несуществующий город,\nили этот город находится в каком-то "Мухосранске"!')
############       
        elif message.text == '🕘Время' or message.text.lower() == 'время' or message.text.lower() =='сколько сейчас время?' or message.text.lower() =='время не подскажешь?':
            client = ntplib.NTPClient()
            response = client.request('ru.pool.ntp.org')
            timenow = localtime(response.tx_time)
            time_sticker = open('timesticker.tgs', 'rb')
            bot.send_sticker(message.chat.id, time_sticker)
            bot.send_message(message.chat.id, '🕘Время: {0:02d}:{1:02d}:{2:02d}'.format(timenow.tm_hour, timenow.tm_min, timenow.tm_sec))
############
        elif message.text == '📜Цитата' or message.text.lower() == 'цитата' or message.text.lower() =='' or message.text.lower() =='расскажи цитату':
            quote_list = [
            'Если у тебя получилось обмануть человека, это не значит, что он дурак, это значит, что тебе доверяли больше, чем ты этого заслуживаешь.',
            'Не тот велик, кто никогда не падал, а тот велик — кто падал и вставал!',
            'Танцуй так, как будто на тебя никто не смотрит. Пой, как будто тебя никто не слышит. Люби так, как будто тебя никогда не предавали, и живи так, как будто земля — это рай.',
            'Заведите себе «идиотскую» привычку радоваться неудачам. Это гораздо веселей, чем раздражаться и ныть по любому поводу.'
            ]

            quote = random.choice(quote_list)
            bot.send_message(message.chat.id, quote)

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Да", callback_data='yes')
            item2 = types.InlineKeyboardButton("Нет", callback_data='no')

            markup.add(item1, item2)
            bot.send_message(message.chat.id, 'Хотите оценить цитату?', reply_markup=markup)

        elif message.text.lower()[0:6] == 'оценка':
            bot.send_message(message.chat.id, 'Оценка сохранена!')
            rating.append(message.text.lower()[-1])

        
        elif  message.text.lower() == '/liststatus':
            bot.send_message(message.chat.id, rating)

############
        elif message.text.lower() == 'игры' or message.text.lower() == 'игра':
            bot.send_message(message.chat.id, 'Coming soon!')

        elif message.text.lower() == 'квест':
            bot.send_message(message.chat.id, 'Coming soon!')
            #am = open('AzbukaMorza.jpg', 'rb')
            #bot.send_photo(message.chat.id, am)
############
        elif message.text == '📟Калькулятор' or message.text.lower() == 'калькулятор':
            bot.send_message(message.chat.id, 'x + y  Сложение\nx - y  Вычитание\nx * y  Умножение\nx / y  Деление\n x // y  Целочисленное деление\nx % y  Остаток от деления\n x ** y  Возведение в степень')
            bot.send_message(message.chat.id, 'Введите выражение:')
        elif '%' in message.text or '+' in message.text or '-' in message.text or '*' in message.text or '/' in message.text:
            try:
                x = message.text
                bot.send_message(message.chat.id, eval(x))
            except:
                bot.send_message(message.chat.id, 'Ошибка!')
############
        elif message.text == '🤖Что я могу?' or message.text.lower() == 'что ты можешь?' or message.text.lower() == 'что ты умеешь?':
            ican = open('dance.tgs','rb')
            bot.send_sticker(message.chat.id, ican)

            bot.send_message(message.chat.id, 'Запросы:\n     1)Температура\n     2)Время\n     3)Игра\n     4)Рандомное число\nВопросы:\n     1)Как тебя зовут?\n     2)Кто твой создатель?\n     3)Как дела?')   
############
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')
 
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает 😢')
            elif call.data == 'yes':
                bot.send_message(call.message.chat.id, 'Введите "Оценка:" и оцените от 1 до 5\nНапример Оценка: 5')
            elif call.data == 'no':
                bot.send_message(call.message.chat.id, 'Принято!')
 
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="==================",
                reply_markup=None)
 
            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="Вы сделали выбор!")
 
    except Exception as e:
        print(repr(e))
 
# RUN
bot.polling(none_stop=True)