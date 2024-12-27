from aiogram import Dispatcher, types, Bot
from aiogram.utils.keyboard import InlineKeyboardBuilder


def register_callbacks(dp: Dispatcher, bot: Bot, contacts_data):
    # Обработчик выбора категории
    @dp.callback_query(lambda c: c.data.startswith('category_'))
    async def handle_category(callback_query: types.CallbackQuery):
        category = callback_query.data.split('_')[1]
        if category in contacts_data:  # Проверяем, есть ли данные для этой категории
            keyboard = InlineKeyboardBuilder()
            keyboard.add(types.InlineKeyboardButton(text="Куда обращаться", callback_data=f"show_contacts_{category}"))
            await callback_query.message.edit_text(
                f"Вы выбрали категорию '{category}'. Что вы хотите сделать?",
                reply_markup=keyboard.as_markup()
            )
        else:
            await callback_query.message.edit_text(
                f"Вы выбрали категорию '{category}'. Эта функциональность в разработке."
            )

    # Обработчик показа контактов
    @dp.callback_query(lambda c: c.data.startswith('show_contacts_'))
    async def show_contacts(callback_query: types.CallbackQuery):
        category = callback_query.data.split('_')[2]  # Извлекаем категорию
        contacts = contacts_data.get(category, {})

        if not contacts:
            await callback_query.message.answer("Контакты для этой категории отсутствуют.")
            return

        response = f"<b>Контакты по категории '{category}':</b>\n"
        for org, data in contacts.items():
            response += f"\n<b>{org}:</b>\n"
            for key, value in data.items():
                response += f"  - {key}: {value}\n"

        await bot.send_message(callback_query.from_user.id, response, parse_mode="HTML")
