from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

language_option = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🇺🇿 Ўзбекча"), KeyboardButton(text="🇷🇺 Русский")]
    ], resize_keyboard=True
)

# option_av_uz = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="Ўз юкли омборлар")],
#         [KeyboardButton(text="")],
#     ],
# )
#
# option_av_ru = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="")],
#         [KeyboardButton(text="Склады собственных грузов")],
#     ],
# )

main_menu_btn_uz = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🚚 Авто"), KeyboardButton(text="🚉 Авто-ЖД")],
        [KeyboardButton(text="🔍 Қидириш"), KeyboardButton(text="Ўз юкли омборлар")],
        [KeyboardButton(text="🚩 Тилни ўзгартириш")],
    ], resize_keyboard=True
)

main_menu_btn_ru = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🚚 Авто"), KeyboardButton(text="🚉 Авто-ЖД")],
        [KeyboardButton(text="🔍 Поиск"), KeyboardButton(text="Склады собственных грузов")],
        [KeyboardButton(text="🚩 Смена языка")],
    ], resize_keyboard=True
)

bekor_qilish_uzb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='❌ Бекор қилиш')],
    ], resize_keyboard=True
)

bekor_qilish_rus = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='❌ Отмена')],
    ], resize_keyboard=True
)

post_nomi_avto_uzb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='26002 - “Тошкент-товар” ТИФ'), KeyboardButton(text="26003 - “Арқ булоқ” ТИФ")],
        [KeyboardButton(text='26004 - “Чуқурсой” ТИФ'), KeyboardButton(text="26010 - “Сирғали” ТИФ")],
        [KeyboardButton(text='⬅️ Орқага')],
    ], resize_keyboard=True
)
post_nomi_avto_temiryul_uzb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='26002 - “Тошкент-товар” ТИФ'), KeyboardButton(text="26003 - “Арқ булоқ” ТИФ")],
        [KeyboardButton(text='26004 - “Чуқурсой” ТИФ'), KeyboardButton(text="26010 - “Сирғали” ТИФ")],
        [KeyboardButton(text='⬅️ Орқага')],
    ], resize_keyboard=True
)

post_nomi_avto_rus = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='26002 - «Ташкент-товарный» ВЭД'), KeyboardButton(text="26003 - «Аркбулак» ВЭД")],
        [KeyboardButton(text='26004 - «Чукурсай» ВЭД'), KeyboardButton(text="26010 - «Сергели» ВЭД")],
        [KeyboardButton(text='⬅️ Назад')],
    ], resize_keyboard=True
)

post_nomi_avto_temiryul_rus = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='26002 - «Ташкент-товарный» ВЭД'), KeyboardButton(text="26003 - «Аркбулак» ВЭД")],
        [KeyboardButton(text='26004 - «Чукурсай» ВЭД'), KeyboardButton(text="26010 - «Сергели» ВЭД")],
        [KeyboardButton(text='⬅️ Назад')],
    ], resize_keyboard=True
)

orqaga_qaytish_uzb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='⬅️ Орқага')],
    ], resize_keyboard=True
)

orqaga_qaytish_rus = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='⬅️ Назад')],
    ], resize_keyboard=True
)

yes_no = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Ha')],
        [KeyboardButton(text="yo'q")]
    ], resize_keyboard=True
)

devide_soha = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='👩🏻‍🔬 Mutaxassisliklar')],
        [KeyboardButton(text="🔬 Xizmatlar")],
        [KeyboardButton(text="🗂 Umumiy ma'lumotlar")],
        [KeyboardButton(text="⬅️ Qaytish")],
    ], resize_keyboard=True
)

yozilish_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='📝 Qabulga yozilish')],
        [KeyboardButton(text='📥 Natijani olish')],
        [KeyboardButton(text='⬅️ Ortga qaytish')],
    ], resize_keyboard=True
)

data_clinic = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='🔍 Umumiy tavsif')],
        [KeyboardButton(text='🧾 Litsenziya')],
        [KeyboardButton(text='📜 Guvohnoma')],
        [KeyboardButton(text='📍 Bizning manzilimiz')],
        [KeyboardButton(text='⬅️ Ortga qaytish')],
    ], resize_keyboard=True
)

ocherad_fields = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='👼🏻 Pediatr'), KeyboardButton(text="🦠 Immunolog")],
        [KeyboardButton(text='🧬 Genikolog'), KeyboardButton(text="🩺 Terapevt")],
        [KeyboardButton(text='🧠 Nevropatolog'), KeyboardButton(text="🦻🏻 Lor")],
        [KeyboardButton(text='🙇🏻‍♂️ Massajist'), KeyboardButton(text="💉 Endokrinolog")],
        [KeyboardButton(text='🍤 Gastroenterolog'), KeyboardButton(text="⬅️ Ortga qaytish")],
    ], resize_keyboard=True
)

yes_no_for_qabul = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='✅ Ha')],
        [KeyboardButton(text="❌ Yo'q")]
    ], resize_keyboard=True
)

reklama_tasdiqlash = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='✅ Ha')],
        [KeyboardButton(text="❌ Yo'q")]
    ], resize_keyboard=True
)

start_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='/start')],
    ], resize_keyboard=True
)
