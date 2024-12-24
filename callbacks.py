from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

router = Router(name="callbacks")

@router.callback_query(F.text == "get_contacts")
async def get_contacts_callback(callback: CallbackQuery, state: FSMContext):
    print("Кнопка нажата")  # Лог для отладки
    contacts_data = router.contacts_data
    text = "<b>Контакты для подачи заявлений:</b>\n\n"

    for organization, data in contacts_data.items():
        text += f"<b>{organization}:</b>\n"
        text += f"Официальный сайт: {data['Официальный сайт']}\n"

        if "Телефон" in data:
            text += f"Телефон: {data['Телефон']}\n"

        if "Email" in data:
            text += f"Email: {data['Email']}\n"

        if "Страница заявления" in data:
            text += f"Ссылка для подачи заявления: {data['Страница заявления']}\n"

        text += "\n"

    await callback.message.edit_text(text)
