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
from keyboards.default.keyboards import yes_no, main_menu_btn_uz, bekor_qilish_uzb, language_option, post_nomi_avto_uzb
from keyboards.default.keyboards import post_nomi_avto_temiryul_uzb, orqaga_qaytish_uzb
from keyboards.inline.uzb_inline import Tumanlar_26002_uzb_avto, Tumanlar_26003_uzb_avto, Tumanlar_26004_uzb_avto, Tumanlar_26010_uzb_avto
from keyboards.inline.uzb_inline import Tumanlar_26002_uzb_jd, Tumanlar_26003_uzb_jd, Tumanlar_26004_uzb_jd, Tumanlar_26010_uzb_jd
from keyboards.inline.uzb_inline import uz_yukli_ombor_uzb, avto_26002_bektemir, avto_26002_yashnabod, avto_26002_yakkasaroy, avto_26002_shayxontohur
from keyboards.inline.uzb_inline import avto_26003_yakkasaroy, avto_26003_chilonzor, avto_26003_sergeli, avto_26003_yangiyul, avto_26003_zangiota

from states.personal_data import PersonalData
from states.uzb_lan import UZB_lan
from states.start_zero import Start_zero

import sqlite3
from loader import db, dp, bot
from data.config import ADMINS


@dp.message_handler(text='/start', state=Start_zero.start_zero)
@dp.message_handler(text='/start', state=UZB_lan.uzb)
@dp.message_handler(text='/start', state=UZB_lan.uzb_post_avto)
@dp.message_handler(text='/start', state=UZB_lan.uzb_post_jd)
@dp.message_handler(text='/start', state=UZB_lan.uzb_sklad_avto_26002)
@dp.message_handler(text='/start', state=UZB_lan.uzb_sklad_jd_26002)
@dp.message_handler(text='/start', state=UZB_lan.uzb_tuman_avto_26002)
@dp.message_handler(text='/start', state=UZB_lan.uzb_tuman_jd_26002)
@dp.message_handler(text='/start', state=UZB_lan.uzb_sklad_avto_26003)
@dp.message_handler(text='/start', state=UZB_lan.uzb_sklad_jd_26003)
@dp.message_handler(text='/start', state=UZB_lan.uzb_tuman_avto_26003)
@dp.message_handler(text='/start', state=UZB_lan.uzb_tuman_jd_26003)
@dp.message_handler(text='/start', state=UZB_lan.uzb_sklad_avto_26004)
@dp.message_handler(text='/start', state=UZB_lan.uzb_sklad_jd_26004)
@dp.message_handler(text='/start', state=UZB_lan.uzb_tuman_avto_26004)
@dp.message_handler(text='/start', state=UZB_lan.uzb_tuman_jd_26004)
@dp.message_handler(text='/start', state=UZB_lan.uzb_sklad_avto_26010)
@dp.message_handler(text='/start', state=UZB_lan.uzb_sklad_jd_26010)
@dp.message_handler(text='/start', state=UZB_lan.uzb_tuman_avto_26010)
@dp.message_handler(text='/start', state=UZB_lan.uzb_tuman_jd_26010)
@dp.message_handler(filters.Text(contains="тилни ўзгартириш", ignore_case=True), state=UZB_lan.uzb)
@dp.message_handler(filters.Text(contains="тилни ўзгартириш", ignore_case=True), state=UZB_lan.uzb_post_avto)
@dp.message_handler(filters.Text(contains="тилни ўзгартириш", ignore_case=True), state=UZB_lan.uzb_post_jd)
async def send_result(message: types.Message):
    await message.answer("🏚 Сиз бош саҳифага қайтдингиз\nВы вернулись на главную страницу\n👇🏻👇🏻👇🏻",
                         reply_markup=language_option)
    await Start_zero.start_zero.set()


