from settings import *
from .sites_parse import *

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    print(message.from_user.id)
    await message.reply("Привет!\nНапиши мне что-нибудь!")

@dp.message_handler(commands=['add_me'])
async def add_to_autoposting_id(message:types.Message):
    user_id = message.from_user.id
    with open("data/vip_users.json","w") as fl:
        json.dump(user_id,fl)
    await message.answer("Вы добавлены в список расслки")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Тест")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Тест")

async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()

async def regular_posting_kwork(q: Parser):
    with open("data/kwork_data.json") as fl:
        starter_data = json.load(fl)
    
    while True:
        with open("data/vip_users.json","r") as fl:
            users = json.load(fl)
        # TODO: Доделать взаимодействие с юзер ИД и сделать отправку сообщения
        # await q.kwork_parse()
        for user_id in users["users_id"]:
            print(user_id)
        
        # await bot.send_message()
        await asyncio.sleep(60*float(config["Telegram"]["sleeping_post"]))