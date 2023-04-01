import pytest

from src.item import Item


@pytest.fixture
def my_object():
    return Item(name="test", price=100, quantity=10)


def test_start_init(my_object):
    assert my_object.name == "test"
    assert my_object.price == 100
    assert my_object.quantity == 10


def test_calculate_total_price(my_object):
    assert my_object.calculate_total_price() == 1000


def test_apply_discount(my_object):
    Item.pay_rate = 0.8
    my_object.apply_discount()
    assert my_object.price == 80