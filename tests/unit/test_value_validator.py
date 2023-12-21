import polars as pl

import validator.value_validator as f


def test_is_greater_than():
    ser = pl.Series([1, 2, 3])
    func = f.is_greater_than(1)
    res = func(ser)

    assert not res[0]
    assert res[1]
    assert res[2]


def test_is_in_value_set():
    ser = pl.Series(['Red', 'green', 'Yellow'])
    func = f.is_in_value_set(('Red', 'Green', 'Blue'))
    res = func(ser)

    assert res[0]
    assert not res[1]
    assert not res[2]