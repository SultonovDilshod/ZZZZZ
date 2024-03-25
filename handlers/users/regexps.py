from aiogram import types
from aiogram.dispatcher import filters

from loader import dp

EMAIL_REGEX = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
PHONE_NUM = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
PASSWORD = r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'
USER_NAME = r'^[a-z0-9_-]{3,15}$'
DATE = r'(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})'
COMMAND_EMAIL_REGEX = r"/email:" + EMAIL_REGEX


@dp.message_handler(filters.Regexp(EMAIL_REGEX))
async def regexp_email(msg: types.Message):
    await msg.answer('Email qabul qilindi')


@dp.message_handler(filters.Regexp(PHONE_NUM))
async def regexp_phone(msg: types.Message):
    await msg.answer('Telefon raqam qabul qilindi')


@dp.message_handler(regexp_commands=[COMMAND_EMAIL_REGEX])
async def command_regexp_example(msg: types.Message):
    await msg.answer('Email qabul qilindi')
