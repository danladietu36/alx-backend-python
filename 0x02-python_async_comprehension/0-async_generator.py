#!/usr/bin/env python3
"""
   Module for a coroutine that takes no arguments.
   The coroutine will loop 10 times,each time asynchronously
   wait 1 second, then yield a random number
   between 0 and 10. Use the random module.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Function that iterate 10 times. """
    for i in range(10):
        await async.sleep(1)
        yield random.random() * 10
