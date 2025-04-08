import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import find_dotenv, load_dotenv

from handlers.user_private import user_router

load_dotenv(find_dotenv())
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()
allowed = ['message, callback_query, inline_query']

dp.include_router(user_router)







async def work():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=allowed)

asyncio.run(work())