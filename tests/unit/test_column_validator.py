import polars as pl

import validator.column_validator as f


def test_has_null_true():
    null_serie = pl.Series([None])
    assert f.has_null(null_serie)


def test_has_null_false():
    not_null_serie = pl.Series([0])
    assert not f.has_null(not_null_serie)


def test_is_int_true():
    int_serie = pl.Series([1, 2, 3])
    assert f.is_int(int_serie)


def test_is_int_false():
    not_int_serie = pl.Series([1, '2', 3])
    assert not f.is_int(not_int_serie)
