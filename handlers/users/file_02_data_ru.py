from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.utils.markdown import hide_link
from loader import dp
from aiogram.dispatcher import filters
import re
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove, CallbackQuery
from keyboards.default.keyboards import yes_no, bekor_qilish_rus, main_menu_btn_ru, language_option, post_nomi_avto_rus
from keyboards.default.keyboards import post_nomi_avto_temiryul_rus, orqaga_qaytish_rus
from keyboards.inline.rus_inline import Tumanlar_26010_rus, Tumanlar_26002_rus, Tumanlar_26003_rus, Tumanlar_26004_rus

from states.personal_data import PersonalData
from states.rus_lan import RUS_lan
from states.start_zero import Start_zero

import sqlite3
from loader import db, dp, bot
from data.config import ADMINS


@dp.message_handler(text='/start', state=Start_zero.start_zero)
@dp.message_handler(text='/start',state=RUS_lan.rus)
@dp.message_handler(text='/start',state=RUS_lan.rus_tuman)
@dp.message_handler(text='/start',state=RUS_lan.rus_post)
@dp.message_handler(text='/start',state=RUS_lan.rus_sklad)
@dp.message_handler(filters.Text(contains="мена языка", ignore_case=True), state=RUS_lan.rus)
async def send_result(message: types.Message):
    await message.answer("🏚 Сиз бош саҳифага қайтдингиз\nВы вернулись на главную страницу\n👇🏻👇🏻👇🏻",
                         reply_markup=language_option)
    await Start_zero.start_zero.set()

@dp.message_handler(filters.Text(contains="русский", ignore_case=True), state=Start_zero.start_zero)
@dp.message_handler(filters.Text(contains="отмена", ignore_case=True), state=RUS_lan.rus)
async def start_register(message: types.Message):
    name = message.from_user.full_name

    await message.answer(
"📣Через данный бот вы можете ознакомиться с информациями об <b>открытых и свободных таможенных складах.</b>\nВключая:\n"
"📤Наименование склада\n👨‍⚖️Заведущий склада\n☎️Тел.номер\n⏰Часы работы\n📍Адрес\n💰Цены на услуги и другие\n\n"
"‼️ Бот предоставляет информацию только о складах при <b>Ташкентском городском таможенном управлении!</b>")
    await message.answer(f"Выберите вид транспорта", reply_markup=main_menu_btn_ru)

    await RUS_lan.rus.set()


@dp.message_handler(filters.Text(contains="авто", ignore_case=True), state=RUS_lan.rus)
@dp.message_handler(filters.Text(contains="авто", ignore_case=True), state=RUS_lan.rus_post)
async def start_register(message: types.Message):



    if message.text.lower() == "🚚 авто":
        await message.answer(f"Вы выбрали АВТО", reply_markup=bekor_qilish_rus)
        await message.answer(f"Пожалуйста, выберите таможенный пост", reply_markup=post_nomi_avto_rus)
        await RUS_lan.rus_post.set()
    elif message.text.lower() == "🚉 avto-temiryo'l":
        await message.answer(f"Вы выбрали АВТО-ЖД", reply_markup=bekor_qilish_rus)
        await message.answer(f"Пожалуйста, выберите таможенный пост", reply_markup=post_nomi_avto_temiryul_rus)
        await RUS_lan.rus_post.set()

    else:
        await message.answer("❌❌❌\nВы ввели неправильное значение. Пожалуйста, обновите снова с помощью кнопки /start")
        RUS_lan.rus.set()




@dp.message_handler(filters.Text(contains="260", ignore_case=True), state=RUS_lan.rus_post)
@dp.message_handler(filters.Text(contains="260", ignore_case=True), state=RUS_lan.rus_sklad)
async def start_register(message: types.Message):
    if message.text == '26002 - «Ташкент-товарный» ВЭД':
        await message.answer(f"Вы выбрали таможенный пост ВЭД «Ташкент-товарный»", reply_markup=orqaga_qaytish_rus)
        await message.answer(f"Пожалуйста, выберите название округа", reply_markup=Tumanlar_26002_rus)
        await RUS_lan.rus_sklad.set()

    elif message.text == "26003 - «Аркбулак» ВЭД":
        await message.answer(f"Вы выбрали таможенный пост ВЭД «Аркбулак»", reply_markup=orqaga_qaytish_rus)
        await message.answer(f"Пожалуйста, выберите название округа", reply_markup=Tumanlar_26003_rus)
        await RUS_lan.rus_sklad.set()

    elif message.text == '26004 - «Чукурсай» ВЭД':
        await message.answer(f"Вы выбрали таможенный пост ВЭД «Чукурсай»", reply_markup=orqaga_qaytish_rus)
        await message.answer(f"Пожалуйста, выберите название округа", reply_markup=Tumanlar_26004_rus)
        await RUS_lan.rus_sklad.set()

    elif message.text == "26010 - «Сергели» ВЭД":
        await message.answer(f"Вы выбрали таможенный пост ВЭД «Сергели»", reply_markup=orqaga_qaytish_rus)
        await message.answer(f"Пожалуйста, выберите название округа", reply_markup=Tumanlar_26010_rus)
        await RUS_lan.rus_sklad.set()

    else:
        pass


