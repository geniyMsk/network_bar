from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

class keyboards():

    agree = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("Подтвердить", callback_data='agree')

            ]
        ]
    )

    phone = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton('Отправить номер телефона', request_contact=True)
            ]
        ], one_time_keyboard=True, resize_keyboard=True
    )

    speakers = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("1",
                                     callback_data='speaker1')
            ],
            [
                InlineKeyboardButton("2",
                                     callback_data='speaker2')
            ],
            [
                InlineKeyboardButton("3",
                                     callback_data='speaker3')
            ],
            [
                InlineKeyboardButton("4",
                                     callback_data='speaker4')
            ],
            [
                InlineKeyboardButton("5",
                                     callback_data='speaker5')
            ],
        ]
    )

    menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton('👈 В главное меню')
            ],
            [
                KeyboardButton('🗓 Мои слоты')
            ]
        ], resize_keyboard=True
    )

