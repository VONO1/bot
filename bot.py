


# Подключаем модуль случайных чисел
import random
# Подключаем модуль для Телеграма
import telebot
# Указываем токен
bot = telebot.TeleBot('1457884681:AAF9GjlOLP7hlhlqimmIMm5heybKXv-Ig28')
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types

email = ''
qs = -1
balls = 0
symptoms = [
'затруднение на вдохе, нехватка воздуха или учащенное дыхание',
# 'Ощущение удушья или комка в горле',
# 'что сердце скачет, колотится, готово выскочить из груди',
# 'Боль в груди, неприятное чувство сдавления в груди',
# 'сильную потливость («пот градом»)',
# 'Слабость, приступы дурноты, головокружения',
# '"Ватные, "не свои" ноги',
# 'Ощущение неустойчивости или потери равновесия',
# 'тошноты или неприятные ощущения в животе',
# 'Ощущение того, что всё окружающее становится странным, нереальным, туманным или отстраненным',
# 'Ощущение, что всё плывет, "нахожусь вне тела"',
# 'Покалывание или онемение в разных частях тела',
# 'Приливы жара или озноба',
# 'Дрожь (тремор)',
# 'Страх смерти или того, что сейчас может произойти что-то ужасное',
# 'Страх сойти с ума или потери самообладания',
# 'Внезапные приступы тревоги, сопровождающиеся тремя или более из вышеперечисленных признаков (дрожь, страх смерти, страх сойти с ума), возникающие непосредственно перед и при попадании в ситуацию, которая, по Вашему опыту, может вызвать приступ',
# 'Внезапные неожиданные приступы тревоги, сопровождающиеся тремя или более из выше перечисленных признаков (дрожь, страх смерти, страх сойти с ума), возникающие по незначительным поводам или без повода ( т.е., когда Вы НЕ находитесь в ситуации, которая, по вашему опыту, может вызвать приступ)',
# 'Внезапные неожиданные приступы, сопровождающиеся одним или двумя из вышеперечисленных признаков (дрожь, страх смерти, страх сойти с ума), возникающие по незначительным поводам или без повода (т.е. , когда Вы НЕ находитесь в ситуации, которая, по Вашему опыту, может вызвать приступ)',
# 'Периоды тревоги, нарастающей по мере того, как Вы готовитесь сделать что-то, что, по вашему опыту, может вызвать тревогу, причем более сильную, чем ту, что в таких случаях испытывает большинство людей',
# 'что избегаете пугающих вас ситуаций',
# 'Состояние зависимости от других людей',
# 'Напряженность и неспособность расслабиться',
# 'тревогу, "нервозность", беспокойство',
# 'Приступы повышенной чувствительности к звуку, свету и прикосновению',
# 'Приступы поноса',
# 'Чрезмерное беспокойство о собственном здоровье',
# 'Ощущение усталости, слабости и повышенной истощаемости',
# 'Головные боли или боли в шее',
# 'Трудности засыпания',
# 'беспокойный сон или просыпаетесь среди ночи',
# 'пеожиданные периоды депрессии, возникающие по незначительным поводам или без повода',
# 'перепады настроения и эмоций, которые в основном зависят от того, что происходит вокруг Вас',
# 'повторяющиеся и неотступные представления, мысли, импульсы или образы, которые Вам кажутся тягостными, противными, бессмысленными или отталкивающими',
'повторение одного и того же действия как ритуала, например, повторные перепроверки, перемывание и пересчет при отсутствии в этом действии необходимости'
]

results = ['баллов. Поздравляем! У Вас отсутствует клинически выраженная тревога. Соблюдайте режим дня! Береги себя! Продолжайте поддерживать свой уровень ментального здоровья!',
'Что-то пошло не так. Наш бот определил, что скорее всего у Вас присутствует клинически выраженная тревога. Чтобы получить рекомендации по дальнейшим действиям Вы можете обратиться к своему участковому психотерапевту или психиатру или в проект когнитивно-поведенческой психологии «Без тревоги». Для записи позвоните: +7 985 985-19-18',
'баллов. Упссс! Бот говорит, что откладывать свою тревогу в долгий ящик не получится. Мы очень рекомендуем Вам в ближайшее время сходить на прием к своему лечащему доктору или участковому психотерапевту/ психиатру. Сообщите ему, что по шкале самооценки тревоги SPRA Д. Шихана у Вас обнаружены высокие баллы! Сообщаем, что в современных условиях тревожные расстройства поддаются успешной коррекции. Если Вы не знаете с чего начать обратитесь в наш проект когнитивно-поведенческой психологии «Без тревоги» по тел.: +7 985 985-19-18'
]

