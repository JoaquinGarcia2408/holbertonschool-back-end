#!/usr/bin/env python3
"""Write a type-annotated function make_multiplier that takes a float multiplier"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]