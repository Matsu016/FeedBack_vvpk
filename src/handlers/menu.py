from aiogram import types, Router, F

from src.keyboards import feedback_choise
from src.data_base import Database

router = Router()


@router.message(F.text == "📝 Додати відгук 📒")
async def add_feedback(message: types.Message):
    await message.answer(text="Куди ви хочете додати?", reply_markup=feedback_choise())


@router.message(F.text == "😱 Переглянути відгук 😱")
async def cmd_start(message: types.Message):
    await message.answer(text="Куди ви хочете додати?", reply_markup=feedback_choise())


@router.message(F.text == "📋 Про бота 📋")
async def cmd_start(message: types.Message):
    await message.answer(text="Інформаці про бота:")


@router.callback_query(F.data == "Сховати ❌")
async def sxovatu(query: types.CallbackQuery):
    await query.message.delete()


@router.message(F.text == "📈 Статистика 📉")
async def cmd_start(message: types.Message):
    db = await Database.setup()

    caption = (
        "<b>Cтатистика</b> 📊:\n",
        f"  • Користувачів 👥: {await db.count_users()}\n",
        f"  • Відгуків 📝: {0}\n",
        f"     ╰ Викладачів 👨‍🏫: {0}\n",
        f"     ╰ Предметів 📕: {0}\n",
        f"     ╰ Коледджу 🏫: {0}\n",
        f"  • Прийнятих відгуків ✅: {0}\n",
        f"  • Відхилених відгуків 🚫: {0}\n",
    )

    await message.answer(text="".join(caption), parse_mode="HTML")