@dp.message_handler(filters.Text(contains="ўзбекча", ignore_case=True), state=Start_zero.start_zero)
@dp.message_handler(filters.Text(contains="бекор қилиш", ignore_case=True), state=UZB_lan.uzb)
async def start_register(message: types.Message):
    name = message.from_user.full_name

    await message.answer(
        "📣Ушбу бот орқали сиз <b>очиқ ва эркин божхона омборлар</b> тўғрисидаги маълумотларни билиб олишингиз мумкин бўлади.\n"
        "Жумладан:\n📤Омбор номи\n👨‍⚖️Омбор мудири\n☎️Тел.рақами\n⏰Иш вақти\n📍Манзили\n💰Хизматлар нархи ва бошқалар.\n\n"
        "‼️ Бот фақатгина <b>Тошкент шахар божхона бошқармасига</b> қарашли бўлган омбор маълумотларини тақдим қилади!"
    )
    await message.answer(f"Транспорт турини танланг", reply_markup=main_menu_btn_uz)

    await UZB_lan.uzb.set()


@dp.message_handler(filters.Text(contains="авто", ignore_case=True), state=UZB_lan.uzb)
@dp.message_handler(filters.Text(contains="авто", ignore_case=True), state=UZB_lan.uzb_post_avto)
@dp.message_handler(filters.Text(contains="авто", ignore_case=True), state=UZB_lan.uzb_post_jd)
@dp.message_handler(filters.Text(contains="авто", ignore_case=True), state=UZB_lan.uzb_uz_yukli)
async def start_register(message: types.Message):
    if message.text == "🚚 Авто":
        await message.answer(f"Сиз АВТО йўналишини танладингиз", reply_markup=bekor_qilish_uzb)
        await message.answer(f"🛃 Божхона постини танланг", reply_markup=post_nomi_avto_uzb)
        await UZB_lan.uzb_post_avto.set()

    elif message.text == "🚉 Авто-ЖД":
        await message.answer(f"Сиз АВТО-ЖД йўналишини танладингиз", reply_markup=bekor_qilish_uzb)
        await message.answer(f"🛃 Божхона постини танланг", reply_markup=post_nomi_avto_temiryul_uzb)
        await UZB_lan.uzb_post_jd.set()

    else:
        await message.answer("❌❌❌\nНотўғри қиймат киритдингиз. Илтимос /start тугмаси орқали қайтадан янгиланг.")
        await UZB_lan.uzb.set()


@dp.message_handler(filters.Text(contains="қидириш", ignore_case=True), state=UZB_lan.uzb)
@dp.message_handler(filters.Text(contains="қидириш", ignore_case=True), state=UZB_lan.uzb_uz_yukli)
async def start_register(message: types.Message):
    await message.answer(f"🔍 Қидирув бўлими яясалиш жараёнида")
    await UZB_lan.uzb.set()


@dp.message_handler(filters.Text(contains="ўз юкли омборлар", ignore_case=True), state=UZB_lan.uzb)
async def start_register(message: types.Message):
    await message.answer(f"Ўз юкли омбор номини танланг", reply_markup=uz_yukli_ombor_uzb)
    await UZB_lan.uzb_uz_yukli.set()

@dp.callback_query_handler(state=UZB_lan.uzb_uz_yukli)
async def start_shifokor(call: CallbackQuery):
    await call.message.answer("😐 Узур ҳозирча ушбу омбор маълумотлати қяйта ишлаш жараёнида. Тез кунда маълумотлар қўшиладм 🤓")


# --------------------------AVTO------------------

