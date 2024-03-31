from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext

from src.keyboards import feedback_choise
from src.data_base import Database

router = Router()


@router.message(F.text == "📝 Додати відгук 📒")
async def add_feedback(message: types.Message):
    await message.answer(
        text="Куди ви хочете додати?", reply_markup=feedback_choise()
    )


@router.message(F.text == "📋 Про бота 📋")
async def cmd_start(message: types.Message):
    await message.answer(text="Інформація про бота:")


@router.callback_query(F.data == "Сховати ❌")
async def hide(query: types.CallbackQuery, state: FSMContext):
    await query.message.delete()
    await state.clear()


@router.message(F.text == "📈 Статистика 📉")
async def cmd_start(message: types.Message):
    db = await Database.setup()

    caption = (
        "<b>Статистика</b> 📊:\n",
        f"  • Користувачів 👥: {await db.count_users()}\n",
        f"  • Відгуків 📝: {await db.count_accept_reject_feedback()}\n",
        f"     ╰ Викладачів 👨‍🏫: {await db.count_teacher_feedback()}\n",
        f"     ╰ Предметів 📕: {await db.count_subject_feedback()}\n",
        f"     ╰ Коледжу 🏫: {await db.count_college_feedback()}\n",
        f"  • Прийнятих відгуків ✅: {await db.count_accept_feedback()}\n",
        f"  • Відхилених відгуків 🚫: {await db.count_reject_feedback()}\n",
    )

    await message.answer(text="".join(caption), parse_mode="HTML")
