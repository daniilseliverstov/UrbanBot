from aiogram import Router, F
from aiogram.enums import ChatType
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboards import get_main_menu_keyboard

router = Router(name="handlers")


@router.message(F.chat.type == ChatType.PRIVATE, F.text == "/start")
async def cmd_start(message: Message, state: FSMContext):
    keyboard = get_main_menu_keyboard()
    await message.answer(
        "Привет! Я помогу тебе отправить заявление о неубранном мусоре.\n\nНажми на кнопку ниже, чтобы получить список контактов:",
        reply_markup=keyboard
    )
