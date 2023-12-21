'''
validators to be applied to values in column

Ex: is_greater_than, is_in_value_set, ...
'''
import typing as t
from polars import Series


T = t.Callable[[Series], Series]


def is_greater_than(a: float) -> T:
    return lambda x: x > a


def is_in_value_set(s: t.Set) -> T:
    return lambda x: x.is_in(s)
