from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Mutaxassisliklar = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Pediatr", callback_data='001'),
         InlineKeyboardButton(text="Immunolog", callback_data='001')],
        [InlineKeyboardButton(text="Genikolog", callback_data='001'),
         InlineKeyboardButton(text="Terapevt", callback_data='001')],
        [InlineKeyboardButton(text="Nevropatolog", callback_data='001'),
         InlineKeyboardButton(text='Lor', callback_data='001')],
        [InlineKeyboardButton(text="Gastroenterolog", callback_data='001')],
        [InlineKeyboardButton(text="Endokrinolog", callback_data='001')],
        [InlineKeyboardButton(text="Nevropatolog", callback_data='001')],
        [InlineKeyboardButton(text="Massajist", callback_data='001')],
    ],
)

Xizmatlar = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Gidromassaj", callback_data='001'),
         InlineKeyboardButton(text="EKG", callback_data='001')],
        [InlineKeyboardButton(text="Uzi, Exo, Doppler", callback_data='001')],
        [InlineKeyboardButton(text="Laboratoriya tahlillar", callback_data='001')],
        [InlineKeyboardButton(text="Massaj:\n🔘 Bolalar uchun\n🔘Kattalar uchun", callback_data='001')],
        [InlineKeyboardButton(text="Yassi oyoqlikni davolash", callback_data='001')],
        [InlineKeyboardButton(text="Fizioterapiya:\n🔘 Darsonval\n🔘Elektroforez", callback_data='001')],
    ],
)

Yozilish = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='👼🏻 Pediatr', callback_data='001'),
         InlineKeyboardButton(text="🦠 Immunolog", callback_data='001')],
        [InlineKeyboardButton(text="🧬 Genikolog", callback_data='001'),
         InlineKeyboardButton(text="🩺 Terapevt", callback_data='001')],
        [InlineKeyboardButton(text="🧠 Nevropatolog", callback_data='001'),
         InlineKeyboardButton(text='🦻🏻 Lor', callback_data='001')],
        [InlineKeyboardButton(text="🍤 Gastroenterolog", callback_data='001')],
        [InlineKeyboardButton(text="💉 Endokrinolog", callback_data='001')],
        [InlineKeyboardButton(text="🙇🏻‍♂️ Massajist", callback_data='001')],
    ],
)