# Заготовки для трёх предложений
first = ["Сегодня — идеальный день для новых начинаний.","Оптимальный день для того, чтобы решиться на смелый поступок!","Будьте осторожны, сегодня звёзды могут повлиять на ваше финансовое состояние.","Лучшее время для того, чтобы начать новые отношения или разобраться со старыми.","Плодотворный день для того, чтобы разобраться с накопившимися делами."]
second = ["Но помните, что даже в этом случае нужно не забывать про","Если поедете за город, заранее подумайте про","Те, кто сегодня нацелен выполнить множество дел, должны помнить про","Если у вас упадок сил, обратите внимание на","Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про"]
second_add = ["отношения с друзьями и близкими.","работу и деловые вопросы, которые могут так некстати помешать планам.","себя и своё здоровье, иначе к вечеру возможен полный раздрай.","бытовые вопросы — особенно те, которые вы не доделали вчера.","отдых, чтобы не превратить себя в загнанную лошадь в конце месяца."]
third = ["Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.","Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.","Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы доведите дела до конца.","Не нужно бояться одиноких встреч — сегодня то самое время, когда они значат многое.","Если встретите незнакомца на пути — проявите участие, и тогда эта встреча посулит вам приятные хлопоты."]
# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(content_types=['text'])












def get_text_messages(message):
    # Если написали «Привет»
    if message.text == "/Start":
        # Пишем приветствие
        # bot.send_message(message.from_user.id, "Привет, я - бот психолог")
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_oven = types.InlineKeyboardButton(text='Тест самооценки тревоги SPRA Д. Шихана ', callback_data='test')
        # И добавляем кнопку на экран
        keyboard.add(key_oven)
        key_telec = types.InlineKeyboardButton(text='Открытый чат группы ПОПА ', url="https://t.me/joinchat/EZkYyBvRq8f4A_uzelWPig")
        keyboard.add(key_telec)
        key_bliznecy = types.InlineKeyboardButton(text='Закрытый чат с Денисом и Виталием', callback_data='zodiac')
        keyboard.add(key_bliznecy)
        key_rak = types.InlineKeyboardButton(text='Наш канал YouTube', url="https://www.youtube.com/channel/UC5i4yB4eOdLyA-eXv1Hi5cg?view_as=subscriber")
        keyboard.add(key_rak)
        key_lev = types.InlineKeyboardButton(text='Техники самопомощи ', callback_data='zodiac')
        keyboard.add(key_lev)
        key_deva = types.InlineKeyboardButton(text='Скачать приложение Без тревоги', url="https://example.com")
        keyboard.add(key_deva)
        key_vesy = types.InlineKeyboardButton(text='Записаться на индивидуальную консультацию', callback_data='zodiac')
        keyboard.add(key_vesy)
        key_scorpion = types.InlineKeyboardButton(text='Мы в Инстаграм', callback_data='zodiac')
        keyboard.add(key_scorpion)

        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Привет, я - бот психолог', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


    def get_email(message):  # получаем фамилию
        global email
        name = message.text
        bot.send_message(message.from_user.id, 'Спасибо!')
        bot.register_next_step_handler(message, get_surname)

    def get_surname(message):
        global surname;
        surname = message.text;
        bot.send_message('Продолжаем...');
# Обработчик нажатий на кнопки




@bot.callback_query_handler(func=lambda call: True)
# def get_text_messages:

