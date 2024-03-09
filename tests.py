import pytest
from Classes import Category, Product


@pytest.fixture()
def category_object():
    return Category('jive dance', 'Latin American',  ['shoes', 'jazz bands'])


@pytest.fixture()
def product_object():
    return Product('shoes', 'low heel', 10, 3500.00)


def test_init_category(category_object):
    assert category_object.name == 'Folk dance'
    assert category_object.description == 'Latin American'
    assert category_object.goods == ['shoes', 'jazz bands']


def test_init_product(product_object):
    assert product_object.name == 'shoes'
    assert product_object.description == 'low heel'
    assert product_object.price == 3500.00
    assert product_object.quantity_in_stock == 10
    assert product_object.total_categories == 0
    assert product_object.total_unique_products == 0