@dp.message_handler(filters.Text(contains="260", ignore_case=True), state=UZB_lan.uzb_post_avto)
@dp.message_handler(filters.Text(contains="260", ignore_case=True), state=UZB_lan.uzb_sklad_avto_26002)
@dp.message_handler(filters.Text(contains="260", ignore_case=True), state=UZB_lan.uzb_sklad_avto_26003)
@dp.message_handler(filters.Text(contains="260", ignore_case=True), state=UZB_lan.uzb_sklad_avto_26004)
@dp.message_handler(filters.Text(contains="260", ignore_case=True), state=UZB_lan.uzb_sklad_avto_26010)
async def start_register(message: types.Message):
    if message.text == '26002 - “Тошкент-товар” ТИФ':
        await message.answer(f'Сиз "Тошкент-товар" ТИФ божхона постини танладингиз', reply_markup=orqaga_qaytish_uzb)
        await message.answer(f"Илтимос туман номини танланг", reply_markup=Tumanlar_26002_uzb_avto)
        await UZB_lan.uzb_sklad_avto_26002.set()

    elif message.text == "26003 - “Арқ булоқ” ТИФ":
        await message.answer(f'Сиз "Арк булоқ" ТИФ божхона постини танладингиз', reply_markup=orqaga_qaytish_uzb)
        await message.answer(f"Илтимос туман номини танланг", reply_markup=Tumanlar_26003_uzb_avto)
        await UZB_lan.uzb_sklad_avto_26003.set()

    elif message.text == '26004 - “Чуқурсой” ТИФ':
        await message.answer(f'Сиз "Чуқурсой" ТИФ божхона постини танладингиз', reply_markup=orqaga_qaytish_uzb)
        await message.answer(f"Илтимос туман номини танланг", reply_markup=Tumanlar_26004_uzb_avto)
        await UZB_lan.uzb_sklad_avto_26004.set()

    elif message.text == "26010 - “Сирғали” ТИФ":
        await message.answer(f'Сиз "Сирғали" ТИФ божхона постини танладингиз', reply_markup=orqaga_qaytish_uzb)
        await message.answer(f"Илтимос туман номини танланг", reply_markup=Tumanlar_26010_uzb_avto)
        await UZB_lan.uzb_sklad_avto_26010.set()

    else:
        pass


# --------------------------JD------------------

@dp.message_handler(filters.Text(contains="260", ignore_case=True), state=UZB_lan.uzb_post_jd)
@dp.message_handler(filters.Text(contains="260", ignore_case=True), state=UZB_lan.uzb_sklad_jd_26002)
@dp.message_handler(filters.Text(contains="260", ignore_case=True), state=UZB_lan.uzb_sklad_jd_26003)
@dp.message_handler(filters.Text(contains="260", ignore_case=True), state=UZB_lan.uzb_sklad_jd_26004)
@dp.message_handler(filters.Text(contains="260", ignore_case=True), state=UZB_lan.uzb_sklad_jd_26010)
async def start_register(message: types.Message):
    if message.text == '26002 - “Тошкент-товар” ТИФ':
        await message.answer(f'Сиз "Тошкент-товар" ТИФ божхона постини танладингиз', reply_markup=orqaga_qaytish_uzb)
        await message.answer(f"Илтимос туман номини танланг", reply_markup=Tumanlar_26002_uzb_jd)
        await UZB_lan.uzb_sklad_jd_26002.set()

    elif message.text == "26003 - “Арқ булоқ” ТИФ":
        await message.answer(f'Сиз "Арк булоқ" ТИФ божхона постини танладингиз', reply_markup=orqaga_qaytish_uzb)
        await message.answer(f"Илтимос туман номини танланг", reply_markup=Tumanlar_26003_uzb_jd)
        await UZB_lan.uzb_sklad_jd_26003.set()

    elif message.text == '26004 - “Чуқурсой” ТИФ':
        await message.answer(f'Сиз "Чуқурсой" ТИФ божхона постини танладингиз', reply_markup=orqaga_qaytish_uzb)
        await message.answer(f"Илтимос туман номини танланг", reply_markup=Tumanlar_26004_uzb_jd)
        await UZB_lan.uzb_sklad_jd_26004.set()

    elif message.text == "26010 - “Сирғали” ТИФ":
        await message.answer(f'Сиз "Сирғали" ТИФ божхона постини танладингиз', reply_markup=orqaga_qaytish_uzb)
        await message.answer(f"Илтимос туман номини танланг", reply_markup=Tumanlar_26010_uzb_jd)
        await UZB_lan.uzb_sklad_jd_26010.set()

    else:
        pass


# --------------------------AVTO------------------

@dp.message_handler(filters.Text(contains="орқага", ignore_case=True), state=UZB_lan.uzb_post_avto)
async def start_register(message: types.Message):
    if message.text == "⬅️ Орқага":
        await message.answer(f"Илтимос транспорт турини танланг", reply_markup=main_menu_btn_uz)
        await UZB_lan.uzb.set()
    else:
        pass


