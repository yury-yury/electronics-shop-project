import pytest

from src.keyboard import KeyBoard



@pytest.fixture
def my_object():
    return KeyBoard(name="test", price=100, quantity=10)


def test_start_init(my_object):
    assert my_object.name == "test"
    assert my_object.price == 100
    assert my_object.quantity == 10
    assert my_object.language == 'EN'


def test_language_getter(my_object: KeyBoard) -> None:
    assert my_object.name == 'test'


def test_change_lang(my_object: KeyBoard) -> None:
    assert my_object.language == 'EN'
    my_object.change_lang()
    assert my_object.language == 'RU'
    my_object.change_lang()
    assert my_object.language == 'EN'


def test_set_language_false(my_object: KeyBoard) -> None:
    with pytest.raises(Exception):
        my_object.language = 'CH'
