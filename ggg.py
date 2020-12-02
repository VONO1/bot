Xr = 0
Q = 1

import telebot
import requests

# Указываем токен
client = telebot.TeleBot('1457884681:AAF9GjlOLP7hlhlqimmIMm5heybKXv-Ig28')
client.enable_save_next_step_handlers(delay=2)
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types



markup = types.ReplyKeyboardMarkup(True)
key1 = types.KeyboardButton('START')
markup.add(key1)



symptoms = [
'затруднение на вдохе, нехватка воздуха или учащенное дыхание',
'Ощущение удушья или комка в горле',
'что сердце скачет, колотится, готово выскочить из груди',
'Боль в груди, неприятное чувство сдавления в груди',
'сильную потливость («пот градом»)',
'Слабость, приступы дурноты, головокружения',
'"Ватные, "не свои" ноги',
'Ощущение неустойчивости или потери равновесия',
'тошноты или неприятные ощущения в животе',
'Ощущение того, что всё окружающее становится странным, нереальным, туманным или отстраненным',
'Ощущение, что всё плывет, "нахожусь вне тела"',
'Покалывание или онемение в разных частях тела',
'Приливы жара или озноба',
'Дрожь (тремор)',
'Страх смерти или того, что сейчас может произойти что-то ужасное',
'Страх сойти с ума или потери самообладания',
'Внезапные приступы тревоги, сопровождающиеся тремя или более из вышеперечисленных признаков (дрожь, страх смерти, страх сойти с ума), возникающие непосредственно перед и при попадании в ситуацию, которая, по Вашему опыту, может вызвать приступ',
'Внезапные неожиданные приступы тревоги, сопровождающиеся тремя или более из выше перечисленных признаков (дрожь, страх смерти, страх сойти с ума), возникающие по незначительным поводам или без повода ( т.е., когда Вы НЕ находитесь в ситуации, которая, по вашему опыту, может вызвать приступ)',
'Внезапные неожиданные приступы, сопровождающиеся одним или двумя из вышеперечисленных признаков (дрожь, страх смерти, страх сойти с ума), возникающие по незначительным поводам или без повода (т.е. , когда Вы НЕ находитесь в ситуации, которая, по Вашему опыту, может вызвать приступ)',
'Периоды тревоги, нарастающей по мере того, как Вы готовитесь сделать что-то, что, по вашему опыту, может вызвать тревогу, причем более сильную, чем ту, что в таких случаях испытывает большинство людей',
'что избегаете пугающих вас ситуаций',
'Состояние зависимости от других людей',
'Напряженность и неспособность расслабиться',
'тревогу, "нервозность", беспокойство',
'Приступы повышенной чувствительности к звуку, свету и прикосновению',
'Приступы поноса',
'Чрезмерное беспокойство о собственном здоровье',
'Ощущение усталости, слабости и повышенной истощаемости',
'Головные боли или боли в шее',
'Трудности засыпания',
'беспокойный сон или просыпаетесь среди ночи',
'неожиданные периоды депрессии, возникающие по незначительным поводам или без повода',
'перепады настроения и эмоций, которые в основном зависят от того, что происходит вокруг Вас',
'повторяющиеся и неотступные представления, мысли, импульсы или образы, которые Вам кажутся тягостными, противными, бессмысленными или отталкивающими',
'повторение одного и того же действия как ритуала, например, повторные перепроверки, перемывание и пересчет при отсутствии в этом действии необходимости'
]
results = ['баллов. Поздравляем! У Вас отсутствует клинически выраженная тревога. Соблюдайте режим дня! Береги себя! Продолжайте поддерживать свой уровень ментального здоровья!',
'Что-то пошло не так. Наш бот определил, что скорее всего у Вас присутствует клинически выраженная тревога!',
'баллов. Упссс! Бот говорит, что откладывать свою тревогу в долгий ящик не получится. Мы очень рекомендуем Вам в ближайшее время сходить на прием к своему лечащему доктору или участковому психотерапевту/ психиатру. Сообщите ему, что по шкале самооценки тревоги SPRA Д. Шихана у Вас обнаружены высокие баллы! Сообщаем, что в современных условиях тревожные расстройства поддаются успешной коррекции.'
]



#ГЛАВНОЕ МЕНЮ:
bot_main_menu = types.InlineKeyboardMarkup(row_width=1)
item_no = types.InlineKeyboardButton(text='Тест самооценки тревоги \n SPRA Д. Шихана', callback_data='question')
open_chat = types.InlineKeyboardButton(text='Открытый чат группы ПОПА ',url="https://t.me/joinchat/EZkYyBvRq8f4A_uzelWPig")
close_chat = types.InlineKeyboardButton(text='Закрытый чат с Денисом и Виталием', callback_data='zodiac')
you_tube = types.InlineKeyboardButton(text='Наш канал YouTube',url="https://www.youtube.com/channel/UC5i4yB4eOdLyA-eXv1Hi5cg?view_as=subscriber")
help_salf= types.InlineKeyboardButton(text='Техники самопомощи ', callback_data='zodiac')
d_app = types.InlineKeyboardButton(text='Скачать приложение Без тревоги', url="https://example.com")
kons = types.InlineKeyboardButton(text='Записаться на индивидуальную консультацию', callback_data='zodiac')
insta = types.InlineKeyboardButton(text='Мы в Инстаграм', callback_data='instagrams')
bot_main_menu.add(item_no,open_chat,close_chat,you_tube,help_salf,d_app,kons,insta)


