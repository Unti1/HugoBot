from settings import *
from tools import *

if __name__ == '__main__':
    q = Parser()
    loop = asyncio.get_event_loop()
    loop.create_task(regular_posting_kwork(q))
    executor.start_polling(dp, loop = loop,on_shutdown=shutdown)
    