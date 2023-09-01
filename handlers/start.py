# -*- coding: utf-8 -*-
import codecs
import datetime
import json
import logging
from asyncio import sleep

import aiogram.types
from aiogram.dispatcher import FSMContext

from loader import bot, dp
from config import ADMINS
from aiogram import types
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, \
    InlineQueryResultArticle, InputMessageContent, ContentType, File, ReplyKeyboardRemove, WebAppInfo
from dir.keyboards import keyboards
import dir.DBCommands as db

import dir.states as states
from loader import scheduler

kb = keyboards()

speakers = [
    'Анастасия Федорова, директор по продуктам вертикалей Недвижимость, Авто, Услуги, Работа',
    'Виталий Туманов, директор по продукту для частных пользователей',
    'Андрей Рыбинцев, директор по данным',
    'Андрей Тарасов, дизайн-директор',
    'Александр Капустин, директор финтех-продуктов'
]

themes = [
    [
        'Запуск новых бизнес-моделей в зрелых продуктах',
        'Построение сильной продуктовой команды, принципы организации команд',
        'Необходимые качества для профессионального роста менеджеру команды'
    ],
    [
        'Как построить тесную работу продукта с другими функциями и бизнесом',
        'Как простроить product-led organization',
        'Пользовательский рост через продукт'
    ],
    [
        'ML powered продукты',
        'Антифрод в продуктах',
        'Зачем продакт-менеджеру изучать ML и AI',
        'Как работать из кальянной (бонус!)'
    ],
    [
        'Как обновлять очень большие продукты',
        'Как делать дизайн супераппа',
        'Брендинг в продукте',
        'Какой дизайнер вам нужен'
    ],
    [
        'Финтех: как это делать',
        'Продуктовые страдания: как найти идею и вырастить команду',
        'Customer success подход к построению продуктов'
    ]
]

slots = ['12.00-12.20', '12.30-12.50', '13.00-13.20', '13.30-13.50', '14.00-14.20', '14.30-14.50', '15.00-15.20',
         '15.30-15.50', '16.00-16.20', '16.30-16.50', '17.00-17.20', '17.30-17.50', '10.00-10.20', '10.30-10.50',
         '11.00-11.20', '11.30-11.50']
slots_speakers = [
    [6, 7, 8, 9, 10, 11],
    [6, 7, 8, 9, 10, 11],
    [6, 7, 8, 9, 10, 11],
    [0, 1, 2, 3, 4, 5],
    [12, 13, 14, 15, 0, 1]
]

group_id = -982049044
@dp.message_handler(commands='start', state='*')
async def start(message: Message):
    chat_ids = db.get_all_chat_id()
    chat_id = message.from_user.id

    if (chat_id,) not in chat_ids:
        username = message.from_user.username
        db.add_user(chat_id, username)

    state_conf = db.get_state_conf(chat_id)
    # if state_conf == False:


    await message.answer_chat_action('upload_document')
    await message.answer_document(document=open("Politika_konfidencial'nosti_internet_sajta_1.pdf", 'rb'))
    await message.answer_chat_action('upload_document')
    await message.answer_document(document=open('Согласие.pdf', 'rb'),
                                  caption='Продолжая пользоваться чат-ботом, ты подтверждаешь, что согласен на обработку персональных данных и ознакомлен с Политикой конфиденциальности',
                                  reply_markup=kb.agree)
    db.set_state_conf(chat_id)


@dp.callback_query_handler(text='agree')
async def reg1(call: CallbackQuery):
    chat_id = call.from_user.id

    await bot.send_message(chat_id=chat_id, text='Давай знакомиться)\n'
                                                 'Напиши имя и фамилию👇')
    await states.reg.NAME.set()


@dp.message_handler(state=states.reg.NAME)
async def reg2(message: Message):
    chat_id = message.from_user.id
    name = message.text
    if len(name) <= 1:
        return
    db.set_name(chat_id, name)
    await message.answer('Расскажи, кем ты работаешь?')
    await states.reg.PROF.set()


@dp.message_handler(state=states.reg.PROF)
async def reg3(message: Message):
    chat_id = message.from_user.id
    prof = message.text

    db.set_prof(chat_id, prof)
    await message.answer('В какой компании? 😌')
    await states.reg.COMPANY.set()


