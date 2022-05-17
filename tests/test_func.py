"""Test cases for the func module."""
from baslertwo import sqrt


def test_func() -> None:
    """Sqrt test."""
    assert sqrt(2) == 4
    assert sqrt(-3) == 9
