from aiogram import Bot, types
from aiogram.dispatcher.dispatcher import Dispatcher
# from aiogram.fsm.storage.memory import MemoryStorage
# from aiogram.enums.parse_mode import ParseMode
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from utils.hello.sqlite import DataBase

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)
db = DataBase(path_to_db="data/main.db")
