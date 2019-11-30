import aiohttp
import asyncio
import async_timeout

async def fetch(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()

async def print_page(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        print(html)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([print_page('http://127.0.01:8081'),
                                      print_page('http://127.0.01:8082'),
                                      print_page('http://127.0.01:8083')]))
