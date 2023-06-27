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


def test_name_getter(my_object: Item) -> None:
    assert my_object.name == 'test'


def test_name_setter_true(my_object: Item) -> None:
    my_object.name = 'test_1'
    assert my_object.name == 'test_1'


def test_name_setter_false(my_object: Item) -> None:
    with pytest.raises(Exception):
        my_object.name = 'test_1_test_1'


def test_instantiate_from_csv() -> None:
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    assert Item.all[0].name == 'Смартфон'

def test_string_to_number_true() -> None:
    assert Item.string_to_number('10.00') == 10
    assert Item.string_to_number('123123123') == 123123123

def test_string_to_number_false():
    with pytest.raises(Exception):
        Item.string_to_number('qwerty')