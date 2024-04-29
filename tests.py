import pytest
from main import Category, Product, Smartphone, Grass


@pytest.fixture()
def category_object():
    return Category('Folk dance', 'Russian',  ['shoes', 'boots'])


@pytest.fixture()
def product_object():
    return Product('shoes', 'low heel', 10, 3500.00)

@pytest.fixture()
def smartphone_object():
    return Smartphone('iphone', 'description',
                      1, 100, 'good', '15 pro',
                      5, 'silver')

@pytest.fixture()
def grass_object():
    return Grass('grass', 'description', 100, 5,
                 'Russia', 7, 'red')

def test_init_category(category_object):
    assert category_object._name == 'Folk dance'
    assert category_object._description == 'Russian'
    assert category_object.goods == ['shoes', 'boots']


def test_init_product(product_object):
    assert product_object._name == 'shoes'
    assert product_object._description == 'low heel'
    assert product_object.price == 3500.00


def test_init_smartphone(smartphone_object):
    assert smartphone_object._name == 'iphone'
    assert smartphone_object._description == 'description'
    assert smartphone_object._color == 'silver'
    assert smartphone_object._price == 100
    assert smartphone_object._quantity == 1


def test_add_products(product_object):
    total = product_object + product_object
    assert total == 70000.0


def test_add_goods(category_object, smartphone_object):
    category_object.add_goods(smartphone_object)
    assert category_object.goods == ['shoes', 'boots', smartphone_object]