@dp.message_handler(filters.Text(contains="орқага", ignore_case=True), state=UZB_lan.uzb_sklad_avto_26002)
@dp.message_handler(filters.Text(contains="орқага", ignore_case=True), state=UZB_lan.uzb_sklad_avto_26003)
@dp.message_handler(filters.Text(contains="орқага", ignore_case=True), state=UZB_lan.uzb_sklad_avto_26004)
@dp.message_handler(filters.Text(contains="орқага", ignore_case=True), state=UZB_lan.uzb_sklad_avto_26010)
async def start_register(message: types.Message):
    if message.text == "⬅️ Орқага":
        await message.answer(f"Илтимос транспорт турини танланг", reply_markup=main_menu_btn_uz)
        await UZB_lan.uzb_post_avto.set()
    else:
        pass


# --------------------------JD------------------

@dp.message_handler(filters.Text(contains="орқага", ignore_case=True), state=UZB_lan.uzb_post_jd)
async def start_register(message: types.Message):
    if message.text == "⬅️ Орқага":
        await message.answer(f"Илтимос транспорт турини танланг", reply_markup=main_menu_btn_uz)
        await UZB_lan.uzb.set()
    else:
        pass


@dp.message_handler(filters.Text(contains="орқага", ignore_case=True), state=UZB_lan.uzb_sklad_jd_26002)
@dp.message_handler(filters.Text(contains="орқага", ignore_case=True), state=UZB_lan.uzb_sklad_jd_26003)
@dp.message_handler(filters.Text(contains="орқага", ignore_case=True), state=UZB_lan.uzb_sklad_jd_26004)
@dp.message_handler(filters.Text(contains="орқага", ignore_case=True), state=UZB_lan.uzb_sklad_jd_26010)
async def start_register(message: types.Message):
    if message.text == "⬅️ Орқага":
        await message.answer(f"Илтимос транспорт турини танланг ", reply_markup=main_menu_btn_uz)
        await UZB_lan.uzb_post_jd.set()
    else:
        pass


# --------------------------AVTO_26002------------------

@dp.callback_query_handler(text="Бектемир тумани 26002_avto", state=UZB_lan.uzb_sklad_avto_26002)
async def start_shifokor(call: CallbackQuery):
    await call.message.answer("Омбор номини танланг", reply_markup=avto_26002_bektemir)


@dp.callback_query_handler(text="Яшнобод тумани 26002_avto", state=UZB_lan.uzb_sklad_avto_26002)
async def start_shifokor(call: CallbackQuery):
    await call.message.answer("Омбор номини танланг", reply_markup=avto_26002_yashnabod)


@dp.callback_query_handler(text="Шайхонтоҳур тумани 26002_avto", state=UZB_lan.uzb_sklad_avto_26002)
async def start_shifokor(call: CallbackQuery):
    await call.message.answer("Омбор номини танланг", reply_markup=avto_26002_yakkasaroy)


@dp.callback_query_handler(text="Яккасарой тумани 26002_avto", state=UZB_lan.uzb_sklad_avto_26002)
async def start_shifokor(call: CallbackQuery):
    await call.message.answer("Омбор номини танланг", reply_markup=avto_26002_shayxontohur)

@dp.callback_query_handler(text='"HEKLER" MCHJ', state=UZB_lan.uzb_sklad_avto_26002)
@dp.callback_query_handler(text='ООО "APP SERVIS"', state=UZB_lan.uzb_sklad_avto_26002)
@dp.callback_query_handler(text='ООО "TOP SMART LINE"', state=UZB_lan.uzb_sklad_avto_26002)
@dp.callback_query_handler(text='"DIPLOMATIK KORPUSGA XIZMAT KO`RSATISH BYUROSI" DUK', state=UZB_lan.uzb_sklad_avto_26002)
@dp.callback_query_handler(text='ООО "HIRING-SERVIS"', state=UZB_lan.uzb_sklad_avto_26002)
async def start_shifokor(call: CallbackQuery):
    await call.message.answer("⚠️⚠️⚠️\n\nОмбор маълумотлари ҳали киритилмаган. Бу шунчаки намуна")
    await call.message.answer(hide_link("https://telegra.ph/OOO-Coca-Cola-Ichimligi-Uzbekistan-LTD-03-24"))
    await call.message.answer_location(latitude=41.296201, longitude=69.298287)

