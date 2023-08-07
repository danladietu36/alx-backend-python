#!/usr/bin/env python3
"""
   Python asynchronous module that takes in an integer argument
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Asynchronous function that waits for a random delay
    """
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
