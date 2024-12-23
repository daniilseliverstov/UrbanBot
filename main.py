import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

with open("teg_api") as file:
    api_token = file.read()

logging.basicConfig(level=logging.INFO)
bot = Bot(token=api_token)
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
