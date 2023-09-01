# -*- coding: utf8 -*-


import logging

import aiogram
from aiogram import executor

from utils import on_startup_notify
from loader import dp
import handlers
from aiogram.types import ParseMode, BotCommand, BotCommandScopeChat
from config import ADMINS
from loader import bot




async def on_startup(dispatcher):

    await on_startup_notify(dispatcher)




log_file = 'logs.log'
f = open(log_file, 'a')
f.write('-------------------------\n')
f.close()

file_log = logging.FileHandler(log_file)
console_out = logging.StreamHandler()
logging.basicConfig(handlers=(file_log, console_out),
                    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)



if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)