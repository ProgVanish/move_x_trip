import asyncio
import logging
from config import config
from aiogram import Bot, Dispatcher
from handlers import registration

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=config.token.get_secret_value())
    dp = Dispatcher()
    dp.include_routers(registration.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())