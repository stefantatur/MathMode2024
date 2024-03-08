from datetime import datetime
from time import sleep
import requests
from bs4 import BeautifulSoup as BS


def print_message(message):
    t = message['time']
    dt = datetime.fromtimestamp(t)
    print(dt.strftime('%Y-%m-%d %H:%M:%S'), message['name'])
    print(message['text'])


def help():
    print(
        ' В графе Ваше имя: введите имя. \n В графе сообщение: пропишите текст и нажмите enter для отправки письма.\n Server\n Основной файл где прописаны roots для сайта. Служит основой для работы с сервером,заносит сообщения в базу данных,сохраняет их.\n Receiver \n Осуществляет связь между server и sender. Обрабатывает сообщения и несет в себе основные функции.\n Sender \n Осуществляет отправку сообщений. Выводит сообщения.')



def weather():
    url = 'https://yandex.com.am/weather/?lat=55.75581741&lon=37.61764526'
    response = requests.get(url)
    bs = BS(response.text, "lxml")
    temp = bs.find('span', 'temp__value temp__value_with-unit')
    wt = bs.find('div', 'link__condition day-anchor i-bem')
    print(temp.text, wt.text)


after = 0
while True:
    response = requests.get('http://127.0.0.1:5000/messages', params={'after': after})
    messages = response.json()['messages']

    for message in messages:
        print_message(message)
        if '/help' in message['text']:
            help()
        print(" ")
        if '/weather' in message['text']:
            weather()
        print(" ")

    after = message['time']
    sleep(1)




