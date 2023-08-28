#!/usr/bin/env python3
"""Write a type-annotated function to_kv that takes a string k and an int OR float v"""
from typing import List, Union


def to_kv(k : str, v : Union[float, int]) -> tuple[str, float]:
    "arguments and returns a tuple"
    return (k, float(v ** 2))