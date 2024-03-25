from aiogram.dispatcher.filters.state import StatesGroup, State

class PersonalData(StatesGroup):
    fullname = State()
    email = State()
    phone_number = State()
    id_number = State()
