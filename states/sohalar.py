from aiogram.dispatcher.filters.state import StatesGroup, State


class Sohalar(StatesGroup):
    chose_soha = State()
    doctors = State()
    litsenziya = State()
