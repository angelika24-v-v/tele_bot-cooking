import asyncio # библиотека, которая отвечает за асинхронную работу
import logging  # абор функций и классов, которые позволяют регистрировать события, происходящие во время работы кода.

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand
from aiogram.types.bot_command_scope import BotCommandScopeAllPrivateChats

from config_loader import Config, load_config
from handlers.start import start_handlers
from updatesworker import get_handled_updates_list


async def set_bot_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Запустить бота"),
    ]

    await bot.set_my_commands(commands, scope=BotCommandScopeAllPrivateChats())


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        # filename="recipe.log"
    )

    config: Config = load_config()

    storage = MemoryStorage()
    bot = Bot(config.bot.token, parse_mode="HTML")
    dp = Dispatcher(bot, storage=storage)

    start_handlers(dp)

    await set_bot_commands(bot)

    try:
        await dp.skip_updates()
        await dp.start_polling(allowed_updates=get_handled_updates_list(dp))

    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


try:
    asyncio.run(main())
except (KeyboardInterrupt, SystemExit):
    logging.error("Bot stopped!")