@dp.message_handler(filters.Text(contains="назад", ignore_case=True), state=RUS_lan.rus_post)
async def start_register(message: types.Message):
    if message.text == "⬅️ Назад":
        await message.answer(f"Пожалуйста, выберите вид транспорта", reply_markup=main_menu_btn_ru)
        await RUS_lan.rus.set()

    else:
        pass


@dp.message_handler(filters.Text(contains="назад", ignore_case=True), state=RUS_lan.rus_sklad)
async def start_register(message: types.Message):
    if message.text == "⬅️ Назад":
        await message.answer(f"Пожалуйста, выберите вид транспорта", reply_markup=main_menu_btn_ru)
        await RUS_lan.rus.set()

    else:
        pass


# “Toshkent-tovar” TIF bojxona posti
# 26002
#
# “Ark buloq” TIF bojxona posti
# 26003
#
# “Chuqursoy” TIF bojxona posti
# 26004
#
# “Sirg‘ali” TIF bojxona posti
# 26010


from aiogram.utils.markdown import hide_link


@dp.callback_query_handler(text="Бектемирский район", state=RUS_lan.rus_sklad)
async def start_shifokor(call: CallbackQuery):
    await call.message.answer(hide_link("https://telegra.ph/OOO-Coca-Cola-Ichimligi-Uzbekistan-LTD-03-24"))
    await call.message.answer("📍Адрес таможенного склада: 100005, г.Ташкент, Яшнободский район, ул. Фергана Йули, дом 13/11\n👇👇👇")
    await call.message.answer_location(latitude=41.296201, longitude=69.298287)



#
# from aiogram.filters import Command
# from aiogram.types import FSInputFile, Message
# from aiogram.utils.media_group import MediaGroupBuilder
#
# @dp.callback_query_handler(text="Бектемирский район", state=RUS_lan.rus_sklad)
# async def cmd_album(call: CallbackQuery):
#     album_builder = MediaGroupBuilder(
#         caption='📥<b>Nomi:</b> OOO "Coca-Cola Ichimligi Uzbekistan LTD"\n'
#                 '📗<b>Ombor turi:</b> Ochiq\n'
#                 '🛃<b>Bojxona posti xududida joylashgan:</b> Xa!\n'
#                 "📌<b>Ombor tavsifi:<b>"
#                 "\n    ✅ Quruq ombor;\n    ✅ Forkliftlar;\n    ✅ Ko'p yillik ish tajribasi;\n    ✅ 24/7 video kuzatuv\n"
#                 '🔰<b>Xizmatlar doirasi:</b>'
#                 '\n    ✅ Tovarlarni “bojxona ombori” va “vaqtinchalik saqlash” rejimlarida saqlash;'
#                 '\n    ✅ Tovarlarni bojxona omborida saqlash;'
#                 '\n    ✅ Yuklash va tushirish operatsiyalari.\n'
#                 '🌀kv.m\n'
#                 '🔅<b>Yopiq maydon (m.kub):</b> 3600.00\n'
#                 '🔷 🔷 🔷 🔷 🔷\n'
#                 '👨‍💼<b>Ombor mudiri:</b> Даулетов Ринат Шавкатович'
#                 '☎️<b>Tel.raqamlari:</b> 90 175-73-13; 99 883-58-11;78 140-06-96'
#                 '⏰<b>Ish vaqti:</b> Du-Sh    9:00 - 18:00'
#                 "💰<b>Xizmatlar narxi:</b> kuniga bir tonna uchun 3000 so'mdan (batafsil preyskurantda) ___________"
#                 '📍<b>Bojxona ombori manzili:</b> 100005, г.Ташкент, Яшнободский район, ул. Фергана Йули, дом 13/11'
#     )
#     album_builder.add(
#         type="photo",
#         media=FSInputFile("image_from_pc.jpg")
#         # caption="Подпись к конкретному медиа"
#
#     )
#     # Если мы сразу знаем тип, то вместо общего add
#     # можно сразу вызывать add_<тип>
#     album_builder.add_photo(
#         # Для ссылок или file_id достаточно сразу указать значение
#         media="https://picsum.photos/seed/groosha/400/300"
#     )
#     album_builder.add_photo(
#         media="<ваш file_id>"
#     )
#     await message.answer_media_group(
#         # Не забудьте вызвать build()
#         media=album_builder.build()
#     )
