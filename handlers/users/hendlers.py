from aiogram import types
from aiogram.dispatcher import filters
from keyboards.default.keyboards import main_menu_btn_uz, yozilish_btn

from loader import dp


# TEXT handlers
@dp.message_handler(filters.Text(contains='assalomu alaykum', ignore_case=True))
@dp.message_handler(filters.Text(contains='salom', ignore_case=True))
@dp.message_handler(filters.Text(contains='qalay', ignore_case=True))
async def emoji_handler(message: types.Message):
    await message.answer(
        f"Assalomu ayaykum, hurmatli mijoz {message.from_user.full_name}!", reply_markup=main_menu_btn)


@dp.message_handler(filters.Text(contains='rahmat', ignore_case=True))
async def emoji_handler(message: types.Message):
    await message.answer(
        f"Sizga xizmat ko'rsatishdan mamnunmiz, hurmatli {message.from_user.full_name}! 🤗🤗🤗",
        reply_markup=main_menu_btn)


@dp.message_handler(filters.Text(contains='iflos', ignore_case=True))
@dp.message_handler(filters.Text(contains='nas', ignore_case=True))
@dp.message_handler(filters.Text(contains='pes', ignore_case=True))
@dp.message_handler(filters.Text(contains='xarom', ignore_case=True))
@dp.message_handler(filters.Text(contains='lanat', ignore_case=True))
@dp.message_handler(filters.Text(contains='pashol', ignore_case=True))
@dp.message_handler(filters.Text(contains='gaday', ignore_case=True))
@dp.message_handler(filters.Text(contains='onangni', ignore_case=True))
@dp.message_handler(filters.Text(contains='ska', ignore_case=True))
async def emoji_handler(message: types.Message):
    await message.answer(
        f"So'kinish odob yuzasiga to'g'ri kelmaydi, hurmatli {message.from_user.full_name}! 🙂🙂🙂",
        reply_markup=main_menu_btn)


# FILE< IMAGE< VOICE HANDLERS

@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photo_handler(msg: types.Message):
    await msg.answer("Agar bu rasim hujjat bo'lsa, iltimos unga izoh yozib qoldiring", reply_markup=main_menu_btn)


@dp.message_handler(content_types=types.ContentTypes.STICKER)
# @dp.message_handler(content_types=types.ContentTypes.STICKER)
async def emoji_handler(msg: types.Message):
    await msg.answer('😀', reply_markup=main_menu_btn)


@dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
async def emoji_handler(msg: types.Message):
    await msg.answer('Bu qaysi turdagi hujjat ekanligini izohga yozib qoldiring', reply_markup=main_menu_btn)


@dp.message_handler(content_types='contact')
# @dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def contact_handler(msg: types.Message):
    await msg.answer('Kim bu?', reply_markup=main_menu_btn)


@dp.message_handler(content_types=types.ContentTypes.VOICE)
async def audio_handler(msg: types.Message):
    await msg.answer(
        'Hurmatli foydalanuvchi, siz bizga ovozli xabar qoldirdingiz.'
        'Bu bot bu turdagi xabarlarni qayta tahrirlash imkoniyati mavjud emas'
        'Iltimos bu turdagi malumot yubormang', reply_markup=main_menu_btn)


# BOSHQA HANDLERLAR

# IsReplyFilter
@dp.message_handler(is_reply=True, commands='user_id')
async def reply_filter_example(msg: types.Message):
    await msg.answer(msg.reply_to_message.from_user.id, reply_markup=main_menu_btn)


# IsSenderContact
@dp.message_handler(content_types='contact', is_sender_contact=True)
# @dp.message_handler(filters.IsSenderContact(True), content_types='contact')
async def sender_contact_example(msg: types.Message):
    await msg.answer('Rahmat, kontaktingiz qabul qilindi!', reply_markup=main_menu_btn)


# ForwardedMessageFilter
@dp.message_handler(is_forwarded=True)
async def forwarded_example(msg: types.Message):
    await msg.answer('Birovning xabarini menga yuborayapsizmi?', reply_markup=main_menu_btn)


# ChatTypeFilter
# @dp.message_handler(chat_type='private', commands='is_pm')
@dp.message_handler(filters.ChatTypeFilter(types.ChatType.PRIVATE), commands='shaxsiy')
async def chat_type_example(msg: types.Message):
    await msg.answer('Bu shaxsiy chat', reply_markup=main_menu_btn)
