import requests
import timeit
import asyncio
from aiohttp import ClientSession
import json


people = {"name": "阿伟", "age": 26, "address": "绍兴", "salary": 999999}

url1 = "http://127.0.0.1:5000/insert"
url2 = "http://127.0.0.1:8000/insert"

def rqt1():
    request1 = requests.post(url1, json=people, headers={"Connection": "close"}).json()

def rqt2():
    request2 = requests.post(url2, json=people, headers={"Connection": "close"}).json()

# async def req3():
#     async with ClientSession() as session:
#         async with session.post(url2, json.dumps(people), headers={"Content-Type": "application/json"}) as resp:

#     request3 = requests.post(url2, json=people, headers={"Connection": "close"}).json()
#     return request3



def rqt3():
    async def post(url, data, headers=None):
        async with ClientSession(headers=headers) as session:
            result = await session.post(url, data=data)
            return await result.json()
    loop = asyncio.get_event_loop()
    for i in range(1000):
        result = loop.run_until_complete(post(url2,json.dumps(people),headers={"Content-Type": "application/json"}))
    loop.close()
    # print(result)


# timer1 = timeit.Timer("rqt1()", setup="from __main__ import rqt1")
# print("Flask API:", timer1.timeit(number=1000))
# timer2 = timeit.Timer("rqt2()", setup="from __main__ import rqt2")
# print("FastAPI API:", timer2.timeit(number=1000))
timer3 = timeit.Timer("rqt3()", setup="from __main__ import rqt3")
print("FastAPI async API:", timer3.timeit(number=1))