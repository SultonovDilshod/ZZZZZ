import time

from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from data.config import ADMINS
from loader import dp, bot, db
from states.reklama import Reklama
from keyboards.default.keyboards import reklama_tasdiqlash, start_btn, language_option
from states.TMC_natija import TestNatija
from states.clean_base import Clean
from aiogram.dispatcher import FSMContext




























Reklama_text = []
User_ids = []


@dp.message_handler(text='/allusers_list', user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    result = ""
    for i in users:
        result += f"👤 --- TMC ID: {i[6]}\n" \
                  f"♦️ F.I.O: {i[1]}\n" \
                  f"♦️ Pochta mazil: {i[4]}\n" \
                  f"♦️ Tel nomeri: {i[5]}\n"
    print(result)
    await message.answer(result)


@dp.message_handler(text='/allusers_info', user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    for i in users:
        res = f"👤 --- TMC ID: {i[6]}\n" \
              f"📍 F.I.O: {i[1]}\n" \
              f"📍 Telegram name: {i[2]}\n" \
              f"📍 Pochta mazil: {i[4]}\n" \
              f"📍 Tel nomeri: {i[5]}\n" \
              f"📍 Telegram ID: {i[0]}\n\n"
        print(res)
        await message.answer(res)


# _____________________________________________________________________________________________________________________

#                                           TEST RESULT

@dp.message_handler(text='/result_test', user_id=ADMINS)
async def send_result(message: types.Message):
    await message.answer("👤  Hurmatli shifokor,\nQabulingizdagi bemorning ID raqamini kiriting:\n👇🏻👇🏻👇🏻")
    await TestNatija.ask_user.set()


@dp.message_handler(state=TestNatija.ask_user, user_id=ADMINS)
async def send_result(message: types.Message):
    try:
        id_code = message.text
        users = db.select_user(given_id=id_code)
        if users:
            User_ids.append(users[0])
            await message.answer("⚠️")
            await message.answer("Tasdiqlaysizmi?", reply_markup=reklama_tasdiqlash)
            await TestNatija.confirm_natija.set()
        else:
            await message.answer("❌ Bunday foydalanuvchi bazada mavjud emas", reply_markup=ReplyKeyboardRemove())
            await TestNatija.ask_user.set()

    except:
        await message.answer("❌ ID raqam kiritdingiz\nIltimos qaytadan kiriting",
                             reply_markup=ReplyKeyboardRemove())
        await TestNatija.ask_user.set()


@dp.message_handler(state=TestNatija.confirm_natija, user_id=ADMINS)
async def send_result(message: types.Message, state: FSMContext):
    if message.text == '✅ Ha':
        await message.answer("✅✅✅\nFayl yoki hujjatni yuboring", reply_markup=ReplyKeyboardRemove())
        await TestNatija.file_send.set()

    elif message.text == "❌ Yo'q":
        await message.answer("Siz bosh sahifaga qaytdingiz:", reply_markup=main_menu_btn)
        await state.finish()


@dp.message_handler(state=TestNatija.file_send, user_id=ADMINS)
async def send_result(message: types.Message, state: FSMContext):
    await message.forward(chat_id=User_ids[-1], disable_notification=False)
    await message.answer("EGASIGA YETDI")                           # SHIFOKOR TEXT YUBORILDI, FILE BO"LIB QOLSACHI

    await message.answer("✅ ", reply_markup=main_menu_btn)
    await state.finish()


# _____________________________________________________________________________________________________________________


#                                           REKLAMA

@dp.message_handler(text='/reklama', user_id=6093689347)
async def ask_adds(message: types.Message):
    await message.reply("O'rtoq boshliq\n\nReklamangizni kiriting:\n👇🏻👇🏻👇🏻")
    await Reklama.reklama_kiritish.set()


@dp.message_handler(state=Reklama.reklama_kiritish, user_id=6093689347)
async def res_adds(message: types.Message):
    ali = message.text                                          # RASIM BO"LIB QOLSACHI, KEYIN LISTGA QO"SHISH KERAK
    Reklama_text.append(ali)
    await message.answer("⚠️")
    await message.answer("Haqiqatdan ham ushbu reklamani tasdiqlaysizmi!?", reply_markup=reklama_tasdiqlash)
    await Reklama.tasdiqlsh.set()


@dp.message_handler(state=Reklama.tasdiqlsh)
async def send_adds(message: types.Message, state: FSMContext):
    if message.text == '✅ Ha':
        await message.answer("✅")
        await message.answer("Adds send successfully", reply_markup=main_menu_btn)
        users = db.select_all_users()
        for user in users:
            user_id = user[0]
            await bot.send_message(chat_id=user_id, text=Reklama_text[-1])
            time.sleep(1)
        await state.finish()
    elif message.text == "❌ Yo'q":
        await message.answer("Reklamangizni qaytadan tahrir qiling:", reply_markup=start_btn)
        await state.finish()


# _____________________________________________________________________________________________________________________

#                                            CLEAR BASE

@dp.message_handler(text='/clean_db', user_id=6093689347)
async def delete_all_users(message: types.Message, state: FSMContext):
    await message.answer("⚠️")
    await message.answer("Haqiqatdan ham <b>BAZA</b> ni tozalamoqchimisiz?", reply_markup=reklama_tasdiqlash)
    await Clean.confirm_clean.set()


@dp.message_handler(state=Clean.confirm_clean, user_id=6093689347)
async def delete_all_users(message: types.Message, state: FSMContext):
    if message.text == '✅ Ha':
        db.delete_users()
        await message.answer("✅✅✅\nBAZA tozalandi", reply_markup=main_menu_btn)
        await state.finish()

    elif message.text == "❌ Yo'q":
        await message.answer("Siz bosh sahifaga qaytdingiz:", reply_markup=main_menu_btn)
        await state.finish()
