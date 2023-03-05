import pytest
##тестируемый код

class Product:
    # атрибуты класса
    discount = 0.85 # уровень цен с учетом скидки
    instances = [] # список экземпляров класса

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.__class__.instances.append(self) # добавляем экземпляр в список

    def total_cost(self):
        return self.price * self.quantity # общая стоимость товара в магазине

    def apply_discount(self):
        self.price *= self.discount # применяем скидку к цене товара

##тестирование

def test_init():
    p = Product("test", 10, 2)
    assert p.name == "test"
    assert p.price == 10
    assert p.quantity == 2

def test_total_cost():
    p = Product("test", 10, 2)
    assert p.total_cost() == 20

def test_apply_discount():
    p = Product("test", 10, 2)
    p.apply_discount()
    assert p.price == 8.5

def test_instances():
    p1 = Product("test1", 10, 2)
    p2 = Product("test2", 5, 3)
    assert p1 in Product.instances
    assert p2 in Product.instances