@dp.message_handler(state=states.reg.COMPANY)
async def reg4(message: Message):
    chat_id = message.from_user.id
    company = message.text

    db.set_company(chat_id, company)
    await message.answer('Напиши номер телефона.\n'
                         'Он может понадобиться для оперативной связи 🙌🏻', reply_markup=kb.phone)
    await states.reg.PHONE.set()


@dp.message_handler(state=states.reg.PHONE)
async def reg5(message: Message):
    chat_id = message.from_user.id
    phone = message.text


    db.set_phone(chat_id, phone)

    text = 'Ура, почти всё!\n' \
           'Выбери, с кем хочешь встретиться 😌\n\n' \
           '– Анастасия Федорова, директор по продуктам вертикалей Недвижимость, Авто, Услуги, Работа\n' \
           '– Виталий Туманов, директор по продукту для частных пользователей\n' \
           '– Андрей Рыбинцев, директор по данным\n' \
           '– Андрей Тарасов, дизайн-директор\n' \
           '– Александр Капустин, директор финтех-продуктов\n'
    await message.answer(text, reply_markup=kb.speakers)
    await states.reg.CHOOSE_SPEAKER.set()



@dp.message_handler(state=states.reg.PHONE, content_types=types.ContentType.CONTACT)
async def reg5_1(message: Message):
    chat_id = message.from_user.id
    phone = message.contact.phone_number

    db.set_phone(chat_id, phone)
    text = 'Ура, почти всё!\n' \
           'Выбери, с кем хочешь встретиться 😌\n\n' \
           '1. Анастасия Федорова, директор по продуктам вертикалей Недвижимость, Авто, Услуги, Работа\n' \
           '2. Виталий Туманов, директор по продукту для частных пользователей\n' \
           '3. Андрей Рыбинцев, директор по данным\n' \
           '4. Андрей Тарасов, дизайн-директор\n' \
           '5. Александр Капустин, директор финтех-продуктов\n'
    await message.answer(text, reply_markup=kb.speakers)
    await states.reg.CHOOSE_SPEAKER.set()


@dp.callback_query_handler(lambda c: c.data[:7] == 'speaker', state=states.reg.CHOOSE_SPEAKER)
async def choose_speaker(call: CallbackQuery):
    chat_id = call.from_user.id
    message_id = call.message.message_id

    speaker_id = int(call.data[7:])
    text = f'{speakers[speaker_id - 1]}\n\n' \
           'Темы:'
    i = 1
    keyboard = InlineKeyboardMarkup()
    for el in themes[speaker_id - 1]:
        text += f'\n{i}. {el}'
        keyboard.add(InlineKeyboardButton(f'Тема {i}', callback_data=f'theme_{i}_sp_{speaker_id}'))
        i += 1
    keyboard.add(InlineKeyboardButton('Назад', callback_data='back'))

    await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=keyboard)
    await states.reg.CHOOSE_THEME.set()


@dp.callback_query_handler(text='back', state=states.reg.CHOOSE_THEME)
async def choose_speaker(call: CallbackQuery):
    chat_id = call.from_user.id
    message_id = call.message.message_id

    text = 'Ура, почти всё!\n' \
           'Выбери, с кем хочешь встретиться 😌\n\n' \
           '1. Анастасия Федорова, директор по продуктам вертикалей Недвижимость, Авто, Услуги, Работа\n' \
           '2. Виталий Туманов, директор по продукту для частных пользователей\n' \
           '3. Андрей Рыбинцев, директор по данным\n' \
           '4. Андрей Тарасов, дизайн-директор\n' \
           '5. Александр Капустин, директор финтех-продуктов\n'
    await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=kb.speakers)
    await states.reg.CHOOSE_SPEAKER.set()


