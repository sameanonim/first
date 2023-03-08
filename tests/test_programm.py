import pytest
from programm import Item

@pytest.fixture
def item():
    return Item("Айфон", 10000, 9)

##тестирование

def test_instantiate_from_csv():
    items = Item.instantiate_from_csv()
    assert len(items) == 5
    assert items[0].name == "Смартфон"
    assert items[1].price == 1000.0
    assert items[2].quantity == 5.0

def test_is_integer():
    assert Item.is_integer(5) == True
    assert Item.is_integer(5.5) == False
    assert Item.is_integer("5") == False
    assert Item.is_integer(0) == True
    assert Item.is_integer(-10) == True

def test_repr():
    item = Item("Item 1", 10, 5)
    assert repr(item) == "Item('Item 1', 10, 5)"

def test_str():
    item = Item("Item 1", 10, 5)
    assert str(item) == "Item 1"