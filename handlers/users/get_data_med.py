from aiogram import types
from loader import dp
from aiogram.dispatcher import filters
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove, CallbackQuery
from keyboards.default.keyboards import devide_soha, data_clinic
from keyboards.inline.fields_for_get_data import Mutaxassisliklar, Xizmatlar
from states.sohalar import Sohalar
from keyboards.default.keyboards import main_menu_btn_uz
from aiogram.dispatcher import FSMContext


@dp.message_handler(filters.Text(contains="ma'lumot olish", ignore_case=True))
async def start_soha(message: types.Message):
    await message.answer(
        "Assalomu alaykum\n\nHurmatli mijoz siz bizning klinikada mavjud bo'lgan quyidagi ma'lumotlarni"
        " olishingiz mumkin\n\n👇🏻👇🏻👇🏻",
        reply_markup=devide_soha)
    await Sohalar.chose_soha.set()


@dp.message_handler(state=Sohalar.chose_soha)
@dp.message_handler(state=Sohalar.doctors)
async def start_mutaxassislik(message: types.Message, state: FSMContext):
    if message.text.lower() == "👩🏻‍🔬 mutaxassisliklar":
        await message.answer(
            "Klinikamizda mavjud bo'lgan sohalar bo'yicha mutaxassisliklar bilan tanishishingiz mumkin!",
            reply_markup=Mutaxassisliklar)
        await Sohalar.doctors.set()
    elif message.text.lower() == "🔬 xizmatlar":
        await message.answer("Klinikamizda mavjud bo'lgan sohalar bo'yicha xizmat turlari bilan tanishishingiz mumkin!",
                             reply_markup=Xizmatlar)
        await Sohalar.doctors.set()
    elif message.text.lower() == "⬅️ qaytish":
        await message.answer("Bosh sahifa", reply_markup=main_menu_btn)
        await state.finish()
    elif message.text.lower() == "🗂 umumiy ma'lumotlar":
        await message.answer(
            "✅✅✅\n\nSiz <b>Klinika TMC</b> haqida quyidagi ma'lumotlarni ko'rishingiz mumkin:\n\n👇🏻👇🏻👇🏻",
            reply_markup=data_clinic)
        await Sohalar.litsenziya.set()
    else:
        await state.finish()


@dp.callback_query_handler(text="001", state=Sohalar.doctors)
async def start_shifokor(call: CallbackQuery):
    txt_send = "✅ <b>Klinika TMC</b>\n\n" \
               "<b>🔹 Mutaxassisligi: </b>Pediatr\n" \
               "<b>🔹 Lavozimi: </b>Bosh shifokor\n" \
               "<b>🔹 Ish tajribasi: </b>6 yil\n" \
               "<b>🔹 Bog'lanish: </b>loreminput@gmail.com\n" \
               "<b>🔹 Qo'shimcha: </b>Shiforok, bolalar kasalliklari shu jumladan\n" \
               "\t\t\t🔘 Teri kasalliklari\n\t\t\t🔘 Allergik kasallilar\n\t\t\t🔘 Oshqozon-ichak kasalliklar\n " \
               "yo'nalishlari bo'yich davolash ishlarini olib boradi"
    await call.message.answer_photo(photo='https://telegra.ph/Doctor-moster-dishko-07-25', caption=txt_send)
    await Sohalar.doctors.set()
    # await call.message.delete()
    # await call.answer(cache_time=60)


