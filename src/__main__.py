import asyncio
import logging
from aiogram import Bot, Dispatcher
from src.config import TOKEN
from src.handlers import comands, menu, submenu, view_feedback


async def register_handlers(dp: Dispatcher) -> None:
    dp.include_router(submenu.router)
    dp.include_router(comands.router)
    dp.include_router(view_feedback.router)
    dp.include_router(menu.router)


async def start_bot() -> None:
    bot = Bot(token=TOKEN)
    dispatcher = Dispatcher()

    await register_handlers(dispatcher)
    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(start_bot())
