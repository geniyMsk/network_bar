import telebot
from telebot import types
import random
from random import randint
from aiogram.types import ReplyKeyboardRemove,\
    ReplyKeyboardMarkup, KeyboardButton,\
    InlineKeyboardMarkup, InlineKeyboardButton, InputFile

import codecs
import webbrowser
import time
global nw
nw = time.time_ns()

rat = open('/root/GFG.html', 'w')

def user_open():
    file = open('/root/myusers', 'r+')
    d = {}
    for elem in file.readlines():
        a = elem.split()
        d[a[0]] = int(a[1])
    file.close()
    return d


def names_open():
    f = open('/root/mynames', 'r+')
    d = dict()
    for elem in f.readlines():
        a = elem.split()
        d[a[0]] = a[1]
    f.close()
    return d

def add_user(userlist):
    open('/root/myusers', 'w').close()
    f = open('/root/myusers', 'r+')
    for key in userlist.keys():
        f.write(str(key) + " " + str(userlist[key]) + "\n")
    f.close()

def add_name(namelist):
    open('/root/mynames', 'w').close()
    f = open('/root/mynames', 'r+')
    for key in namelist.keys():
        f.write(str(key) + " " + str(namelist[key]) + "\n")
    f.close()

users = user_open()
names = names_open()

def rating_sort(names):
    global users
    open('/root/GFG.html', 'w').close()
    f = open('/root/GFG.html', 'w')
    s = ''
    sorted_dict = {}
    sorted_keys = sorted(users, key=users.get, reverse=True)
    for i in sorted_keys:
        s += str(names[i]) + " " + str(users[i]) + "<br>"
    html_template = """
        <html>
        <head></head>
        <meta charset="utf-8">
        <body>
        <h1>Rating RUege_bot </h1>
        <p> <big>""" + s + """ <big></p>

        </body>
        </html>
        """

    f.write(html_template)
    f.close()
    file = codecs.open("GFG.html", 'r', "utf-8")
    print(file.read())

import os

bot = telebot.TeleBot('')

class word(object):
    def __init__(self, test, ans):
        self.test = test
        self.ans = ans

CHART = dict()

def prepri_open():
    f = open('/root/dict.txt', 'r+', encoding="utf8")
    d = []
    for elem in f.readlines():
        test = elem[:-2:]
        ans = elem[-2]
        d.append(word(test, ans))
        print(test, ans)
    f.close()
    return d

def suffix_open():
    f = open('/root/dict2.txt', 'r+', encoding="utf8")
    d = []
    for elem in f.readlines():
        test = elem[:-2:]
        ans = elem[-2]
        d.append(word(test, ans))
        print(test, ans)
    f.close()
    return d

def korni_open():
    f = open('/root/dict3.txt', 'r+', encoding="utf8")
    d = []
    for elem in f.readlines():
        test = elem[:-2:]
        ans = elem[-2]
        d.append(word(test, ans))
        print(test, ans)
    f.close()
    return d

def ship_open():
    f = open('/root/dict4.txt', 'r+', encoding="utf8")
    d = []
    for elem in f.readlines():
        test = elem[:-2:]
        ans = elem[-2]
        d.append(word(test, ans))
        print(test, ans)
    f.close()
    return d

def mix_open():
    f = open('/root/dict5.txt', 'r+', encoding="utf8")
    d = []
    for elem in f.readlines():
        test = elem[:-2:]
        ans = elem[-2]
        d.append(word(test, ans))
        print(test, ans)
    f.close()
    return d

def add_word(c, w):
    f = open('/root/dict.txt', 'r+', encoding="utf8")
    f.seek(0, os.SEEK_END)
    f.write(c + " " + w + "\n")
    f.close()


prepri_dict = prepri_open()
suffix_dict = suffix_open()
korni_dict = korni_open()
ship_dict = ship_open()
mix_dict = mix_open()
wait_list = dict()
type = dict()
@bot.message_handler(commands=["chart"])
def chart(m, res=False):
    bot.send_message(m.chat.id, 'Ваш счёт: ' + str(CHART.get(m.chat.id, 0)))

