
class Category:
    all_total_category = 0
    all_total_unique_product = 0
    name: str
    description: str
    goods: list

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.goods = goods
        self.all_total_category = 1
        Category.all_total_unique_product += 1


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
