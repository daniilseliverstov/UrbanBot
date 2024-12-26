from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardMarkup, KeyboardButton


def get_main_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(types.InlineKeyboardButton(text="Мусор", callback_data="category_waste"))
    keyboard.add(types.InlineKeyboardButton(text="Транспорт", callback_data="category_transport"))
    keyboard.add(types.InlineKeyboardButton(text="Дороги", callback_data="category_roads"))
    keyboard.add(types.InlineKeyboardButton(text="Роспотребнадзор", callback_data="category_rpn"))
    return keyboard.as_markup()


def get_start_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Начать")]],
        resize_keyboard=True
    )
    return keyboard
