#!/usr/bin/env python3
"""
   Python asynchronous module that import List and return
   list of delas in a sorted manner.
"""

import asyncio
from typing import List


wait_random = __import__("0-basic_async_syntax.py").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Asynchronous function that spawn wait_random n times
        with the specified max_delay
    """
    delay_time = await asyncio.gather(
            *tuple(map(lamda _: wait_random(max_delay), range(n))))
    return sorted(delay_time)
