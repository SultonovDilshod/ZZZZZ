from aiogram import executor
from aiogram import Dispatcher
# from aiogram import Bot, types, Dispatcher, executor
#
#
# from aiogram.dispatcher.dispatcher import Dispatcher
from loader import dp, db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):

    await set_default_commands(dispatcher)

    try:
        db.create_table_users()
    except Exception as err:
        print(err)

    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp)