@dp.callback_query_handler(lambda c: c.data[:5] == 'theme', state=states.reg.CHOOSE_THEME)
async def choose_speaker(call: CallbackQuery):
    chat_id = call.from_user.id
    message_id = call.message.message_id

    theme_id = call.data[6]
    speaker_id = call.data[11]
    keyboard = InlineKeyboardMarkup()
    if int(speaker_id) <= 3:
        keyboard.add(InlineKeyboardButton('4 сентября', callback_data=f'date_{speaker_id}_{theme_id}_1'))
        keyboard.add(InlineKeyboardButton('5 сентября', callback_data=f'date_{speaker_id}_{theme_id}_2'))
    elif int(speaker_id) == 4:
        keyboard.add(InlineKeyboardButton('4 сентября', callback_data=f'date_{speaker_id}_{theme_id}_1'))
    elif int(speaker_id) == 5:
        keyboard.add(InlineKeyboardButton('5 сентября', callback_data=f'date_{speaker_id}_{theme_id}_2'))

    keyboard.add(InlineKeyboardButton('Назад', callback_data=f'back_{speaker_id}'))

    await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='Выбери дату 👇',
                                reply_markup=keyboard)
    await states.reg.CHOOSE_DATE.set()


@dp.callback_query_handler(lambda c: c.data[:4] == 'back', state=states.reg.CHOOSE_DATE)
async def choose_speaker(call: CallbackQuery):
    chat_id = call.from_user.id
    message_id = call.message.message_id

    speaker_id = int(call.data[5])

    text = f'{speakers[speaker_id - 1]}\n\n' \
           'Темы:'
    i = 1
    keyboard = InlineKeyboardMarkup()
    for el in themes[speaker_id - 1]:
        text += f'\n{i}. {el}'
        keyboard.add(InlineKeyboardButton(f'Тема {i}', callback_data=f'theme_{i}_sp_{speaker_id}'))
        i += 1
    keyboard.add(InlineKeyboardButton('Назад', callback_data='back'))

    await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=keyboard)
    await states.reg.CHOOSE_THEME.set()


@dp.callback_query_handler(lambda c: c.data[:4] == 'date', state=states.reg.CHOOSE_DATE)
async def choose_speaker(call: CallbackQuery):
    chat_id = call.from_user.id
    message_id = call.message.message_id

    theme_id = int(call.data[7])
    speaker_id = int(call.data[5])
    date = call.data[-1]

    res = []
    for el in slots_speakers[speaker_id-1]:

        if db.get_slot_status(speaker_id, el, date) == None:
            res.append(InlineKeyboardButton(text=slots[el], callback_data=f'slot_{speaker_id}_{theme_id}_{date}_{el}'))

    keyboard = InlineKeyboardMarkup(row_width=3)
    l=len(res)
    if l==6:
        keyboard.add(res[0], res[1], res[2], res[3], res[4], res[5])
    elif l==5:
        keyboard.add(res[0], res[1], res[2], res[3], res[4])
    elif l==4:
        keyboard.add(res[0], res[1], res[2], res[3])
    elif l==3:
        keyboard.add(res[0], res[1], res[2])
    elif l==2:
        keyboard.add(res[0], res[1])
    elif l==1:
        keyboard.add(res[0])
    keyboard.add(InlineKeyboardButton(text='Назад', callback_data=f'back_{speaker_id}_{theme_id}'))

    await bot.edit_message_text(message_id=message_id, chat_id=chat_id, text='Выбери слот для встречи👇',
                                reply_markup=keyboard)
    await states.reg.CHOOSE_SLOT.set()


@dp.callback_query_handler(lambda c: c.data[:4] == 'back', state=states.reg.CHOOSE_SLOT)
async def choose_speaker(call: CallbackQuery):
    chat_id = call.from_user.id
    message_id = call.message.message_id


    theme_id = int(call.data[7])
    speaker_id = int(call.data[5])

    keyboard = InlineKeyboardMarkup()
    if int(speaker_id) <= 3:
        keyboard.add(InlineKeyboardButton('4 сентября', callback_data=f'date_{speaker_id}_{theme_id}_1'))
        keyboard.add(InlineKeyboardButton('5 сентября', callback_data=f'date_{speaker_id}_{theme_id}_2'))
    elif int(speaker_id) == 4:
        keyboard.add(InlineKeyboardButton('4 сентября', callback_data=f'date_{speaker_id}_{theme_id}_1'))
    elif int(speaker_id) == 5:
        keyboard.add(InlineKeyboardButton('5 сентября', callback_data=f'date_{speaker_id}_{theme_id}_2'))

    keyboard.add(InlineKeyboardButton('Назад', callback_data=f'back_{speaker_id}'))

    await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='Выбери дату 👇',
                                reply_markup=keyboard)
    await states.reg.CHOOSE_DATE.set()



