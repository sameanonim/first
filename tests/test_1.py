import pytest
import csv

class Item:
    pay_rate = 1 #уровень цены на товар
    all = []


    def __init__(self, name, price, quantity):
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)


    def __repr__(self) -> str:
        '''Выводит полную информацию экземпляра класса'''
        return f"Item('{self.__name}', {self.price}, {self.quantity})"


    def __str__(self) -> str:
        '''Выводит информацию пользователю об экзмпляре класса '''
        return f"{self.__name}"

    @property
    def name(self) -> str:
        '''Возваращает наименование товара'''
        return self.__name

    @name.setter
    def name(self, value: str):
        '''Проверяет, чтобы длина наименования товара не была более 10 символов,
            иначе возвращает ошибку'''
        if len(value) > 10:
            raise Exception ("Длина наименования товара превышает 10 символов.")
        else:
            self.__name = value


    def calculate_total_price(self):
        '''Вычисляет общую стоимость категории товара в магазине'''
        self.total_price = self.price * self.quantity * self.pay_rate
        return self.total_price


    def apply_discount(self):
        '''Вычисляет актуальную стоимость товара'''
        self.price = self.price * self.pay_rate
        return self.price


    @classmethod
    def instantiate_from_csv(cls):
        '''Считывает данные из csv-файла и создает экземпляры класса,
        инициализируя их данными из файла'''
        items = []
        with open('items.csv') as file:
            data = csv.DictReader(file)
            for i in data:
                if cls.is_integer(i['price']):
                    price = int(float(i['price']))
                else:
                    price = float(i['price'])
                if cls.is_integer(i['quantity']):
                    quantity = int(float(i['quantity']))
                else:
                    quantity = float(i['quantity'])
                items.append(cls(i['name'], price, quantity))
        return items

    @staticmethod
    def is_integer(x):
        '''Возвращает True, если число целое'''
        isInt = int(x) == x
        return isInt

##тестирование

def test_name_length():
    with pytest.raises(ValueError):
        p = Item("This name is too long", 10, 5)

def test_total_cost():
    p = Item("Test Product", 10, 5)
    assert p.total_cost() == 50

def test_apply_discount():
    p = Item("Test Product", 10, 5)
    p.apply_discount()
    assert p.price == 8.5

def test_instantiate_from_csv():
    items = Item.instantiate_from_csv()
    assert len(items) == 3
    assert items[0].name == "Product 1"
    assert items[0].price == 10.0
    assert items[0].quantity == 5
    assert items[1].name == "Product 2"
    assert items[1].price == 20.0
    assert items[1].quantity == 10
    assert items[2].name == "Product 3"
    assert items[2].price == 30.0
    assert items[2].quantity == 15