def callback_worker(call):
    global qs
    global balls
    # Если нажали на одну из 12 кнопок — выводим гороскоп
    if call.data == "zodiac":
        # Формируем гороскоп
        msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_add) + ' ' + random.choice(third)
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)

    if call.data == "test":
        # Готовим кнопки
        keyboard_test = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        net = types.InlineKeyboardButton(text='Нет', callback_data='zero')
        # И добавляем кнопку на экран
        keyboard_test.add(net)
        little = types.InlineKeyboardButton(text='Немного', callback_data='one')
        keyboard_test.add(little)
        umm = types.InlineKeyboardButton(text='Умеренно', callback_data='two')
        keyboard_test.add(umm)
        sil = types.InlineKeyboardButton(text='Сильно', callback_data='three')
        keyboard_test.add(sil)
        ks = types.InlineKeyboardButton(text='Крайне сильно', callback_data='four')
        keyboard_test.add(ks)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(call.from_user.id, text='Как сильно Вы ощущаете ' + symptoms[1].lower(),reply_markup=keyboard_test)

    if call.data == "zero":
        if qs < len(symptoms):
            balls = balls + 0
            qs = qs + 1
            # Готовим кнопки
            keyboard_test = types.InlineKeyboardMarkup()
            # По очереди готовим текст и обработчик для каждого знака зодиака
            net = types.InlineKeyboardButton(text='Нет', callback_data='zero')
            # И добавляем кнопку на экран
            keyboard_test.add(net)
            little = types.InlineKeyboardButton(text='Немного', callback_data='one')
            keyboard_test.add(little)
            umm = types.InlineKeyboardButton(text='Умеренно', callback_data='two')
            keyboard_test.add(umm)
            sil = types.InlineKeyboardButton(text='Сильно', callback_data='three')
            keyboard_test.add(sil)
            ks = types.InlineKeyboardButton(text='Крайне сильно', callback_data='four')
            keyboard_test.add(ks)
            # Показываем все кнопки сразу и пишем сообщение о выборе
            bot.send_message(call.from_user.id, text='Как сильно Вы ощущаете ' + symptoms[qs].lower(),reply_markup=keyboard_test)
        else:
            keyboard_results = types.InlineKeyboardMarkup()
            show_res = types.InlineKeyboardButton(text='Смотреть результаты', callback_data='res')
            keyboard_results.add(show_res)

    if call.data == "one":
        if qs < len(symptoms):
            balls = balls + 1
            qs = qs + 1
            # Готовим кнопки
            keyboard_test = types.InlineKeyboardMarkup()
            # По очереди готовим текст и обработчик для каждого знака зодиака
            net = types.InlineKeyboardButton(text='Нет', callback_data='zero')
            # И добавляем кнопку на экран
            keyboard_test.add(net)
            little = types.InlineKeyboardButton(text='Немного', callback_data='one')
            keyboard_test.add(little)
            umm = types.InlineKeyboardButton(text='Умеренно', callback_data='two')
            keyboard_test.add(umm)
            sil = types.InlineKeyboardButton(text='Сильно', callback_data='three')
            keyboard_test.add(sil)
            ks = types.InlineKeyboardButton(text='Крайне сильно', callback_data='four')
            keyboard_test.add(ks)
            # Показываем все кнопки сразу и пишем сообщение о выборе
            bot.send_message(call.from_user.id, text='Как сильно Вы ощущаете ' + symptoms[qs].lower(),reply_markup=keyboard_test)
        else:
            keyboard_results = types.InlineKeyboardMarkup()
            show_res = types.InlineKeyboardButton(text='Смотреть результаты', callback_data='res')
            keyboard_results.add(show_res)

    if call.data == "res":
        bot.send_message(call.message.chat.id, 'Ваш результат -' + str(balls))

    if call.data == "two":
        if qs < len(symptoms):
            balls = balls + 2
            qs = qs + 1
            # Готовим кнопки
            keyboard_test = types.InlineKeyboardMarkup()
            # По очереди готовим текст и обработчик для каждого знака зодиака
            net = types.InlineKeyboardButton(text='Нет', callback_data='zero')
            # И добавляем кнопку на экран
            keyboard_test.add(net)
            little = types.InlineKeyboardButton(text='Немного', callback_data='one')
            keyboard_test.add(little)
            umm = types.InlineKeyboardButton(text='Умеренно', callback_data='two')
            keyboard_test.add(umm)
            sil = types.InlineKeyboardButton(text='Сильно', callback_data='three')
            keyboard_test.add(sil)
            ks = types.InlineKeyboardButton(text='Крайне сильно', callback_data='four')


            keyboard_test.add(ks)
            # Показываем все кнопки сразу и пишем сообщение о выборе
            bot.send_message(call.from_user.id, text='Как сильно Вы ощущаете ' + symptoms[qs].lower(),reply_markup=keyboard_test)
        else:
            keyboard_results = types.InlineKeyboardMarkup()
            show_res = types.InlineKeyboardButton(text='Смотреть результаты', callback_data='res')
            keyboard_results.add(show_res)


    if call.data == "three":
        if qs < len(symptoms):
            balls = balls + 3
            qs = qs + 1
            # Готовим кнопки
            keyboard_test = types.InlineKeyboardMarkup()
            # По очереди готовим текст и обработчик для каждого знака зодиака
            net = types.InlineKeyboardButton(text='Нет', callback_data='zero')
            # И добавляем кнопку на экран
            keyboard_test.add(net)
            little = types.InlineKeyboardButton(text='Немного', callback_data='one')
            keyboard_test.add(little)
            umm = types.InlineKeyboardButton(text='Умеренно', callback_data='two')
            keyboard_test.add(umm)
            sil = types.InlineKeyboardButton(text='Сильно', callback_data='three')
            keyboard_test.add(sil)
            ks = types.InlineKeyboardButton(text='Крайне сильно', callback_data='four')
            keyboard_test.add(ks)
            # Показываем все кнопки сразу и пишем сообщение о выборе
            bot.send_message(call.from_user.id, text='Как сильно Вы ощущаете ' + symptoms[qs].lower(),reply_markup=keyboard_test)
        else:
            bot.send_message(call.message.chat.id, 'Ваш результат -' + str(balls))
            # keyboard_results = types.InlineKeyboardMarkup()
            # show_res = types.InlineKeyboardButton(text='Смотреть результаты', callback_data='res')
            # keyboard_results.add(show_res)


    if call.data == "four":
        global email
        email = message.text
        bot.send_message(message.message.chat.id, 'Ваш результат -' + str(balls) + 'Баллов \n Напишите Ваш email и я пришлю подробную расшифровку!')
        # bot.send_message(call.message.chat.id, 'Ваш результат -' + str(balls) + 'номер вопроса' + str(qs) +'словарь' + str(len(symptoms)-1))
        # if qs == len(symptoms):
        #     global email
        #     email = call.text
        #     bot.send_message(call.message.chat.id, 'Ваш результат -' + str(balls) +'Баллов \n Напишите Ваш email и я пришлю подробную расшифровку!')
        #     # bot.register_next_step_handler(message, get_surname)

        if qs < len(symptoms):
            balls = balls + 4
            qs = qs + 1
            # Готовим кнопки
            keyboard_test = types.InlineKeyboardMarkup()
            # По очереди готовим текст и обработчик для каждого знака зодиака
            net = types.InlineKeyboardButton(text='Нет', callback_data='zero')
            # И добавляем кнопку на экран
            keyboard_test.add(net)
            little = types.InlineKeyboardButton(text='Немного', callback_data='one')
            keyboard_test.add(little)
            umm = types.InlineKeyboardButton(text='Умеренно', callback_data='two')
            keyboard_test.add(umm)
            sil = types.InlineKeyboardButton(text='Сильно', callback_data='three')
            keyboard_test.add(sil)
            ks = types.InlineKeyboardButton(text='Крайне сильно', callback_data='four')
            keyboard_test.add(ks)
            # Показываем все кнопки сразу и пишем сообщение о выборе
            bot.send_message(call.from_user.id, text='Как сильно Вы ощущаете ' + symptoms[qs].lower(),reply_markup=keyboard_test)




            # keyboard_results = types.InlineKeyboardMarkup()
            # show_res = types.InlineKeyboardButton(text='Смотреть результаты', callback_data='res')
            # keyboard_results.add(show_res)


# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)


