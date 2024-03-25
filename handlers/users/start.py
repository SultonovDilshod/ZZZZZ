from aiogram import types
from aiogram.dispatcher import FSMContext
import sqlite3
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters import Command, Text
from keyboards.default.keyboards import language_option
from states.och_sohalar import OchSohalar
from states.start_zero import Start_zero

from loader import db, dp, bot
from data.config import ADMINS


@dp.message_handler(text='/start')
# @dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name

    count = db.count_users()[0]
    sms = f"✅✅✅\n{name} /start тугмасини босди.\n Базада {count} та фойдаланувчи бор"
    for admin in ADMINS:
        await bot.send_message(chat_id=admin, text=sms)

    await message.answer(
        f"🤖 Ассалому алайкум ҳурматли {name}!\n🚩 Ботдан фойдаланишни бошлаш учун аввал ўзингизга қулай тилни танланг 👇\n➖➖➖\n"
        f"🤖 Здравствуйте, уважаемый {name}!\n🚩 Перед тем как начать пользоваться ботом, выберите удобный для вас язык 👇")


    await message.answer("Илтимос тилни танланг / Пожалуйста, выберите язык", reply_markup=language_option)

    await Start_zero.start_zero.set()
