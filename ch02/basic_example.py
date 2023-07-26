import argparse
import asyncio
import random
from utils import async_timed


@async_timed()
async def add_num(num1: int, num2: int) -> int:
    # dont use time.sleep as it blocks all execution
    await asyncio.sleep(random.randint(0, 3))
    return num1 + num2


async def print_add_num(num1: int, num2: int) -> None:
    result = await add_num(num1, num2)
    print(f'{num1} + {num2} = {result}')


async def main():
    random.seed(42)
    tasks = []

    for _ in range(args.num_iterations):
        # Tasks are wrappers around a coroutine that schedule a coroutine
        # to run on the event loop as soon as possible
        task = asyncio.create_task(print_add_num(
            random.randint(0, 100), random.randint(0, 100)))
        tasks.append(task)

    for task in tasks:
        await task


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('num_iterations', type=int, default=10,
                        help='an integer for the accumulator')

    args = parser.parse_args()
    print(f"Runinng with {args.num_iterations} iterations...")
    asyncio.run(main())
