from store.store import *


def check_store():
    # Создаем товары, которые будут на складе
    product_1 = Product("Смартфон Xiaomi 14 12/512 ГБ", 70230, 30)
    product_2 = Product("Смартфон Xiaomi POCO X6 Pro 12/512 ГБ", 28700, 50)
    product_3 = Product("Смартфон Redmi Note 13 8/256 ГБ", 19326, 100)

    product_in_warehouse = [product_1, product_2, product_3]
    for product in product_in_warehouse:
        print(
            f"Товар {product.name} был добавлен на склад в количестве {product.stock} шт. по цене {product.price} руб."
        )
    print()

    # Добавляем/убираем n-ое количество единиц товара со склада
    try:
        product_2.update_stock(20)
        product_3.update_stock(-120)
    except Exception as e:
        print(e)

    # Создаем магазин
    store = Store()

    # Список всех товаров
    store.list_products()

    # Добавляем товары в магазин
    store.add_product(product_1)
    store.add_product(product_2)
    store.add_product(product_3)

    # Список всех товаров
    store.list_products()

    # Создаем заказ
    order = Order()

    # Добавляем товары в заказ
    order.add_product(product_1, 1)
    order.add_product(product_2, 2)
    order.add_product(product_1, 50)
    order.add_product(product_3, 3)
    order.products_leave()

    # Выводим общую стоимость заказа
    order.calculate_total()

    # Удалим какие-то товары из заказа
    try:
        order.remove_product(product_2, 1)
        order.remove_product(product_2, 500)
    except Exception as e:
        print(e)

    # Возврат товара на склад
    order.return_product(product_2, 1)

    # Проверяем остатки на складе после заказа
    store.list_products()

    # Выводим общую стоимость заказа
    order.calculate_total()


def main():
    check_store()


if __name__ == "__main__":
    main()
