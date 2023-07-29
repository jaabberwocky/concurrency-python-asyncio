import asyncio
import aiohttp
from aiohttp import ClientSession
from util import async_timed


@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    # simulating a very slow request which will be timed-out
    if url == "https://www.youtube.com":
        print("sleeping...")
        await asyncio.sleep(10)
    async with session.get(url) as result:
        return (url, result.status)


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        urls = ['https://www.example.com',
                'https://www.google.com', 'https://www.yahoo.com', 'https://www.youtube.com']
        tasks = []
        for url in urls:
            print(f"creating task for {url}")
            tasks.append(asyncio.create_task(fetch_status(session, url)))

        for task in tasks:
            try:
                url, status = await asyncio.wait_for(task, 2)
            except asyncio.exceptions.TimeoutError:
                print(f"Timeout!")
            print(f'Status for {url} was {status}')

if __name__ == '__main__':
    asyncio.run(main())
