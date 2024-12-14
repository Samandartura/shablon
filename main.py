from asyncio import run

from aiogram.types import BotCommand
from aiogram import Bot, Dispatcher , types, F
from aiogram.filters import Command
from humanfriendly.terminal import message

import filter
import funksiyalar
dp = Dispatcher()

async def funk1(bot:Bot):
    await bot.send_message(chat_id=8186528368,text="Bot ishlamoqda")

async def funk2(bot:Bot):
    await bot.send_message(chat_id=8186528368,text="Bot tuxtadi")

async def start():
    dp.startup.register(funk1)
    dp.shutdown.register(funk2)

    bot = Bot("5358442766:AAHgnJt3NfcRUbC-vlCN7S6Cz6dfeEXJ8ck")

    await bot.set_my_commands([
        BotCommand(command="/start", description="Botni ishga tushirish"),
        BotCommand(command="/help", description="yordam uchun ")
    ])    
    print("Bot ishga tushdi")
    await dp.start_polling(bot, polling_timeout=1)



run(start())