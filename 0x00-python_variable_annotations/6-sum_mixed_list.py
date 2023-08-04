#!/usr/bin/env python3
'''Python module for mixed list of integers and loats.
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Function that computes the sum of a list of
       integers and floating-point numbers.
    '''
    return float(sum(mxd_lst))