#МЕНЮ ТЕСТА
test_menu = types.InlineKeyboardMarkup(row_width=1)
mmm1 = types.InlineKeyboardButton(text='Нет', callback_data='get_user_info1')
mmm2 = types.InlineKeyboardButton(text='Немного', callback_data='get_user_info2')
mmm3 = types.InlineKeyboardButton(text='Умеренно', callback_data='get_user_info3')
mmm4 = types.InlineKeyboardButton(text='Сильно', callback_data='get_user_info2')
mmm5 = types.InlineKeyboardButton(text='Крайне сильно', callback_data='get_user_info3')
test_menu.add(mmm1, mmm2, mmm3, mmm4, mmm5)

#МЕНЮ ИНСТАГРАМ@
inst_menu = types.InlineKeyboardMarkup(row_width=1)
inst1 = types.InlineKeyboardButton(text='Сидняев Виталий', url="https://www.instagram.com/sidnyaev_psy/")
inst2 = types.InlineKeyboardButton(text='Денис Иванов', url="https://www.instagram.com/id_psy/")
inst_menu.add(inst1, inst2)


#МЕНЮ ПОЛУЧЕНИЯ РЕЗУЛЬТАТОВ
result_menu = types.InlineKeyboardMarkup()
ras = types.InlineKeyboardButton(text='Получить рекомендации', callback_data='get_user_mail')
# item_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
result_menu.add(ras)

#МЕНЮ ОПЛАТЫ
privat_menu = types.InlineKeyboardMarkup()
pay = types.InlineKeyboardButton(text='Оплатить', callback_data='get_user_mail')
# item_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
privat_menu.add(pay)


def sendd():
    requests.get('https://api.telegram.org/bot{}/sendMessage'.format(client),params=dict(chat_id='@Vitalii_super_bot', text='Hello world!'))

@client.message_handler(commands=['START'])
def get_user_info(message):
    client.send_message(message.chat.id, 'Выберите нужный раздел', reply_markup=bot_main_menu)


@client.callback_query_handler(func=lambda call: True)
def answer(call):
    def SUPERFUNCTION(z):

        global Xr
        global Q
        Xr = Xr + z
        if Q < len(symptoms):
            print('Номер вопроса:', Q+1)
            print('Длина списка', len(symptoms))
            Q = Q + 1
            client.send_message(call.from_user.id, text='Вопрос '+ str(Q) + '/' + str(len(symptoms))+'\n' +'Как сильно Вы ощущаете ' + symptoms[(Q-1)].lower(), reply_markup=test_menu)
        else:
            if Xr <30:
                znn = 0
            if Xr >= 80:
                znn = 2
            if 80 > Xr & Xr > 30:
                znn = 1
            client.send_message(call.from_user.id, 'Ваш результат: ' + str(Xr) + ' балла(ов)'+'\n' + results[znn], reply_markup=result_menu)

    if call.data == 'yes':
        pass
        # markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True , one_time_keyboard = False)
        # item_id = types.KeyboardButton('МОЙ ID')
        # item_username = types.KeyboardButton('МОЙ НИК')
        # item_opros = types.KeyboardButton('ОПРОС')
        # markup_reply.add(item_id, item_username,item_opros)
        # client.send_message(call.message.chat.id, 'Нажмите одну из кнопок', reply_markup=markup_reply)

    elif call.data == 'question':
        client.send_message(call.from_user.id, text= 'Вопрос '+ str(Q) + '/' + str(len(symptoms))+'\n' +'Как сильно Вы ощущаете ' + symptoms[Q].lower(), reply_markup=test_menu)
    elif call.data == 'get_user_info1':
        SUPERFUNCTION(0)
    elif call.data == 'get_user_info2':
        SUPERFUNCTION(1)
    elif call.data == 'get_user_info3':
        SUPERFUNCTION(2)
    elif call.data == 'get_user_info4':
        SUPERFUNCTION(3)
    elif call.data == 'get_user_info5':
        SUPERFUNCTION(4)
    elif call.data == 'get_user_mail':
        client.send_message(call.message.chat.id, 'Пожалуйста введите ваш email')
    elif call.data == 'instagrams':
        client.send_message(call.from_user.id, text= 'Ежедневно обновляемый, самый актуальный материал о КПТ и о нашей жизни в наших аккаунтах', reply_markup=inst_menu)

@client.message_handler(content_types=['text'])
def get_text(message):
    if message.text == 'МОЙ ID':
        client.send_message(message.chat.id, f'Your ID: {message.from_user.id}')
    elif message.text == 'МОЙ НИК':
        client.send_message(message.chat.id, f'Your ID: {message.from_user.first_name}{message.from_user.last_name}')
    elif message.text == 'ОПРОС':
        client.send_message(message.chat.id, 'Введите ваше имя')
        client.register_next_step_handler(message, get_user_mail)
    if '@' in message.text:
        sendd()
        requests.get('https://api.telegram.org/bot{}/sendMessage'.format('1457884681:AAF9GjlOLP7hlhlqimmIMm5heybKXv-Ig28'),params=dict(chat_id='@Vitalii_super_bot', text=message.text))
        client.send_message(message.chat.id, 'Спасибо! Рекомендации будут отправлены на ваш адрес', reply_markup=bot_main_menu)

def go_main_menu(message):
    print('мы здесь')
    client.send_message(message.chat.id, 'Выберите раздел:', reply_markup=bot_main_menu)
    # client.send_message(message.chat.id, 'Пожалуйста введите ваш email')
    # client.register_next_step_handler(message, get_suka)

def get_suka(message):
    client.send_message(message.chat.id, 'Вернуться?', reply_markup=inst_menu)





client.polling(none_stop = True, interval = 0)

