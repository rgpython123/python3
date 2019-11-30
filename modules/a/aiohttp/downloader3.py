import aiohttp
import asyncio
import async_timeout
import os

# get content and write it to file
def write_to_file(filename, content):
  with open(filename, 'wb') as f:
    f.write(content)

async def fetch(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.read()

async def download_file(url):
    async with aiohttp.ClientSession() as session:
        content = await fetch(session, url)
        basepath, filename = os.path.split(url)
  
        write_to_file(filename, content)

images = [ 'http://127.0.0.1/mp3/Meditation1.mp3', 'http://127.0.0.1/mp3/Meditation2.mp3', 'http://127.0.0.1/mp3/Meditation3.mp3' ]

coroutines = [download_file(url) for url in images]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(coroutines))
loop.close()
