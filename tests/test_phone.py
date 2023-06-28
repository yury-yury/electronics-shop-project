import pytest

from src.phone import Phone
from src.item import Item


@pytest.fixture
def my_object():
    return Phone(name="test", price=100, quantity=10, number_of_sim=1)


def test_start_init(my_object):
    assert my_object.name == "test"
    assert my_object.price == 100
    assert my_object.quantity == 10
    assert my_object.number_of_sim == 1


def test_calculate_total_price(my_object):
    assert my_object.calculate_total_price() == 1000


def test_apply_discount(my_object):
    Phone.pay_rate = 0.8
    my_object.apply_discount()
    assert my_object.price == 80


def test_name_getter(my_object: Item) -> None:
    assert my_object.name == 'test'


def test_name_setter_true(my_object: Item) -> None:
    my_object.name = 'test_1'
    assert my_object.name == 'test_1'


def test_name_setter_false(my_object: Item) -> None:
    with pytest.raises(Exception):
        my_object.name = 'test_1_test_1'


def test__repr__(my_object):
    assert repr(my_object) == "Phone('test', 100, 10, 1)"


def test__str__(my_object):
    assert str(my_object) == 'test'

def test_add(my_object):
    with pytest.raises(ValueError):
        res = my_object + 10
    assert my_object + Phone('test2', 100, 10, 2) == 20
    assert my_object + Item('test2', 100, 10) == 20