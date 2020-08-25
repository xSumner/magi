import asyncio
import time
from aiohttp import ClientSession

url = 'http://127.0.0.1:8000/insert'
url1 = "http://127.0.0.1:5000/insert"

now = lambda: time.time()
async def req_get(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            response = await response.read()
            #print(response,type(response))

async def req_post(url):
    async with ClientSession() as session:
        async with session.post(url) as response:
            response = await response.read()

if __name__ == '__main__':
    start = now()
    #方法可以创建一个事件循环,asyncio.BaseEventLoop。
    #协程对象不能直接运行，在注册事件循环的时候，其实是run_until_complete方法将协程包装成为了一个任务（task）对象。
    #所谓task对象是Future类的子类。保存了协程运行后的状态，用于未来获取协程的结果
    loop = asyncio.get_event_loop()
    #需要处理的任务
    tasks = [asyncio.ensure_future(req_post(url)) for i in range(1000)]
    #tasks = [loop.create_task(req_get(url)) for i in range(512)] 确定参数是协程的时候可以用这个
    #将协程注册到事件循环，并启动事件循环
    #loop.run_until_complete(asyncio.gather(*tasks))
    loop.run_until_complete(asyncio.wait(tasks))
    for task in tasks:
        print(task)
        print('Task ret: ', task.result())
    print('TIME: ', now() - start)