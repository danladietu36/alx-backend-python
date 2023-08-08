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
    n = 0
    while n < 10:
        await asyncio.sleep(1)
        yield random.random() * 10
        n += n
