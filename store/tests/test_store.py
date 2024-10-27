import pytest
import io
from unittest.mock import patch

from store.store import Product, Order


class MockProduct:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def update_stock(self, quantity):
        self.stock += quantity


def test_update_stock_positive_quantity():
    """Проверяет, что метод update_stock увеличивает количество товара на складе
    при добавлении положительного количества.
    """
    product = Product("Телефон", 1000, 50)
    product.update_stock(10)
    assert product.stock == 60


def test_update_stock_negative_quantity():
    """Проверяет, что метод update_stock не уменьшает количество товара на складе
    ниже нуля и выводит сообщение об ошибке при попытке удалить больше товара, чем есть.
    """
    product = Product("Телефон", 1000, 50)
    try:
        product.update_stock(-60)
    except Exception as e:
        pass
    assert product.stock == 50


def test_update_stock_zero_quantity():
    """Проверяет, что метод update_stock не меняет количество товара при добавлении нуля."""
    product = Product("Телефон", 1000, 50)
    product.update_stock(0)
    assert product.stock == 50


def test_add_product_enough_stock():
    """Проверяет, что метод add_product добавляет товар в заказ,
    если товара достаточно на складе.
    """
    order = Order()
    product = Product("Телефон", 1000, 50)
    order.add_product(product, 10)
    assert order.products[product] == 10
    assert product.stock == 40


def test_add_product_not_enough_stock():
    """Проверяет, что метод add_product не добавляет товар в заказ,
    если товара недостаточно на складе, и выводит сообщение об ошибке.
    """
    order = Order()
    product = Product("Телефон", 1000, 50)
    order.add_product(product, 60)
    assert product.stock == 50
    assert product not in order.products


def test_add_product_existing_product():
    """Проверяет, что метод add_product увеличивает количество товара в заказе,
    если товар уже есть в заказе.
    """
    order = Order()
    product = Product("Телефон", 1000, 50)
    order.add_product(product, 5)
    order.add_product(product, 3)
    assert order.products[product] == 8
    assert product.stock == 42


def test_add_product_zero_quantity():
    """Проверяет, что метод add_product не добавляет товар в заказ,
    если количество равно нулю.
    """
    order = Order()
    product = Product("Телефон", 1000, 50)
    order.add_product(product, 0)
    assert product.stock == 50


def test_add_product_negative_quantity():
    """Проверяет, что метод add_product не добавляет товар в заказ,
    если количество отрицательное, и ничего не делает.
    """
    order = Order()
    product = Product("Телефон", 1000, 50)
    order.add_product(product, -5)
    assert product.stock == 50


def test_calculate_total_empty_order():
    """Проверяет, что метод calculate_total возвращает 0 для пустого заказа."""
    order = Order()
    assert order.calculate_total() == 0


def test_calculate_total_one_product():
    """Проверяет, что метод calculate_total правильно вычисляет общую стоимость
    заказа с одним товаром.
    """
    order = Order()
    product = Product("Телефон", 1000, 50)
    order.add_product(product, 2)
    assert order.calculate_total() == 2000


def test_calculate_total_multiple_products():
    """Проверяет, что метод calculate_total правильно вычисляет общую стоимость
    заказа с несколькими товарами.
    """
    order = Order()
    product1 = Product("Телефон", 1000, 50)
    product2 = Product("Наушники", 500, 10)
    order.add_product(product1, 2)
    order.add_product(product2, 3)
    assert order.calculate_total() == 3500


def test_products_leave_empty_order():
    """Проверяет, что метод products_leave выводит сообщение о пустой корзине
    для пустого заказа.
    """
    order = Order()
    with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
        order.products_leave()
        assert mock_stdout.getvalue() == "В корзине находятся следующие товары:\n\n"


def test_products_leave_one_product():
    """Проверяет, что метод products_leave выводит информацию о товаре в корзине
    для заказа с одним товаром.
    """
    order = Order()
    product = Product("Телефон", 1000, 50)
    order.add_product(product, 2)
    with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
        order.products_leave()
        assert (
            mock_stdout.getvalue()
            == "В корзине находятся следующие товары:\n  Телефон: 2\n\n"
        )


def test_products_leave_multiple_products():
    """Проверяет, что метод products_leave выводит информацию о товарах в корзине
    для заказа с несколькими товарами.
    """
    order = Order()
    product1 = Product("Телефон", 1000, 50)
    product2 = Product("Наушники", 500, 10)
    order.add_product(product1, 2)
    order.add_product(product2, 3)
    with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
        order.products_leave()
        assert (
            mock_stdout.getvalue()
            == "В корзине находятся следующие товары:\n  Телефон: 2\n  Наушники: 3\n\n"
        )


def test_remove_product_enough_quantity():
    """Проверяет, что метод remove_product удаляет указанное количество товара из заказа,
    если товара достаточно.
    """
    order = Order()
    product = Product("Телефон", 1000, 50)
    order.add_product(product, 5)
    with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
        order.remove_product(product, 2)
        assert order.products[product] == 3
        assert (
            mock_stdout.getvalue()
            == "Вы удалили 2 шт. товара Телефон\nВ корзине находятся следующие товары:\n  Телефон: 3\n\n"
        )


def test_remove_product_not_enough_quantity():
    """Проверяет, что метод remove_product не удаляет товар из заказа,
    если товара недостаточно, и выводит сообщение об ошибке.
    """
    order = Order()
    product = Product("Телефон", 1000, 50)
    order.add_product(product, 5)
    with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
        try:
            order.remove_product(product, 8)
        except Exception as e:
            print(e)
        assert (
            mock_stdout.getvalue()
            == "Вы не можете убрать из заказа товаров больше, чем в него положили. В заказе 5 шт. товара Телефон\n\n"
        )
        assert order.products[product] == 5


def test_remove_product_remove_all():
    """Проверяет, что метод remove_product удаляет товар из заказа,
    если удаляется все количество товара, и удаляет товар из словаря products.
    """
    order = Order()
    product = Product("Телефон", 1000, 50)
    order.add_product(product, 5)
    with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
        order.remove_product(product, 5)
        assert product not in order.products
        assert (
            mock_stdout.getvalue()
            == "Вы удалили 5 шт. товара Телефон\nВ корзине находятся следующие товары:\n\n"
        )


def test_add_product_one_product():
    """Проверяет, что метод add_product правильно добавляет товар в заказ,
    и количество товаров в заказе увеличивается на один после добавления."""
    order = Order()
    product = Product("Телефон", 1500, 100)
    order.add_product(product, 23)
    assert product in order.products
    assert len(order.products) == 1


def test_add_product_few_products():
    """Проверяет, что метод add_product правильно добавляет товары в заказ,
    и количество товаров в заказе увеличивается на один после добавления."""
    order = Order()
    product1 = Product("Телефон", 1500, 100)
    product2 = Product("Наушники", 1000, 100)
    order.add_product(product1, 3)
    order.add_product(product2, 5)
    assert product1 in order.products
    assert product2 in order.products
    assert len(order.products) == 2


def test_add_product_add_empty():
    """Проверяет, что метод add_product правильно добавляет товар в заказ,
    и количество товаров в заказе увеличивается на один после добавления."""
    order = Order()
    product = Product("Телефон", 1500, 100)
    order.add_product(product, 0)
    assert product not in order.products
    assert len(order.products) == 0
