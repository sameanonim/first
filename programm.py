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

    @classmethod
    def instantiate_from_csv(cls):
        '''Считывает данные из csv-файла'''
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
        '''Возвращает True, если целое'''
        isInt = int(x) == x
        return isInt