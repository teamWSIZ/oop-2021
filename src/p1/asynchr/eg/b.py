import time
from asyncio import sleep

from p1.asynchr.drone_control_jobs import log

import asyncio
import aiohttp
import requests

URL = 'https://wdauth.wsi.edu.pl/status'

async def afoo():
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as resp:
            d = await resp.json()
            await sleep(1)
            log(d)
    log('afoo - done')

async def foo():
    r = requests.get(URL)
    time.sleep(1)
    log(r.json())
    log('foo - done')

async def main():
    await afoo()
    for _ in range(10):
        asyncio.create_task(afoo())
        asyncio.create_task(foo())
    await sleep(2)
    log('program -- done')

if __name__ == '__main__':
    asyncio.run(main())


