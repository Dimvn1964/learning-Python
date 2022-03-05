import telebot
from config import keys, TOKEN
from extensions import ConvertionException, CryptoConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])                                #создание декоратора, реагирующего на команды "start" и "help" обращением к методу message_handler
def start(message: telebot.types.Message):                                      #функция, обрабатывающая команду
    text = "Рады приветствовать Вас в автоматическом конвертере валют! \
Для начала работы введите команду в следующем формате: \n<название переводимой валюты> \
<в какую валюту перевести><количество переводимой валюты>\nЧтобы увидеть список\
 доступных валют введите /values"                                                #текст сообщения для пользователя
    bot.send_message(message.chat.id, text)                                     #отправка сообщения с текстом text и результатами обхода словаря по ключам. Также пометка сообщения как отвеченного.

@bot.message_handler(commands=['values'])                                       #создание декоратора, реагирующего на команду "values" обращением к методу message_handler
def values(message: telebot.types.Message):                                     #функция, обрабатывающая команду
    text = 'Доступные валюты:'                                                  #текст сообщения для пользователя
    for key in keys.keys():                                                  #цикл обхода по ключам словаря
        text = '\n'.join((text, key, ))                                             #отображение каждой валюты с новой строки
    bot.reply_to(message, text)                                                 #отправка сообщения с текстом text и результатами обхода словаря по ключам. Также пометка сообщения как отвеченного.

@bot.message_handler(content_types=['text', ])                                    #создание декоратора, реагирующего на текст пользователя обращением к методу message_handler
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('Ошибка в количестве параметров. Повторите ввод')

        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя. \n{e}.')
    except Exception as e:
        bot.reply_to(message, f'Ошибка сервера, не удалось обработать команду\n{e}.')
    else:
        text = f'Цена {amount} {quote} составляет {total_base} {base}'
        bot.send_message(message.chat.id, text)

#quote_ticker, base_ticker = keys[quote], keys[base]

bot.polling()