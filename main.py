import logging
import asyncio
import json
from aiogram import Bot, Dispatcher
from handlers import router as handlers_router
from callbacks import router as callbacks_router


def load_contacts_from_json(file_path="trash_contact.json"):
    with open(file_path, encoding='utf-8') as f:
        return json.load(f)


with open("teg_api") as file:
    api_token = file.read().strip()

logging.basicConfig(level=logging.INFO)
bot = Bot(token=api_token)
dp = Dispatcher()
contacts_data = load_contacts_from_json()

dp.include_router(handlers_router)
dp.include_router(callbacks_router)
callbacks_router.contacts_data = contacts_data

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
