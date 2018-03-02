import myprogram
import pytest


def test_doubleit():
    """This functions checks if the functions works fine"""
    assert myprogram.doubleit(10) == 20


def test_doubleit_type():
    """This functions test whether the function fails right"""
    with pytest.raises(TypeError):
        myprogram.doubleit("hello")