# --------------------------AVTO_26003------------------


@dp.callback_query_handler(text='Янгийўл тумани 26003_avto', state=UZB_lan.uzb_sklad_avto_26003)
async def start_shifokor(call: CallbackQuery):
    await call.message.answer("Омбор номини танланг", reply_markup=avto_26003_yangiyul)


@dp.callback_query_handler(text='Зангота тумани 26003_avto', state=UZB_lan.uzb_sklad_avto_26003)
async def start_shifokor(call: CallbackQuery):
    await call.message.answer("Омбор номини танланг", reply_markup=avto_26003_zangiota)


@dp.callback_query_handler(text='Сергели тумани 26003_avto', state=UZB_lan.uzb_sklad_avto_26003)
async def start_shifokor(call: CallbackQuery):
    await call.message.answer("Омбор номини танланг", reply_markup=avto_26003_sergeli)


@dp.callback_query_handler(text='Чилонзор тумани 26003_avto', state=UZB_lan.uzb_sklad_avto_26003)
async def start_shifokor(call: CallbackQuery):
    await call.message.answer("Омбор номини танланг", reply_markup=avto_26003_chilonzor)


@dp.callback_query_handler(text='Яккасарой тумани 26003_avto', state=UZB_lan.uzb_sklad_avto_26003)
async def start_shifokor(call: CallbackQuery):
    await call.message.answer("Омбор номини танланг", reply_markup=avto_26003_yakkasaroy)


@dp.callback_query_handler(text='"ARK-BULOQ KARVONSAROYI" MCHJ', state=UZB_lan.uzb_sklad_avto_26003)
@dp.callback_query_handler(text='ООО "HIGHWAY LOGISTICS CENTER"', state=UZB_lan.uzb_sklad_avto_26003)
@dp.callback_query_handler(text='ЧП "PHARMAX"', state=UZB_lan.uzb_sklad_avto_26003)
@dp.callback_query_handler(text='ООО "SHOHJAHON AGRO"', state=UZB_lan.uzb_sklad_avto_26003)
@dp.callback_query_handler(text='ООО "CAPITAL LOGISTICS 2020"', state=UZB_lan.uzb_sklad_avto_26003)
@dp.callback_query_handler(text='OOO "ELITE GLOBAL PLUS"', state=UZB_lan.uzb_sklad_avto_26003)
async def start_shifokor(call: CallbackQuery):
    await call.message.answer("⚠️⚠️⚠️\n\nОмбор маълумотлари ҳали киритилмаган. Бу шунчаки намуна")
    await call.message.answer(hide_link("https://telegra.ph/OOO-Coca-Cola-Ichimligi-Uzbekistan-LTD-03-24"))
    await call.message.answer_location(latitude=41.296201, longitude=69.298287)

# --------------------------JD------------------

# @dp.callback_query_handler(text="Бектемир тумани", state=UZB_lan.uzb_sklad_jd)
# async def start_shifokor(call: CallbackQuery):
#     await call.message.answer(hide_link("https://telegra.ph/OOO-Coca-Cola-Ichimligi-Uzbekistan-LTD-03-24"))
#     await call.message.answer_location(latitude=41.296201, longitude=69.298287)

    # await call.message.answer_photo(photo='https://telegra.ph/coca-cola-mchj-03-23', caption="BEKTEMIRRRRRRRRRRR")
    # await UZB_lan.uzb_tuman.set()

    # def webAppKeyboard():  # создание клавиатуры с webapp кнопкой
    #     keyboard = types.ReplyKeyboardMarkup(row_width=1)  # создаем клавиатуру
    #     webAppTest = types.WebAppInfo("https://www.kun.uz")
    #     one_butt = types.KeyboardButton(text="Тестовая страница", web_app=webAppTest)  # создаем кнопку типа webapp
    #     keyboard.add(one_butt)  # добавляем кнопки в клавиатуру
    #     return keyboard  # возвращаем клавиатуру

    # await call.message.answer("Lorem", reply_markup=webAppKeyboard())
