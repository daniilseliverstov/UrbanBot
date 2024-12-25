from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_contacts_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(types.InlineKeyboardButton(text="Показать контакты", callback_data="show_contacts"))
    return keyboard.as_markup()

