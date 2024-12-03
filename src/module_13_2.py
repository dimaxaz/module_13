import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    print('Привет! Я бот помогающий твоему здоровью.')
    await message.reply('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_messages(message: types.Message):
    print('Введите команду /start, чтобы начать общение.')
    await message.reply('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    print('Updates were skipped successfully.')
    executor.start_polling(dp, skip_updates=True) 