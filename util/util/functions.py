import functools
import time
from typing import Callable, Any
import asyncio
from aiohttp import ClientSession


def async_timed():
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f'starting {func} with args {args} {kwargs}')
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f'finished {func} in {total:.4f} second(s)')

        return wrapped

    return wrapper


async def delay(seconds: int) -> None:
    print(f'delaying {seconds} second(s)')
    await asyncio.sleep(seconds)


async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url) as result:
        return (url, result.status)


def delay_if_url(specified_url: str):
    def decorator(func):
        async def wrapper(*args, **kwargs):
            session, url = args[0], args[1]
            if url == specified_url:
                await asyncio.sleep(10)
            return await func(session, url)
        return wrapper
    return decorator
