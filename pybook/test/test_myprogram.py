"""This file shows how testing is conducted for a python file."""

try:
    import myprogram
    import pytest
except ImportError, e:
    print e


def test_doubleit():
    """This functions checks if the functions works fine"""
    assert myprogram.doubleit(10) == 20


def test_doubleit_type():
    """This functions test whether the function fails right"""
    with pytest.raises(TypeError):
        myprogram.doubleit("hello")
