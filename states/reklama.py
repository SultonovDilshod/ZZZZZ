from aiogram.dispatcher.filters.state import StatesGroup, State


class Reklama(StatesGroup):
    reklama_kiritish = State()
    tasdiqlsh = State()

