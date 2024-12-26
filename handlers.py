from aiogram import Dispatcher, types
from aiogram.filters import CommandStart
from keyboards import get_main_keyboard, get_start_keyboard


def register_handlers(dp: Dispatcher, contacts_data):
    @dp.message(CommandStart())
    async def start_command(message: types.Message):
        keyboard = get_main_keyboard()
        await message.answer(
            "Привет! Этот бот поможет вам связаться с нужными организациями по вопросам благоустройства.\n"
            "Выберите интересующую вас категорию:",
            reply_markup=keyboard
        )

    @dp.message(lambda message: True)  # Обработчик для любых текстовых сообщений
    async def unknown_message(message: types.Message):
        keyboard = get_start_keyboard()
        await message.answer(
            "Извините, я не понял ваше сообщение. Пожалуйста, используйте кнопки меню или нажмите кнопку 'Начать'.",
            reply_markup=keyboard
        )
