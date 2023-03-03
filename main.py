import asyncio

from util import async_timer


@async_timer()
async def delay(delay_seconds: int) -> int:
    print(f'засыпаю на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)
    print(f'сон в течение {delay_seconds} с закончился')
    return delay_seconds


@async_timer()
async def main():
    print('Создали задачу 1')
    task_one = asyncio.create_task(delay(2))
    print('Создали задачу 2')
    task_two = asyncio.create_task(delay(3))
    result1 = await task_one
    result2 = await task_two

    print(result1, result2)

asyncio.run(main())
