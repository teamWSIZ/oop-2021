import asyncio
from asyncio import sleep
from datetime import datetime

from p1.asynchr.drone_control_jobs import log


async def foo(x):
    await sleep(1)
    print(f'x={x}')

async def main(d):
    await foo(10)
    asyncio.create_task(foo(1))
    await sleep(d)

if __name__ == '__main__':
    log('a')
    asyncio.run(main(d=0.5))
    log('done')
