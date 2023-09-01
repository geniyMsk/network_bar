# -*- coding: utf-8 -*-
import logging
import datetime
from aiogram import Dispatcher
from aiogram.types import BotCommand, BotCommandScope, BotCommandScopeChat

from config import ADMINS
from loader import bot



async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            pass
        except Exception as err:
            logging.error(err)

