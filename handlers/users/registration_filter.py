from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from loader import dp
from aiogram.dispatcher import filters
import re
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.keyboards import yes_no

from states.personal_data import PersonalData

# FOR DATABSE
import sqlite3
from loader import db, dp, bot
from data.config import ADMINS

EMAIL_REGEX = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
PHONE_NUM = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
PASSWORD = r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'


def start_reg():
    @dp.message_handler(filters.Text(contains="ro'yxatdan o'tish", ignore_case=True))
    async def start_register(message: types.Message):
        await message.answer("Bizning klinikamizning ro'yxatdan o'tish qismiga xush kelibsiz",
                             reply_markup=ReplyKeyboardRemove())
        await message.answer("Iltimos To'liq ism sharifingizni kiriting: ", reply_markup=bekor_qilish)
        await PersonalData.fullname.set()


start_reg()


@dp.message_handler(state=PersonalData.fullname)
async def answer_fullname(message: types.Message, state: FSMContext):
    if message.text.lower() == "❌ bekor qilish":
        await state.finish()
        await message.answer("Bosh sahifa", reply_markup=main_menu_btn)
    else:
        fullname = message.text
        await state.update_data(
            {"fullname": fullname}
        )

        await message.answer("Iltimos email addresingizni kiriting: ", reply_markup=bekor_qilish)
        # await PersonalData.next()
        await PersonalData.email.set()


def check_email():
    @dp.message_handler(state=PersonalData.email)
    async def answer_email(message: types.Message, state: FSMContext):
        if message.text.lower() == "❌ bekor qilish":
            await state.finish()
            await message.answer("Bosh sahifa", reply_markup=main_menu_btn)
        else:
            email = message.text
            match = re.search(EMAIL_REGEX, email)

            if match:
                await state.update_data(
                    {"email": email}
                )
                await message.answer("Telefon nomeringizni kiriting: ", reply_markup=bekor_qilish)
                await PersonalData.phone_number.set()
                # await PersonalData.next()
            else:
                check_email()
                await message.answer("Iltimos email addresingizni qaytadan kiriting! ", reply_markup=bekor_qilish)
                await PersonalData.email.set()


check_email()


def check_phone():
    @dp.message_handler(state=PersonalData.phone_number)
    async def answer_phone(message: types.Message, state: FSMContext):
        if message.text.lower() == "❌ bekor qilish":
            await state.finish()
            await message.answer("Bosh sahifa", reply_markup=main_menu_btn)
        else:
            number = message.text
            match = re.search(PHONE_NUM, number)

            if match:
                await state.update_data(
                    {"phone_number": number}
                )
                await message.answer("✅✅✅\n\nTabriklaymiz siz muvaffaqiyatli ro'yxatdan o'tdingiz",
                                     reply_markup=bekor_qilish)
                await message.answer('Tasdiqlaysizmi?', reply_markup=yes_no)
                await PersonalData.id_number.set()



            else:
                check_phone()
                await message.answer("Iltimos telefon nomeringizni qaytadan kiriting: ")
                await PersonalData.phone_number.set()


check_phone()


@dp.message_handler(state=PersonalData.id_number)
async def answer_okay(message: types.Message, state: FSMContext):
    if message.text.lower() == 'ha':
        username = message.from_user.full_name
        tm_id = message.from_user.id
        given_id = (int(tm_id) + 2525625)*7

        await state.update_data(
            {"ID_number": given_id}
        )

        data = await state.get_data()
        name = data.get('fullname')
        email = data.get('email')
        phone_num = data.get('phone_number')
        id_user = data.get('ID_number')

        try:
            db.add_user(id=message.from_user.id, full_name=name, username=username, telegram_id=tm_id, email_db=email,
                        tel_num=phone_num, given_id=given_id)

            count = db.count_users()[0]
            sms = f"✅✅✅\n{name} ro'yxatdan o'tdi.\n Bazada {count} ta foydalanuvchi bor"
            await bot.send_message(chat_id=ADMINS[0], text=sms)

            await message.answer(f"🟢🟢🟢\n\nYour ID:\n {given_id}\n\n⚠️⚠️⚠️ ID raqamingizni unutmang, "
                                 "chunki ushbu ID orali shifokor qabuliga yozilishingiz va shifokor ko'rigi"
                                 "natijalarini olishingiz mumkin")
            await message.answer(f"Tabriklayman! \nSiz muvaffaqqiyatli ro'yxatdan o'tdingiz\n\n"
                                 f"1️⃣ FIO: {name}\n"
                                 f"2️⃣ Email: {email}\n"
                                 f"3️⃣ Tel: {phone_num}\n"
                                 f"4️⃣ ID: {id_user}", reply_markup=main_menu_btn)
            await state.finish()

        except sqlite3.IntegrityError as err:
            await message.answer("‼️‼️‼️\n\nKechirasiz siz avval ro'yxatdan o'tgansiz", reply_markup=main_menu_btn)
            await state.finish()

            await bot.send_message(chat_id=ADMINS, text=err)


    else:
        await message.answer("Afsusdaman. Sizning so'rovingiz rad etildi\nQaytadan ro'yxatdan o'ting",
                             reply_markup=main_menu_btn)
        await state.finish()
