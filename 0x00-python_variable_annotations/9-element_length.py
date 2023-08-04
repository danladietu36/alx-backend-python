#!/usr/bin/env python3
'''Python annotation module
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Python function that returns a list of tuples 
       containing the element and its length.
    '''
    return [(element, len(element)) for element in lst]
