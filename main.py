from settings import *
from tools import *

async def main():
    global q
    q = Parser()
    await q.__init__()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # loop.create_task()
    # executor.start_polling(dp, on_shutdown=shutdown)
    
    loop.run_until_complete(main())
    # print(q.kwork_data)
    