@dp.message_handler(state=Sohalar.litsenziya)
async def start_back(message: types.Message, state: FSMContext):
    if message.text == "⬅️ Ortga qaytish":
        await message.answer("✅ \nMa'lumot olish bo'limi\n\n👇🏻👇🏻👇🏻", reply_markup=devide_soha)
        await Sohalar.chose_soha.set()
    elif message.text == "🔍 Umumiy tavsif":
        await message.answer_photo(photo="https://telegra.ph/Balensa-TMC-07-25",
                                   caption="<b>Klinika TMC</b> 2023-yilda tahskil etilgan. Unda...")
        await Sohalar.litsenziya.set()
    elif message.text == "🧾 Litsenziya":
        await message.answer_photo(photo="https://telegra.ph/Klinika-litsenziyasi-07-25")
        await Sohalar.litsenziya.set()
    elif message.text == "📜 Guvohnoma":
        await message.answer("✅ Ushbu manzil orqali siz guvohnomani ko'rishingiz mumkin\n\n👇🏻👇🏻👇🏻\n"
                             "https://fo.birdarcha.uz/pub/certificate/legal_entities/search?tin=308056897")
        await Sohalar.litsenziya.set()
    elif message.text == "📍 Bizning manzilimiz":
        await message.answer_location(latitude=41.37858296881298, longitude=69.23017442973716)
        await Sohalar.litsenziya.set()
    else:
        await state.finish()


# @dp.message_handler(state=Sohalar.doctors)
# async def start_back(message: types.Message, state: FSMContext):
#     if message.text == "⬅️ Ortga qaytish":
#         await message.answer("Orga qaytdingiz", reply_markup=main_menu_btn)
#         await Sohalar.chose_soha.set()
#     elif message.text == "🔍 Umumiy tavsif":
#         await message.answer_photo(photo="https://telegra.ph/Balensa-TMC-07-25",
#                                    caption="<b>Klinika TMC</b> 2023-yilda tahskil etilgan. Unda...")
#         await Sohalar.doctors.set()
#     elif message.text == "🧾 Litsenziya":
#         await message.answer_photo(photo="https://telegra.ph/Klinika-litsenziyasi-07-25")
#         await Sohalar.doctors.set()
#     elif message.text == "📜 Guvohnoma":
#         await message.answer("✅ Ushbu manzil orqali siz guvohnomani ko'rishingiz mumkin\n\n👇🏻👇🏻👇🏻\n"
#                              "https://fo.birdarcha.uz/pub/certificate/legal_entities/search?tin=308056897")
#         await Sohalar.doctors.set()
#     elif message.text == "📍 Bizning manzilimiz":
#         await message.answer_location(latitude=41.311059, longitude=69.279836)
#         await Sohalar.doctors.set()
#     else:
#         await state.finish()


#
# @dp.message_handler(state=Sohalar.litsenziya)
# async def start_back(message: types.Message, state: FSMContext):
#     if message.text.lower() == "⬅️ ortga qaytish":
#         await message.answer("Orga qaytdingiz", reply_markup=main_menu_btn)
#         await Sohalar.chose_soha.set()
#     else:
#         await state.finish()
#
# # @dp.message_handler(filters.Text(contains="ortga qaytish"), state=Sohalar.doctors)
# # async def start_back(message: types.Message):
# #     await message.answer("Orga qaytdingiz", reply_markup=main_menu_btn)
# #     await Sohalar.chose_soha.set()
#
#
# @dp.message_handler(filters.Text(contains="umumiy tavsif", ignore_case=True))
# async def start_tavsif(message: types.Message):
#     await message.answer_photo(photo="https://telegra.ph/Balensa-TMC-07-25",
#                                caption="<b>Klinika TMC</b> 2023-yilda tahskil etilgan. Unda...")
#
#
# @dp.message_handler(filters.Text(contains="litsenziya", ignore_case=True))
# async def start_mutaxassislik(message: types.Message):
#     await message.answer_photo(photo="https://telegra.ph/Klinika-litsenziyasi-07-25")
#
#
# @dp.message_handler(filters.Text(contains="guvohnoma", ignore_case=True))
# async def start_mutaxassislik(message: types.Message):
#     await message.answer("✅ Ushbu manzil orqali siz guvohnomani ko'rishingiz mumkin\n\n👇🏻👇🏻👇🏻\n"
#                          "https://fo.birdarcha.uz/pub/certificate/legal_entities/search?tin=308056897")
#
#
# @dp.message_handler(filters.Text(contains="bizning manzilimiz", ignore_case=True))
# async def start_mutaxassislik(message: types.Message):
#     await message.answer_location(latitude=41.311059, longitude=69.279836)
#
