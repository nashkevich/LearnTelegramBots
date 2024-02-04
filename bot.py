import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from main import get_trades,get_ticker

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "6950136664:AAF2q-FQdfe9Wje-vYEWg2EMwO55k-vwYdM"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)


async def send_status():
    while True:
        await bot.send_message(text=get_trades(),chat_id=692407594)
        await asyncio.sleep(60)







async def main() -> None:
    await dp.start_polling(bot,on_startup = await send_status())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())