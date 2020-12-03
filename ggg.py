# -*- coding: utf8 -*-

Xr = 0
Q = 1

import telebot
import requests

# Указываем токен
client = telebot.TeleBot('1457884681:AAF9GjlOLP7hlhlqimmIMm5heybKXv-Ig28')
client.enable_save_next_step_handlers(delay=2)
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types
from requests import get
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
help_salf= types.InlineKeyboardButton(text='Техники самопомощи ', callback_data='get_tech')
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
mainn = types.InlineKeyboardButton(text='Главное меню', callback_data='get_user_info')
inst_menu.add(inst1, inst2, mainn)


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

#МЕНЮ ТЕХНИКИ
tech_menu = types.InlineKeyboardMarkup(row_width=1)
B_TECH1 = types.InlineKeyboardButton(text='Техника осознанности «Изюм»', callback_data='TECH1')
B_TECH2 = types.InlineKeyboardButton(text='Практика «5-4-3-2-1»  ', callback_data='TECH2')
B_TECH3 = types.InlineKeyboardButton(text='Переключение внимания', callback_data='TECH3')
B_TECH4 = types.InlineKeyboardButton(text='Техника STOP/ СТОП', callback_data='TECH4')
B_TECH5 = types.InlineKeyboardButton(text='Техника работы с телом', callback_data='TECH5')
B_TECH6 = types.InlineKeyboardButton(text='Рюкзак тревоги', callback_data='TECH6')
B_TECH7 = types.InlineKeyboardButton(text='Техника дыхания', callback_data='TECH7')
B_TECH8 = types.InlineKeyboardButton(text='Прогрессивно-мышечная релаксация по Джекосбону.', callback_data='TECH8')
mainn = types.InlineKeyboardButton(text='Главное меню', callback_data='get_user_info')
tech_menu.add(B_TECH1,B_TECH2,B_TECH3,B_TECH4,B_TECH5,B_TECH6,B_TECH7,B_TECH8,mainn)

def sendd():
    requests.get('https://api.telegram.org/bot{}/sendMessage'.format(client),params=dict(chat_id='@Vitalii_super_bot', text='Hello world!'))

