
class Category:
    all_total_category = 0
    all_total_unique_product = 0
    name: str
    description: str
    goods: list

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.__goods = goods
        self.all_total_category = 1
        Category.all_total_unique_product += 1

    def add_goods(self, good):
        """принимает товар и добавляет этот товар в приватный список"""
        self.__goods.append(good)

    @property
    def goods(self):
        """Геттер, который выводит список товаров в формате: продукт, цена, остаток- шт."""
        return [f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.' for good in self.__goods]

class Product:
    name: str
    description: str
    quantity: int
    price: float

    def __init__(self, name, description, quantity, price):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price

    @classmethod
    def create(cls, name, description, quantity, price, goods):
        """класс-метод, который создает товар и возвращает объект, который можно добавлять в список товаров.
        Для данного метода реализуйте проверку наличия такого же товара,
        схожего по имени. В случае если товар уже существует,
        необходимо сложить количество в наличии старого товара и нового.
        При конфликте цен выбрать ту, которая является более высокой.
        Для этого можно в метод передать список товаров, в котором нужно искать дубликаты."""
        for good in goods:
            if good.name.lower() == name.lower():
                good.quantity += quantity
                good.price = max(good.price, price)
                return good
        return cls(name, price, quantity)  #как в этом методе сравнить еще и описание товара? Например в списке есть туфли, и добавляют еще туфли- но они могут быть на разном каблуке.

    @property
    def price(self):
        """Для класса Product геттеры для атрибута цены.
        """
        return self.price

    @price.setter
    def price(self, new_price) -> float:
        """для класса Product сеттер для атрибута цены.
            В случае если цена равна или ниже нуля, выведите сообщение в консоль, что цена введена некорректная,
            при этом новую цену устанавливать не нужно.
            В случае если цена товара понижается, добавьте логику подтверждения пользователем вручную через ввод
            y (значит yes) или n (значит no) для согласия понизить цену или для отмены действия соответственно."""
        if new_price <= 0:
            print("Цена введена некорректная")
        elif self.price < new_price:
            confirmation = input("Хотите зафиксировать пониженную цену? (y/n)")
            if confirmation == "y":
                self.price = new_price
            else:
                print("Отмена действия")
        else:
            self.price = new_price




