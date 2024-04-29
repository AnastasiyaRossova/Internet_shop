from abc import ABC, abstractmethod


class Abstract_Product(ABC):
    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def price(self):
        pass

class Repr_Mixin:
    def __repr__(self):
        return f"Создан объект под именем {self._name}: {self._description}"


class Category(Repr_Mixin):
    all_total_category = 0
    all_total_unique_product = 0
    name: str
    description: str
    goods: list

    def __init__(self, name, description, goods):
        self._name = name
        self._description = description
        self.__goods = goods
        self._all_total_category = 1
        Category.all_total_unique_product += 1
        print(repr(self))

    def add_goods(self, good):
        """принимает товар и добавляет этот товар в приватный список"""
        if not isinstance(type(good), Product) and not issubclass(type(good), Product):
            raise ValueError
        self.__goods.append(good)

    @property
    def goods(self):
        """Геттер, который выводит список товаров в формате: продукт, цена, остаток- шт."""
        return self.__goods

    def __str__(self):
        "Строка, отображения 'Наименование продукта, кол-во пна складе: ** шт.'"
        return f'{self._name}, количество продуктов на складе: {self.__len__()} шт.'

    def __len__(self):
        "подсчет кол-ва продуктов в категории"
        total_goods = len(self.__goods)
        return total_goods

    def calculate_avg_price(self):
        try:
            total_price = 0
            total_quantity = 0
            for product in self.__goods:
                total_price += product.price * product._quantity
                total_quantity += product._quantity
            return total_price / total_quantity
        except ZeroDivisionError:
            return 0


class Product(Repr_Mixin, Abstract_Product):
    name: str
    description: str
    quantity: int
    price: float

    def __init__(self, name, description, quantity, price):
        self._name = name
        self._description = description
        self._quantity = quantity
        self._price = price
        print(repr(self))

    def __str__(self):
        return f'{self._name}, {self._price} руб. Остаток: {self.__len__()} шт.'

    def __len__(self):
        return self._quantity

    @classmethod
    def create(cls, name, description, quantity, price, goods):
        """класс-метод, который создает товар и возвращает объект, который можно добавлять в список товаров.
        Для данного метода реализуйте проверку наличия такого же товара,
        схожего по имени. В случае если товар уже существует,
        необходимо сложить количество в наличии старого товара и нового.
        При конфликте цен выбрать ту, которая является более высокой.
        Для этого можно в метод передать список товаров, в котором нужно искать дубликаты."""
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        for good in goods:
            if good.name.lower() == name.lower():
                good.quantity += quantity
                good.price = max(good.price, price)
                return good
        return cls(name, price, quantity)  #?? как в этом методе сравнить еще и описание товара? Например в списке есть туфли, и добавляют еще туфли- но они могут быть на разном каблуке.

    @property
    def price(self):
        """Для класса Product геттеры для атрибута цены.
        """
        return self._price

    @price.setter
    def price(self, new_price) -> float:
        """для класса Product сеттер для атрибута цены.
            В случае если цена равна или ниже нуля, выведите сообщение в консоль, что цена введена некорректная,
            при этом новую цену устанавливать не нужно.
            В случае если цена товара понижается, добавьте логику подтверждения пользователем вручную через ввод
            y (значит yes) или n (значит no) для согласия понизить цену или для отмены действия соответственно."""
        if new_price <= 0:
            print("Цена введена некорректная")
        elif self._price < new_price:
            confirmation = input("Хотите зафиксировать пониженную цену? (y/n)")
            if confirmation == "y":
                self._price = new_price
            else:
                print("Отмена действия")
        else:
            self._price = new_price

    def __add__(self, other):
        """добавляем возможность получения общей суммы товара на складе, таким образом,
        чтобы результат выполнения сложения двух продуктов
         был сложением сумм, умноженных на количество этих продуктов на складе.
        ((кол-во товара 1 * цену товара 1) + (кол-во товара 2 * цену товара 2))"""
        if type(self) != type(other):
            raise TypeError("Классы должны совпадать")
        return (self._price * self._quantity
                + other._price * other._quantity)


class CategoryIterator:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def __iter__(self):
        self.current_value = -1
        return self

    def __next__(self):
        self.current_value += 1
        if self.current_value < len(self.product):
            return self.products[self.current_value]
        else:
            raise StopIteration


class Smartphone(Product):
    def __init__(self, name, description, quantity,
                 price, perf, model, memory, color):
        super().__init__(name, description, quantity, price)
        self._performance = perf
        self._model = model
        self._memory = memory
        self._color = color

    def __str__(self):
        super().__str__()

    def __len__(self):
        super().__len__()

    @classmethod
    def create(cls, name, description, quantity, price, goods):
        super().create(name, description, quantity, price, goods)

    @property
    def price(self):
        self._price

    @price.setter
    def price(self, new_price):
        super().price(new_price)

    def __add__(self, other):
        super().__add__(other)


class Grass(Product):
    def __init__(self, name, description, quantity, price, country, period, color):
        super().__init__(name, description, quantity, price)
        self.country = country
        self.period = period
        self.color = color

    def __str__(self):
        super().__str__()

    def __len__(self):
        super().__len__()

    @classmethod
    def create(cls, name, description, quantity, price, goods):
        super().create(name, description, quantity, price, goods)

    @property
    def price(self):
        super().price()

    @price.setter
    def price(self, new_price):
        super().price(new_price)

    def __add__(self, other):
        super().__add__(other)


# category_iterator = CategoryIterator([products])
# Перебор товаров с помощью цикла for
# for product in category_iterator:
    #print(product)
