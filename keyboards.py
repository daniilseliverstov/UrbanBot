from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_main_keyboard():
    # Создаем клавиатуру с двумя строками по две кнопки
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Мусор", callback_data="category_waste"),
            InlineKeyboardButton(text="Транспорт", callback_data="category_transport")
        ],
        [
            InlineKeyboardButton(text="Дороги", callback_data="category_roads"),
            InlineKeyboardButton(text="Роспотребнадзор", callback_data="category_rpn")
        ]
    ])
    return keyboard


def get_start_keyboard():
    # Клавиатура с одной кнопкой "Начать"
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Начать", callback_data="start")]
    ])
    return keyboard