@dp.callback_query_handler(lambda c: c.data[:4] == 'slot', state=states.reg.CHOOSE_SLOT)
async def choose_speaker(call: CallbackQuery):
    chat_id = call.from_user.id
    message_id = call.message.message_id

    theme_id = int(call.data[7])
    speaker_id = int(call.data[5])
    date = call.data[9]
    slot_id = int(call.data[11:])
    if date == '1':
        data = '4 сентября'
    else:
        data = '5 сентября'
    text = f'Проверь выбор слота:\n' \
           f'– {speakers[speaker_id-1]}\n' \
           f'– {themes[speaker_id-1][theme_id-1]}\n' \
           f'– {data}\n' \
           f'– {slots[slot_id]}'


    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton('Верно', callback_data=f'conf_{speaker_id}_{theme_id}_{date}_{slot_id}'))
    keyboard.add(InlineKeyboardButton('Неверно', callback_data=f'back_{speaker_id}_{theme_id}_{date}_{slot_id}'))
    await bot.edit_message_text(message_id=message_id, chat_id=chat_id, text=text, reply_markup=keyboard)

    await states.reg.CONFIRM.set()

@dp.callback_query_handler(lambda c: c.data[:4] == 'back', state=states.reg.CONFIRM)
async def choose_speaker(call: CallbackQuery):
    chat_id = call.from_user.id
    message_id = call.message.message_id

    theme_id = int(call.data[7])
    speaker_id = int(call.data[5])
    date = call.data[9]


    res = []
    for el in slots_speakers[speaker_id - 1]:

        if db.get_slot_status(speaker_id, el, date) == None:
            res.append(InlineKeyboardButton(text=slots[el], callback_data=f'slot_{speaker_id}_{theme_id}_{date}_{el}'))

    keyboard = InlineKeyboardMarkup(row_width=3)
    l = len(res)
    if l == 6:
        keyboard.add(res[0], res[1], res[2], res[3], res[4], res[5])
    elif l == 5:
        keyboard.add(res[0], res[1], res[2], res[3], res[4])
    elif l == 4:
        keyboard.add(res[0], res[1], res[2], res[3])
    elif l == 3:
        keyboard.add(res[0], res[1], res[2])
    elif l == 2:
        keyboard.add(res[0], res[1])
    elif l == 1:
        keyboard.add(res[0])
    keyboard.add(InlineKeyboardButton(text='Назад', callback_data=f'back_{speaker_id}_{theme_id}'))

    await bot.edit_message_text(message_id=message_id, chat_id=chat_id, text='Выбери слот для встречи👇',
                                reply_markup=keyboard)
    await states.reg.CHOOSE_SLOT.set()



@dp.callback_query_handler(lambda c: c.data[:4] == 'conf', state=states.reg.CONFIRM)
async def choose_speaker(call: CallbackQuery):
    chat_id = call.from_user.id
    message_id = call.message.message_id

    theme_id = int(call.data[7])
    speaker_id = int(call.data[5])
    date = call.data[9]
    slot_id = int(call.data[11:])

    user = db.get_user(chat_id)
    name = user.name
    phone = user.phone
    company = user.company
    prof = user.prof



    id = db.add_approve(chat_id, speaker_id, theme_id, int(date), slot_id)
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton('Принять', callback_data=f'appr_{id}'))
    keyboard.add(InlineKeyboardButton('Отклонить', callback_data=f'disa_{id}'))

    if date == '1':
        data = '4 сентября'
    else:
        data = '5 сентября'

    text = f'Заявка №{id}\n' \
           f'Имя: {name}\n' \
           f'Телефон: {phone}\n' \
           f'Компания: {company}\n' \
           f'Должность: {prof}\n' \
           f'Спикер: {speakers[speaker_id-1]}\n' \
           f'Тема: {themes[speaker_id-1][theme_id-1]}\n' \
           f'Дата: {data}\n' \
           f'Время: {slots[slot_id]}'

    await bot.send_message(group_id, text, reply_markup=keyboard)

    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=None)
    await bot.send_message(chat_id, 'Спасибо, дождись подтверждения 😉', reply_markup=kb.menu)
    # text = 'Выбери, с кем хочешь встретиться 😌\n\n' \
    #        '1. Анастасия Федорова, директор по продуктам вертикалей Недвижимость\n' \
    #        '2. Виталий Туманов, директор по продукту для частных пользователей\n' \
    #        '3. Андрей Рыбинцев, директор по данным\n' \
    #        '4. Андрей Тарасов, дизайн-директор\n' \
    #        '5. Александр Капустин, директор финтех-продуктов\n'
    # await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=kb.speakers)


