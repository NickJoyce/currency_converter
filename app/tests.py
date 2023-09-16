import asyncio
from aiohttp import ClientSession


async def get_status(url: str):
    async with ClientSession() as session:
        async with session.get(url) as data:
            print(f"Status code: {data.status}")


async def make_request(session:ClientSession, url: str):
    async with session.get(url) as data:
        return await data.json()

async def get_result(url):
    async with ClientSession() as session:
        result = await make_request(session, url)
        print(f"Result: {result}")



async def main():
    from_, to, value  = 'USD', 'RUB', 1

    url = f'http://127.0.0.1:8000/api/rates?from={from_}&to={to}&value={value}'

    t1 = asyncio.create_task(get_status(url))
    t2 = asyncio.create_task(get_result(url))

    await t1
    await t2

asyncio.run(main())