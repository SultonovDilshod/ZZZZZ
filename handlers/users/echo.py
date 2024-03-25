from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer("❌ Noma'lum buyruq!\n\nSiz to'g'ridan-to'g'ri bot chatiga xabar yubordingiz, yoki "
                         "bot tuzilishi yaratuvchisi tomonidan o'zgartirilgan boʻlishi mumkin.\n\n"
                         "ℹ️ Xabarlarni to'g'ridan-to'g'ri botga yubormang yoki "
                         "/start orqali bot menyusini yangilang")
