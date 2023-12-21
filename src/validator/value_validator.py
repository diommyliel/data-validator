'''
validators to be applied to values in column

Ex: is_greater_than, is_in_value_set, ...
'''
import typing as t


def is_greater_than(a: float):
    return lambda x: x > a


def is_in_value_set(s: t.Set):
    return lambda x: x in s
