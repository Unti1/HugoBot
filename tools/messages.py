from settings import *
from tools import *

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Тест")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Тест")

async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()

async def regular_posting_kwork():
    await bot.send_message()