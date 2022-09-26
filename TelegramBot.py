import telebot
from Conf import TOKEN, keys
from extensions import ConExc, Convert

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message: telebot.types.Message):
    text = 'Для перевода валют введите ⌨️:\n <имя валюты, которую переводим> \
    <валюту, в которую переводим> \
    <количество переводимой валюты>\n /currency - список всех доступных валют 💸'
    bot.reply_to(message, text)


@bot.message_handler(commands=['currency'])  # я заменил /values на /currency, но смысл остался тот же
def currency(message: telebot.types.Message):
    text = 'Доступные валюты 🤑'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise ConExc('Неверное количество параметров!')
        base, quote, amount = values
        total = Convert.convert(base, quote, amount)
    except ConExc as e:
        bot.reply_to(message, f'Ошибка пользователя!\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду!\n{e}')
    else:
        mes_s = f"Цена {amount} {base} в {quote} - {total}"
        bot.send_message(message.chat.id, mes_s)


bot.polling()
