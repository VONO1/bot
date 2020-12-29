# import pymorphy2
# #
# #
# # butyavka = morph.parse('бутявка')[0]
# # print(butyavka.make_agree_with_number(1).word)
# # # 'бутявка'
# # print(butyavka.make_agree_with_number(2).word)
# # # 'бутявки'
# # print(butyavka.make_agree_with_number(5).word)
# # # 'бутявок'
import telebot
import requests
# client = telebot.TeleBot('1457884681:AAF9GjlOLP7hlhlqimmIMm5heybKXv-Ig28')
#
#
# api_token = '1457884681:AAF9GjlOLP7hlhlqimmIMm5heybKXv-Ig28'
#
# requests.get('https://api.telegram.org/bot{}/sendMessage'.format(api_token), params=dict(chat_id='@Vitalii_super_bot',text='666Hello world!'))
#
# client.polling(none_stop = True, interval = 0)


import smtplib
smtpObj = smtplib.SMTP('smtp.yandex.ru', 587)
smtpObj.starttls()
smtpObj.login('feedback@Cbtlab.ru','3@BXZWJ4')
smtpObj.sendmail('feedback@Cbtlab.ru','mr.vono@gmail.com','hui!')