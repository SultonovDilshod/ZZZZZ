from aiogram.dispatcher.filters.state import StatesGroup, State


class Clean(StatesGroup):
    confirm_clean = State()

