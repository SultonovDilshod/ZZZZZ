from aiogram import types
from loader import dp



@dp.message_handler(state="/result")
async def start_get_result(message: types.Message):
    await message.answer("iltimos natijalarni qabul qilib oling")
