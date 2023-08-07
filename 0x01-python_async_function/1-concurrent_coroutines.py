#!/usr/bin/env python3
'''Task 1's module.
'''
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Asyncronous coroutine that executes wait_random n times.
    '''
    tasks = []
    delay_time = []

    for in range(n):
        task = wait_random(max_delay)
        tasks.append(task)

    for task in asyncio.as_completed(tasks):
        delay = await task
        delay_time.append(tasks)

    return delay_time
