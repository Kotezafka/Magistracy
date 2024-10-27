from __future__ import annotations
from typing import NoReturn

__all__ = ["Product", "Order", "Store"]


class Product:
    def __init__(self, name: str, price: float, stock: int) -> NoReturn:
        self.name = name
        self.price = price
        self.stock = stock

    def __hash__(self) -> int:
        return hash(self.name)

    def update_stock(self, quantity: int) -> int:
        if self.stock + quantity < 0:
            raise Exception(
                f"Товар {self.name} нет в количестве {quantity*(-1)} шт. Для покупки доступно {self.stock} шт.\n"
            )
        else:
            self.stock += quantity
            print(
                f"Количество товаров {self.name} на складе изменилось. Оставшееся кол-во: {self.stock}\n"
            )
        return self.stock


class Order:
    def __init__(self) -> NoReturn:
        self.products = {}

    def add_product(self, product: Product, quantity: int) -> NoReturn:
        if quantity > product.stock:
            print(
                f"Недостаточно товара на складе. {product.name}: доступно {product.stock} шт.\n"
            )
            return

        if quantity > 0:
            product.stock -= quantity
            if product in self.products:
                self.products[product] += quantity
            else:
                self.products[product] = quantity

    def calculate_total(self) -> float:
        total = 0
        for product, quantity in self.products.items():
            total += quantity * product.price
        print(f"Общая стоимость заказа: {total}\n")
        return total

    def products_leave(self) -> NoReturn:
        print(f"В корзине находятся следующие товары:")
        for product, count in self.products.items():
            print(f"  {product.name}: {count}")
        print()

    def remove_product(self, product: Product, quantity: int) -> NoReturn:
        if self.products[product] - quantity < 0:
            raise Exception(
                f"Вы не можете убрать из заказа товаров больше, чем в него положили. В заказе {self.products[product]} шт. товара {product.name}\n"
            )

        self.products[product] -= quantity
        if self.products[product] == 0:
            self.products.pop(product)

        print(f"Вы удалили {quantity} шт. товара {product.name}")
        self.products_leave()

    def return_product(self, product: Product, quantity: int) -> NoReturn:
        if self.products[product] - quantity < 0:
            raise Exception(
                f"Вы не можете убрать из заказа товаров больше, чем в него положили. В заказе {self.products[product]} шт. товара {product.name}\n"
            )

        self.products[product] -= quantity

        if self.products[product] == 0:
            self.products.pop(product)

        product.update_stock(quantity)
        print(f"Вы удалили {quantity} шт. товара {product.name}")
        self.products_leave()


class Store:
    def __init__(self) -> NoReturn:
        self.products = []

    def add_product(self, product: Product) -> NoReturn:
        self.products.append(product)

    def list_products(self) -> NoReturn:
        print("Все товары в магазине:")
        if len(self.products) == 0:
            print("Товаров в магазине нет\n")
        for product in self.products:
            print(
                f"    {product.name}:\n      Цена - {product.price}\n      Количество товаров в магазине: {product.stock}\n"
            )
