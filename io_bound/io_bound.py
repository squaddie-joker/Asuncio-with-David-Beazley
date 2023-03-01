import asyncio


async def delay(seconds: int = 1) -> None:
    print('Засыпаю на {0} секунд.'.format(str(seconds)))
    await asyncio.sleep(seconds)
    print('Сон в течение {0} секунд завершен.'.format(str(seconds)))
