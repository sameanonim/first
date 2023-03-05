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