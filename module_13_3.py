from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    """
    Реакция на команду /start
    :param message:
    :return:
    """
    await message.answer('Привет! Я бот, помогающий твоему здоровью.')


@dp.message_handler()
async def all_massages(message):
    """
    Реакция на любое сообщение, кроме /start
    :param message:
    :return:
    """
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
