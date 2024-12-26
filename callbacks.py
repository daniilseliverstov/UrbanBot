from aiogram import Dispatcher, types, Bot
from aiogram.utils.keyboard import InlineKeyboardBuilder


def register_callbacks(dp: Dispatcher, bot: Bot, contacts_data):
    @dp.callback_query(lambda c: c.data.startswith('category_'))
    async def handle_category(callback_query: types.CallbackQuery):
        category = callback_query.data.split('_')[1]
        if category == 'waste':
            keyboard = InlineKeyboardBuilder()
            keyboard.add(types.InlineKeyboardButton(text="Куда обращаться", callback_data="show_contacts_waste"))
            await callback_query.message.edit_text(
                "Вы выбрали категорию 'Мусор'. Что вы хотите сделать?",
                reply_markup=keyboard.as_markup()
            )
        elif category == 'transport':
            await callback_query.message.edit_text(
                "Вы выбрали категорию 'Транспорт'. Эта функциональность в разработке."
            )
        elif category == 'roads':
            await callback_query.message.edit_text(
                "Вы выбрали категорию 'Дороги'. Эта функциональность в разработке."
            )
        elif category == 'rpn':
            await callback_query.message.edit_text(
                "Вы выбрали категорию 'Роспотребнадзор'. Эта функциональность в разработке."
            )

    @dp.callback_query(lambda c: c.data == 'show_contacts_waste')
    async def show_contacts(callback_query: types.CallbackQuery):
        response = "<b>Контакты по вопросам мусора:</b>\n"
        for org, data in contacts_data.items():
            response += f"\n<b>{org}:</b>\n"
            for key, value in data.items():
                response += f"  - {key}: {value}\n"
        await bot.send_message(callback_query.from_user.id, response, parse_mode="HTML")
