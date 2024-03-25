from aiogram.dispatcher.filters.state import StatesGroup, State


class UZB_lan(StatesGroup):
    uzb = State()
    uzb_uz_yukli = State()

    uzb_post_avto = State()
    uzb_post_jd = State()

    uzb_sklad_avto_26002 = State()
    uzb_sklad_avto_26003 = State()
    uzb_sklad_avto_26004 = State()
    uzb_sklad_avto_26010 = State()
    uzb_sklad_jd_26002 = State()
    uzb_sklad_jd_26003 = State()
    uzb_sklad_jd_26004 = State()
    uzb_sklad_jd_26010 = State()

    uzb_tuman_avto_26002 = State()
    uzb_tuman_avto_26003 = State()
    uzb_tuman_avto_26004 = State()
    uzb_tuman_avto_26010 = State()
    uzb_tuman_jd_26002 = State()
    uzb_tuman_jd_26003 = State()
    uzb_tuman_jd_26004 = State()
    uzb_tuman_jd_26010 = State()