@dp.message_handler(text='👈 В главное меню', state='*')
async def menu(message: Message):
    text = 'Выбери, с кем хочешь встретиться 😌\n\n' \
           '1. Анастасия Федорова, Директор по продуктам вертикалей Недвижимость, Авто, Услуги, Работа\n' \
           '2. Виталий Туманов, директор по продукту для частных пользователей\n' \
           '3. Андрей Рыбинцев, директор по данным\n' \
           '4. Андрей Тарасов, дизайн-директор\n' \
           '5. Александр Капустин, директор финтех-продуктов\n'
    await message.answer(text=text, reply_markup=kb.speakers)
    await states.reg.CHOOSE_SPEAKER.set()


@dp.message_handler(text='🗓 Мои слоты', state='*')
async def menu(message: Message):
    chat_id = message.from_user.id

    approves = db.get_approve_by_chat_id(chat_id)
    i=0
    for approve in approves:

        approve_id = approve.id
        speaker_id = approve.speaker_id
        theme_id = approve.theme_id
        date = approve.date
        slot_id = approve.slot_id
        if date == '1':
            data = '4 сентября'
        else:
            data = '5 сентября'

        text = f'Слот {i}\n ' \
               f'{themes[speaker_id-1][theme_id-1]}\n' \
               f'{speakers[speaker_id-1]}\n' \
               f'{data}\n' \
               f'{slots[slot_id]}'

        keyboard = InlineKeyboardMarkup()
        keyboard.add(InlineKeyboardButton('Отменить', callback_data=f'stop_{approve_id}'))
        await bot.send_message(chat_id, text, reply_markup=keyboard)


        i+=1

@dp.callback_query_handler(lambda c: c.data[:4] == 'stop', state='*')
async def delete(call: CallbackQuery):
    chat_id = call.from_user.id
    message_id = call.message.message_id


    approve_id = call.data[5:]
    db.del_approve(approve_id)

    await bot.edit_message_reply_markup(chat_id, message_id, reply_markup=None)
    await call.answer('Слот отменен')



@dp.callback_query_handler(chat_id=group_id, state='*')
async def choose_speaker(call: CallbackQuery):

    message_id = call.message.message_id


    approve_id = call.data[5:]
    status = call.data[:4]

    approve = db.get_approve(approve_id)
    if approve == []:
        await bot.edit_message_reply_markup(chat_id=group_id, message_id=message_id, reply_markup=None)
        return

    chat_id = approve.chat_id
    speaker_id = approve.speaker_id
    theme_id = approve.theme_id
    date = approve.date
    slot_id = approve.slot_id




    if status=='appr':
        db.set_approve_status(approve_id, True)

        slot_status = db.get_slot_status(speaker_id, slot_id, date)
        if slot_status==(True, ):
            await call.answer('Слот уже занят')
            return
        await bot.send_message(chat_id, 'Записали! 🙌🏻\n'
                                        'Приходи в Нетворк-бар за 10 минут до начала встречи — как раз успеешь выбрать подходящий напиток 😉')
        await bot.edit_message_reply_markup(chat_id=group_id, message_id=message_id, reply_markup=None)
        db.add_slot(speaker_id, date, slot_id)
        async def push():
            await bot.send_message(chat_id, 'Встреча с продуктовым директором Авито состоится через 10 минут!\n'
                                            'Ждём тебя 😎')

        slot = slots[slot_id]

        hour = int(slot[0:2])
        mins = int(slot[3:5])

        run_date = datetime.datetime(2023, 9, int(date)+3, hour, mins)- datetime.timedelta(minutes=10)
        x = scheduler.add_job(push, 'date', run_date=run_date)
        print(x)


    elif status=='disa':
        db.set_approve_status(approve_id, False)


        await bot.send_message(chat_id, 'К сожалению, слот не подтвержден 😔')
        await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=None)