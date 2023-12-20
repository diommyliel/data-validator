'''
validators to be applied to columns as a whole

Ex: has_null, is_int, ...
'''
import polars as pl


def has_null(x: pl.Series) -> bool:
    return x.null_count() > 0


def is_int(x: pl.Series) -> bool:
    t = x.dtype
    return t in pl.INTEGER_DTYPES
