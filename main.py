import logging
import asyncio
from aiogram import Bot, Dispatcher
import json
from handlers import register_handlers
from callbacks import register_callbacks


with open("teg_api") as file:
    api_token = file.read().strip()

logging.basicConfig(level=logging.INFO)
bot = Bot(token=api_token)
dp = Dispatcher()

with open("trash_contact.json", "r", encoding="utf-8") as file:
    contacts_data = json.load(file)


async def main():
    register_handlers(dp, contacts_data)
    register_callbacks(dp, bot, contacts_data)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
