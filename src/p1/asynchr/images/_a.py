
import asyncio
from asyncio import sleep
from datetime import datetime


def ts():
    return datetime.now().timestamp()

def goo(x):
    # await sleep(1)
    print(f'goo x={x}')

async def foo(x):
    await sleep(1)
    print(f'x={x}')
    await sleep(2)


async def main():
 # await goo(5)
     await foo(10)

t = ts()
asyncio.run(main())
print(f'{ts()-t:.3f}s')

