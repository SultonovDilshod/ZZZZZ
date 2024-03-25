from aiogram.dispatcher.filters.state import StatesGroup, State


class TestNatija(StatesGroup):
    ask_user = State()
    confirm_natija = State()
    file_send = State()

