from aiogram import Dispatcher, types
from aiogram.filters import CommandStart
from keyboards import get_main_keyboard, get_start_keyboard

def register_handlers(dp: Dispatcher):
    # Обработчик команды /start
    @dp.message(CommandStart())
    async def start_command(message: types.Message):
        keyboard = get_start_keyboard()
        await message.answer(
            "Привет! Этот бот поможет вам связаться с нужными организациями по вопросам благоустройства.\n"
            "Нажмите кнопку 'Начать', чтобы продолжить.",
            reply_markup=keyboard
        )

    # Обработчик кнопки "Начать"
    @dp.callback_query(lambda c: c.data == "start")
    async def handle_start(callback_query: types.CallbackQuery):
        keyboard = get_main_keyboard()
        await callback_query.message.answer(
            "Выберите интересующую вас категорию:",
            reply_markup=keyboard
        )

    # Обработчик неизвестных сообщений
    @dp.message()
    async def unknown_message(message: types.Message):
        keyboard = get_start_keyboard()
        await message.answer(
            "Извините, я не понял ваше сообщение. Пожалуйста, используйте кнопки меню или нажмите кнопку 'Начать'.",
            reply_markup=keyboard
        )