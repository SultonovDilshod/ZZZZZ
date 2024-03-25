from aiogram import types
from loader import dp
from aiogram.dispatcher import filters
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove, CallbackQuery
from keyboards.default.keyboards import devide_soha, ocherad_fields, yes_no_for_qabul
from keyboards.inline.fields_for_get_data import Yozilish
from states.och_sohalar import OchSohalar
from keyboards.default.keyboards import yozilish_btn
from aiogram.dispatcher import FSMContext


@dp.message_handler(filters.Text(contains="Shifokor qabuli", ignore_case=True))
async def start_soha(message: types.Message):
    await message.answer("Bizning klinikada qaysi bo'lim qabuliga yozilmoqchisiz?",
                         reply_markup=yozilish_btn)
    await OchSohalar.level_one.set()


@dp.message_handler(state=OchSohalar.level_one)
async def start_mutaxassislik(message: types.Message, state: FSMContext):
    if message.text.lower() == "📝 qabulga yozilish":
        await message.answer(
            "ℹ️ Qabulga yozilmoqchi bo'lgan yo'nalishni va shifokorni tanlang\n\n👇🏻👇🏻👇🏻",
            reply_markup=ocherad_fields)
        await OchSohalar.level_two.set()
    elif message.text.lower() == "⬅️ ortga qaytish":
        await message.answer("Bosh sahifaga qaytdingiz", reply_markup=main_menu_btn)
        await state.finish()
    elif message.text == "📥 Natijani olish":
        await message.answer("Iltimos ID raqamingizni kiriting:", reply_markup=ReplyKeyboardRemove())
        await OchSohalar.level_four.set()
    else:
        await state.finish()


@dp.message_handler(state=OchSohalar.level_two)
async def shifokor_qabuli(message: types.Message, state: FSMContext):
    list = ["👼🏻 Pediatr", "🦠 Immunolog", '🧠 Nevropatolog', "🦻🏻 Lor", '🧬 Genikolog', "🩺 Terapevt",
            '🙇🏻‍♂️ Massajist', "💉 Endokrinolog", '🍤 Gastroenterolog']
    if message.text in list:
        txt_send = "✅ <b>Klinika TMC</b>\n\n" \
                   "<b>🔹 Mutaxassisligi: </b>Pediatr\n" \
                   "<b>🔹 Lavozimi: </b>Bosh shifokor\n" \
                   "<b>🔹 Ish tajribasi: </b>6 yil\n" \
                   "<b>🔹 Bog'lanish: </b>loreminput@gmail.com\n" \
                   "\n\n⁉️⁉️⁉️\n  Siz haqiqatdan ham ushbu shifokor qabuliga yozilmoqchimisiz?"
        await message.answer_photo(photo='https://telegra.ph/Doctor-moster-dishko-07-25', caption=txt_send,
                                   reply_markup=yes_no_for_qabul)
        await OchSohalar.level_two.set()
    elif message.text == "⬅️ Ortga qaytish":
        await message.answer("Qabul bo'lmiga qaytdingiz", reply_markup=yozilish_btn)
        await OchSohalar.level_one.set()
    elif message.text == "✅ Ha":
        await message.answer("✅✅✅\n\nIltimos telegram bot tomonidan sizga berilgan ID raqamni kiriting:",
                             reply_markup=ReplyKeyboardRemove())
        await OchSohalar.level_three.set()
    elif message.text == "❌ Yo'q":
        await message.answer("❌ Boshqa shifokor qabuliga yozilishingiz mumkin", reply_markup=ocherad_fields)
        await OchSohalar.level_two.set()
    else:
        await state.finish()


@dp.message_handler(state=OchSohalar.level_three)
async def start_soha(message: types.Message,  state: FSMContext):
    try:
        if int(message.text) == ((int(message.from_user.id) + 2525625) * 7):
            await message.answer("✅✅✅ Tabriklaymiz!\n\nSizning qabulingiz muvaffaqiyatli amalga oshirildi\n\n"
                                 "Tez orada sizning qabul vaqtingiz e'lon qilinadi", reply_markup=yozilish_btn)
            await OchSohalar.level_one.set()
        elif message.text == "/start":
            await message.answer("Bosh sahifa", reply_markup=main_menu_btn)
            await state.finish()
        else:
            await message.reply("❌❌❌   Xatolik\n\n❎ ID raqamingizni noto'g'ri.\n Iltimos qaytadan kiriting yoki"
                                " /start orqali bot menyusini yangilang ", reply_markup=ReplyKeyboardRemove())
            await OchSohalar.level_three.set()

    except:
        if message.text == "/start":
            await message.answer("Bosh sahifa", reply_markup=main_menu_btn)
            await state.finish()
        else:
            await message.reply("❌❌❌   Xatolik\n\n❎ ID raqamingizni noto'g'ri.\n Iltimos qaytadan kiriting yoki"
                                " /start orqali bot menyusini yangilang ", reply_markup=ReplyKeyboardRemove())
            await OchSohalar.level_three.set()


@dp.message_handler(state=OchSohalar.level_four)
async def start_soha(message: types.Message,  state: FSMContext):
    try:
        if int(message.text) == ((int(message.from_user.id) + 2525625) * 7):
            await message.answer("✅✅✅ Tabriklaymiz!\n\nAvvalambor bizning <b>Klinika TMC</b> "
                                 "xizmatidan foydalanganingiz uchun juda katta rahmat\n\n Sizning natijalaringiz\n\n👇🏻👇🏻👇🏻",
                                 reply_markup=yozilish_btn)
            await OchSohalar.level_one.set()
        elif message.text == "/start":
            await message.answer("Bosh sahifa", reply_markup=main_menu_btn)
            await state.finish()
        else:
            await message.reply("❌❌❌   Xatolik\n\n❎ ID raqamingizni noto'g'ri.\n Iltimos qaytadan kiriting yoki"
                                " /start orqali bot menyusini yangilang ", reply_markup=ReplyKeyboardRemove())
            await OchSohalar.level_four.set()

    except:
        if message.text == "/start":
            await message.answer("Bosh sahifa", reply_markup=main_menu_btn)
            await state.finish()
        else:
            await message.reply("❌❌❌   Xatolik\n\n❎ ID raqamingizni noto'g'ri.\n Iltimos qaytadan kiriting yoki"
                                " /start orqali bot menyusini yangilang ", reply_markup=ReplyKeyboardRemove())
            await OchSohalar.level_four.set()
