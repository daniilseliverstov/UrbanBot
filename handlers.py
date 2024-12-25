from aiogram import Dispatcher, types
from aiogram.filters import CommandStart
from keyboards import get_contacts_keyboard


def register_handlers(dp: Dispatcher, contacts_data):
    @dp.message(CommandStart())
    async def start_command(message: types.Message):
        keyboard = get_contacts_keyboard()
        await message.answer("Привет! Нажми кнопку, чтобы посмотреть контакты:", reply_markup=keyboard)