@client.message_handler(commands=['start'])
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
    elif call.data == 'get_tech':
        client.send_message(call.from_user.id, text=' Помните, что техники станут только помогающим инструментом при работе с тревогой. Они не заменяют полноценных консультаций.',reply_markup=tech_menu)
    elif call.data == 'TECH1':
        client.send_message(call.from_user.id, text= ' Для этого упражнения вам понадобится обычная изюминка. Сядьте в спокойном месте. Закройте глаза. Возьмите изюминку. \n Притворитесь, что Вы никогда ее раньше не видели. Обратите особое внимание на то: \n • как она выглядит; \n • как ощущается в руке; \n • как поверхность изюма реагирует на контакт с телом; \n • как она пахнет; \n • какая она на вкус; \n • какого размера; \n Сосредоточьте свое внимание полностью на изюминке и доведите до сознания, что именно у Вас сейчас в руках/ рту. Опишите все физические и химические качества изюминки. \n Делайте это упражнение 2 раза в день минимум на протяжении месяца', reply_markup=tech_menu)
    elif call.data == 'TECH2':
        client.send_message(call.from_user.id, text= ' Практика «5-4-3-2-1» \n ⠀ Замечательное упражнение, чтобы преодолеть бессмысленное беспокойство и вернуться в момент «здесь и сейчас». Практика «5-4-3-2-1» – это простой, но эффективный инструмент восстановления контроля над сознанием, когда беспокойство пытается взять над ним верх, и она включает в себя гораздо больше, чем просто обратный отсчет от пяти до одного. Упражнение помогает вернуться в реальность благодаря органам чувств – зрению, слуху, осязанию, обонянию и вкусу. \n ⠀ Итак: \n 1. Посмотрите вокруг и отметьте ПЯТЬ предметов, которые вы видите в данный момент. \n 2. Далее прислушайтесь к звукам и выделите ЧЕТЫРЕ из тех, что вы сейчас слышите. \n 3. Теперь обратите внимание на ТРИ осязательных ощущения. Это может быть что угодно: ваши ноги в ботинках, кольцо на пальце, шапка на голове и т. д. \n 4. Затем очередь обоняния: почувствуйте ДВА запаха в пространстве, где вы находитесь. 5. Наконец, ощутите ОДИН вкус. Это даже может быть просто ваш язык, если вы сможете почувствовать его вкус. ⠀\n Такое фокусирование внимания на органах чувств позволяет сосредоточиться на настоящем, а подсчет предметов приостанавливает круговорот мыслей.', reply_markup=tech_menu)
    elif call.data == 'TECH3':
        client.send_photo(call.from_user.id, get("https://yadi.sk/i/XF2TC6nLR7Gz3w").content)
        client.send_message(call.from_user.id, text= ' Переключение внимания \n Вроде бы всё очень просто и понятно - надо просто заняться любым делом, которое тебя отвлечёт. Когда начинает накрывать паническая атака, этот, до банальности простой способ справиться с ней, почему-то не приходит в голову. \n Мы подготовили небольшую карточку с описанием техники, чтобы вы могли её себе сохранить и пользоваться при необходимости! \n', reply_markup=tech_menu)
    elif call.data == 'TECH4':
        client.send_message(call.from_user.id, text= ' Престо не реагируй. \n Остановись! Замри! Не шевелись! Твои эмоции могут побуждать к действию, не раздумывая. Сохраняй над собой контроль! \n \n Сделай шаг назад. \n Сделай перерыв: сделай глубокий вдох. Отпусти ситуацию. Не дай своим чувствам заставить тебя действовать импульсивно\n \n Осмотрись. \n Обрати внимание на то, что происходит вокруг и внутри тебя. Наблюдай. Какова ситуация? Обрати внимание на свои мысли нарушения. Что говорят или делают другие? \n \n Продолжай, сохраняя осознанность. \n Принимая решение, что делать дальше, учитывай свои мысли и эмоции, саму ситуацию. Какие твои действия улучшат или ухудшат ситуацию? \n', reply_markup=tech_menu)
    elif call.data == 'TECH5':
        client.send_message(call.from_user.id, text= ' Техника работы с телом \n Если я чувствую тревожные симптомы в теле: \n 1.	Я с тревогой не борюсь. \n 2.	Я описываю свою тревогу. \n 3.	Я закрываю глаза и визуализирую её. \n 4.	Я придаю ей форму, объем, цвет, фактуру, материализую. \n 5.	Я наблюдаю за трансформацией моей тревоги. \n 6.	Я наблюдаю как она движется. \n 7.	Я наблюдаю за тем как отзывается тело на ее движения. \n 8.	Я не борюсь с этими чувствами               в теле. \n 9.	Я предоставляю еще больше пространства тревоге в теле. \n 10.	Я расширяю границы. \n 11.	Я наблюдаю как тревога увеличивается в этом пространстве, но не конфликтую с ней. \n 12.	Я наполняю пространство воздухом. \n 13.	Я наблюдаю, как тревога купается в этом объеме. \n 14.	Я ещё больше раздвигаю границы. \n 15.	Я разрываю эти границы и наблюдаю как весь объем воздуха объединяется с окружающим меня миром. \n', reply_markup=tech_menu)
    elif call.data == 'TECH6':
        client.send_message(call.from_user.id, text= ' Рюкзак тревоги\n • 	Закрой глаза…\n • 	Представь себя с большим тяжелым рюкзаком за плечами\n • 	В нем накопилось много твоих страхов, тревог, обид, разочарований…\n • 	Весь этот груз очень давит и мешает твоему движению вперед. Ты очень устал и хотел бы от него освободиться. \n • 	Представь, что ты  видишь перед собой большое красивое дерево. Подойди к нему ближе, сними с себя этот рюкзак. Ничто и никто не мешает тебе это сделать. \n • 	Открой его. Посмотри какую тяжесть ты носишь! \n • 	Попробуй представить как выглядят твои тревоги, обиды, разочарования? Может это большие тяжелые камни? \n • 	Запусти руку в рюкзак., достань один из камней. Что это за камень? Подумай об этом. Что это за тревога? А может быть обида и злость? \n • 	Продолжай доставать камни из рюкзака. Разглядывай их, задавай себе вопросы:  «Что это за тревога?», «Что это за груз?», «Почему это для тебя так тяжело?» и т.п. \n • 	Складывай камни, которые достаешь из рюкзака под дерево. Не спеши. \n •   Ты можешь потратить столько времени на обдумывание своих эмоций, тяжести от их груза, как тебе захочется. \n • 	Когда твой рюкзак опустеет, ты можешь оставить все эти камни под деревом. \n • 	Почувствуй как стало легко, как распрямились плечи и стало легче дышать. \n • 	Оцени на сколько более расслабленным сейчас ты себя чувствуешь? Сейчас ты даже немножко улыбаешься. \n • 	Надевай свой пустой рюкзак и отправляйся в путь, выбирая важное для себя направление. \n • 	Не бери с собой эти камни, тебе больше не обязательно о них думать. Все важные задачи ты и так решишь, ты полон сил. \n • 	Тебя не беспокоят эти задачи, потому что они важны именно для тебя и ты решишь их с удовольствием, потому что так ты наполнишь себя еще большей радостью. \n • 	Представь себя в безопасном месте, где тебе тепло хорошо и уютно. Понаблюдай за своим состоянием и попробуй запомнить его, чтобы сохранить как можно дольше. \n', reply_markup=tech_menu)
    elif call.data == 'TECH7':
        client.send_message(call.from_user.id, text= ' Основная задача - восстановить баланс кислорода и углекислого газа. \n \n Панический приступ часто сопровождается поверхностным дыханием, из-за чего мы перенасыщаем свой мозг кислородом, параллельно разгоняя панику до своего пика. \n \n  Положите руку на живот, вдыхайте медленно и спокойно, считая до четырех, а затем медленно и спокойно выдыхайте, считая до шести-семи. Старайтесь дышать таким образом, чтобы чувствовать, как рука поднимается и опускается на животе. \n \n Во время практики дыхания различные мысли могут пытаться переключить ваше внимание от выполнения упражнения на приступ ПА. Если такое происходит, просто отметьте этот факт, а затем плавно переведите свое внимание обратно на дыхание. \n \n Чтобы легче переключить своё внимание, можете представить, как ваши лёгкие увеличиваются наполняясь воздухом, когда вы вдыхаете и уменьшаются, когда вы выдыхаете. \n \n Продолжайте дышать 5-10 минут, пока приступ не пойдет на спад', reply_markup=tech_menu)
    elif call.data == 'TECH8':
        client.send_message(call.from_user.id, text= 'https://www.youtube.com/watch?v=NbPVaC6a5vM&t=656s ', reply_markup=tech_menu)



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