@bot.message_handler(commands=["start"])
def start(m, res=False):
    global users
    if m.chat.id not in users:
        users[m.chat.id] = 0
        add_user(users)
        names[m.chat.id] = m.chat.id
        add_name(names)
    bot.send_message(m.chat.id, "Меню /start\nПре-/При- /prepri\nСчёт /chart\nГласная в корнях /korni\nСуффиксы /suffix\nО/Е после шипящих /ship\nЖесть /mix\nРейтинг /rating\nСбросить очки /reset\nСменить имя /rename")

@bot.message_handler(commands=["prepri"])
def prepri(m, res=False):
    global users
    if m.chat.id not in users:
        users[m.chat.id] = 0
        add_user(users)
        names[m.chat.id] = m.chat.id
        add_name(names)
        # кнопки
    t = prepri_dict[randint(0, len(prepri_dict) - 1)]
    wait_list[m.chat.id] = t
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    type[m.chat.id] = 1
    #button_a = types.KeyboardButton("А")
    #button_o = types.KeyboardButton("О")
    button_e = types.KeyboardButton("Е")
    button_i = types.KeyboardButton("И")
    #button_u = types.KeyboardButton("У")
    #button_yu = types.KeyboardButton("Ю")
    #button_ya = types.KeyboardButton("Я")
    kb.row(button_i, button_e)
    bot.send_message(m.chat.id, '❓Выберите правильное написание: ' + t.test,  reply_markup=kb)

@bot.message_handler(commands=["suffix"])
def suffix(m, res=False):
    global users
    if m.chat.id not in users:
        users[m.chat.id] = 0
        add_user(users)
        names[m.chat.id] = m.chat.id
        add_name(names)
    # кнопки
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    t = suffix_dict[randint(0, len(suffix_dict) - 1)]
    wait_list[m.chat.id] = t
    type[m.chat.id] = 2
    button_a = types.KeyboardButton("А")
    button_o = types.KeyboardButton("О")
    button_e = types.KeyboardButton("Е")
    button_i = types.KeyboardButton("И")
    button_u = types.KeyboardButton("У")
    button_yu = types.KeyboardButton("Ю")
    button_ya = types.KeyboardButton("Я")
    button_yy = types.KeyboardButton("Ы")
    kb.row(button_a, button_e, button_i, button_o, button_yy, button_u, button_yu, button_ya)
    #random.shuffle(kb)
    bot.send_message(m.chat.id, '❓Выберите правильное написание: ' + t.test,  reply_markup=kb)

@bot.message_handler(commands=["korni"])
def korni(m, res=False):
    global users
    if m.chat.id not in users:
        users[m.chat.id] = 0
        add_user(users)
        names[m.chat.id] = m.chat.id
        add_name(names)
    # кнопки
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    t = korni_dict[randint(0, len(korni_dict) - 1)]
    wait_list[m.chat.id] = t
    type[m.chat.id] = 4
    button_a = types.KeyboardButton("А")
    button_o = types.KeyboardButton("О")
    button_e = types.KeyboardButton("Е")
    button_i = types.KeyboardButton("И")
    button_u = types.KeyboardButton("У")
    button_yu = types.KeyboardButton("Ю")
    button_ya = types.KeyboardButton("Я")

    button_yy = types.KeyboardButton("Ы")
    kb.row(button_a, button_e, button_i, button_o, button_yy, button_u, button_yu, button_ya)
    #random.shuffle(kb)
    bot.send_message(m.chat.id, '❓Выберите правильное написание: ' + t.test,  reply_markup=kb)

@bot.message_handler(commands=["ship"])
def ship(m, res=False):
    global users
    if m.chat.id not in users:
        users[m.chat.id] = 0
        add_user(users)
        names[m.chat.id] = m.chat.id
        add_name(names)
    # кнопки
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    t = ship_dict[randint(0, len(ship_dict) - 1)]
    wait_list[m.chat.id] = t
    type[m.chat.id] = 5
    button_o = types.KeyboardButton("О")
    button_e = types.KeyboardButton("Е")
    button_yo = types.KeyboardButton("Ё")
    kb.row(button_e, button_o, button_yo)
    bot.send_message(m.chat.id, '❓Выберите правильное написание: ' + t.test,  reply_markup=kb)

