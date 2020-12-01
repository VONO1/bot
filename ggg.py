# Подключаем модуль случайных чисел
import random
# Подключаем модуль для Телеграма
import telebot

# Указываем токен
client = telebot.TeleBot('1457884681:AAF9GjlOLP7hlhlqimmIMm5heybKXv-Ig28')

client.enable_save_next_step_handlers(delay=2)
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types

markup_inline = types.InlineKeyboardMarkup()
item_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
item_no = types.InlineKeyboardButton(text='нет', callback_data='no')
markup_inline.add(item_yes, item_no)

@client.message_handler(commands=['get_info', 'info'])
def get_user_info(message):

    client.send_message(message.chat.id, 'Начало', reply_markup=markup_inline)


@client.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'yes':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True , one_time_keyboard = False)

        item_id = types.KeyboardButton('МОЙ ID')
        item_username = types.KeyboardButton('МОЙ НИК')
        item_opros = types.KeyboardButton('ОПРОС')


        markup_reply.add(item_id, item_username,item_opros)
        client.send_message(call.message.chat.id, 'Нажмите одну из кнопок', reply_markup=markup_reply)

    elif call.data == 'no':
        pass



@client.message_handler(content_types=['text'])
def get_text(message):
    if message.text == 'МОЙ ID':
        client.send_message(message.chat.id, f'Your ID: {message.from_user.id}')
    elif message.text == 'МОЙ НИК':
        client.send_message(message.chat.id, f'Your ID: {message.from_user.first_name}{message.from_user.last_name}')
    elif message.text == 'ОПРОС':
        client.send_message(message.chat.id, 'Введите ваше имя')
        client.register_next_step_handler(message, get_surname)

def get_surname(message):
    client.send_message(message.chat.id, 'Вводи сука!!!')
    client.register_next_step_handler(message, get_suka)

def get_suka(message):
    client.send_message(message.chat.id, 'Начало', reply_markup=markup_inline)





client.polling(none_stop = True, interval = 0)

