from aiogram.dispatcher.filters.state import State, StatesGroup


class state(StatesGroup):
    ZERO = State()
    RENAME =State()

class reg(StatesGroup):
    NAME = State()
    PROF = State()
    COMPANY = State()
    PHONE = State()
    CHOOSE_SPEAKER = State()
    CHOOSE_THEME = State()
    CHOOSE_DATE = State()
    CHOOSE_SLOT = State()

    CONFIRM = State()