@bot.message_handler(commands=["mix"])
def mix(m, res=False):
    global users
    if m.chat.id not in users:
        users[m.chat.id] = 0
        add_user(users)
        names[m.chat.id] = m.chat.id
        add_name(names)
    # кнопки
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    t = mix_dict[randint(0, len(mix_dict) - 1)]
    wait_list[m.chat.id] = t
    type[m.chat.id] = 6
    button_a = types.KeyboardButton("А")
    button_o = types.KeyboardButton("О")
    button_e = types.KeyboardButton("Е")
    button_i = types.KeyboardButton("И")
    button_u = types.KeyboardButton("У")
    button_yu = types.KeyboardButton("Ю")
    button_ya = types.KeyboardButton("Я")

    button_yy = types.KeyboardButton("Ы")
    kb.row(button_a, button_e, button_i, button_o, button_yy, button_u, button_yu, button_ya)
    #random.shuffle(kb)
    bot.send_message(m.chat.id, '❓Выберите правильное написание: ' + t.test,  reply_markup=kb)

@bot.message_handler(commands = ["rating"])
def rating(m):
    global users
    if m.chat.id not in users:
        users[m.chat.id] = 0
        add_user(users)
        names[m.chat.id] = m.chat.id
        add_name(names)
    rating_sort(names)
    f = open("/root/GFG.html", 'rb')
    bot.send_document(m.chat.id,f,"C:\mybot\GFG.html")
    start(m)

@bot.message_handler(commands = ["rename"])
def rename(m):
    global users
    if m.chat.id not in users:
        users[m.chat.id] = 0
        add_user(users)
        names[m.chat.id] = m.chat.id
        add_name(names)
    type[m.chat.id] = 3
    wait_list[m.chat.id] = 1
    bot.send_message(m.chat.id, 'Введите новое имя:')

@bot.message_handler(commands = ["R8gMn76T4tthjdMGTCnkYFTVNjxT495KY25c5KWB"])
def sbros(m):
    return

@bot.message_handler(commands = ["reset"])
def reset(m):
    global users
    if m.chat.id not in users:
        users[m.chat.id] = 0
        add_user(users)
    users[m.chat.id] = 0
    CHART[m.chat.id] = 0
    add_user(users)
    bot.send_message(m.chat.id, 'Ваш рейтинг сброшен')

cnt = 0

@bot.message_handler(content_types=["text"])
def checker(message):
    global users
    global cnt
    cnt += 1
    if cnt == 50:
        add_user(users)
        cnt = 0
    if message.chat.id in wait_list:
        if type[message.chat.id] == 3:
            names[message.chat.id] = message.text[:50]
            add_name(names)
            bot.send_message(message.chat.id, 'Новое имя установлено: ' + message.text)
            return
    if message.chat.id in wait_list:
        print(message.text.strip(), wait_list[message.chat.id], message.text.strip() == wait_list[message.chat.id].ans)
        if message.text.strip() == wait_list[message.chat.id].ans:
            CHART[message.chat.id] = CHART.get(message.chat.id, 0) + 1
            users[message.chat.id] = users.get(message.chat.id, 0) + 1
            bot.send_message(message.chat.id, "✅Верно")
        else:
            CHART[message.chat.id] = CHART.get(message.chat.id, 0) - 3
            users[message.chat.id] = users.get(message.chat.id, 0) - 3
            bot.send_message(message.chat.id, "❌Ошибка, правильно: " + wait_list[message.chat.id].test.replace("_", wait_list[message.chat.id].ans))
        if type[message.chat.id] == 1:
            prepri(message)
        if type[message.chat.id] == 2:
            suffix(message)
        if type[message.chat.id] == 4:
            korni(message)
        if type[message.chat.id] == 5:
            ship(message)
        if type[message.chat.id] == 6:
            mix(message)
    else:
        start(message)




bot.polling(none_stop=True)

bot.polling(none_stop=True, interval=0)
