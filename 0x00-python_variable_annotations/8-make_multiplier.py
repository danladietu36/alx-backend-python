#!/usr/bin/env python3
'''Python module for creating a multiplier function.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Python function that creates a multiplier function.
    '''
    return lambda x: x * multiplier
