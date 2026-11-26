# Задание 2. Проверяем чётность 🔢
from numbers_utils import is_even

def test_positive_4():
    assert is_even(4) is True

def test_positive_7():
    assert is_even(7) is False

def test_positive_0():
    assert is_even(0) is True

def test_positive_2():
    assert is_even(2) is True

