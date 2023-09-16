import os
from aiohttp import ClientSession
from dotenv import load_dotenv

async def get_result(from_, to, value):
    load_dotenv()
    API_KEY = os.getenv('API_KEY', None)
    url = f"http://data.fixer.io/api/latest?access_key={API_KEY}&symbols={from_},{to}"
    async with ClientSession() as session:
        async with session.get(url) as data:
            data = await data.json()
    if data["success"]:
        rates = data["rates"]
        exchange_rate = 1 / rates[from_] * rates[to]
        return {'result': exchange_rate * value}

