from aiogram import Dispatcher, types, Bot


def register_callbacks(dp: Dispatcher, bot: Bot, contacts_data):

    @dp.callback_query(lambda c: c.data == 'show_contacts')
    async def show_contacts(callback_query: types.CallbackQuery):
        response = "<b>Контакты:</b>\n"
        for org, data in contacts_data.items():
            response += f"\n<b>{org}:</b>\n"
            for key, value in data.items():
                response += f"  - {key}: {value}\n"
        await bot.send_message(callback_query.from_user.id, response, parse_mode="HTML")