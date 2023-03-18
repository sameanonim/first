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

class Phone(Item):
    number_of_sim = []

    '''Класс для телефона'''
    def __init__(self, name: str, price: int, quantity: int, number_of_sim: int):
        '''Инициализирует конструктор класса'''
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __str__(self):
        '''Возвращает строковое представлен''' 
        return f'{self.name}.'

    def __repr__(self):
        '''Возвращает код вызова класса'''
        return f'{self.name} - {self.price}, {self.quantity}, {self.number_of_sim}'

    def __add__(self, other):
        '''Сложение экземпляров класса Phone и Item по количеству товара в магазине.'''
        if isinstance(other, Phone):
            return Phone(self.name + ' & ' + other.name, self.price + other.price, self.quantity + other.quantity, self.number_of_sim)
        elif isinstance(other, Item):
            return Item(self.name + ' & ' + other.name, self.price + other.price, self.quantity + other.quantity)
        else:
            raise TypeError("Нельзя складывать объекты других классов с Phone или Item.")
        
    @property
    def number_of_sim(self) -> int:
        '''Возвращает количество физических SIM-карт'''
        return self.__number_of_sim
    
    @number_of_sim.setter
    def number_of_sim(self, value: int):
        '''Проверяет, чтобы количество физических SIM-карт было целым числом больше нуля,
            иначе возвращает ошибку'''
        if value <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        else:
            self.__number_of_sim = value

class KeyboardLanguageMixin:
    def __init__(self, language="EN"):
        self._language = language

    def change_lang(self):
        '''Меняет язык клавиатуры на английский или русский'''
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'

class Keyboard(Item, KeyboardLanguageMixin):
    '''Класс для клавиатуры'''
    def __init__(self, name: str, price: int, quantity: int, language="EN"):
        '''Инициализирует конструктор класса'''
        super().__init__(name, price, quantity)
        KeyboardLanguageMixin.__init__(self, language)

    def __str__(self):
        '''Возвращает информацию пользователю об экземпляре класса'''
        return f"{self.name}"

    @property
    def language(self):
        '''Возвращает язык клавиатуры'''
        return self._language

    @language.setter
    def language(self, new_lang: str):
        '''Сеттер для языка раскладки клавиатуры'''
        if new_lang not in ["EN", "RU"]:
            raise AttributeError("property 'language' of 'KeyBoard' object has no setter")
        else:
            self._language = new_lang