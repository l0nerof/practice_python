from calculations import calculate_discount, calculate_stock_value
from data_input import get_demo_products, input_products
from general import find_product_by_name, print_product_names


def print_products(products):
    print("Поточні товари:")

    for product_name, details in products.items():
        print(
            f"{product_name}: ціна {details['price']:.2f} грн, "
            f"залишок {details['stock']} од."
        )

    print()


def print_stock_value_report(products):
    stock_values, total_value = calculate_stock_value(products)

    print("Вартість залишків:")

    for product_name, product_value in stock_values.items():
        print(f"{product_name}: {product_value:.2f} грн")

    print(f"Загальна вартість залишків: {total_value:.2f} грн")
    print()


def print_discount_report(products):
    discounts = calculate_discount(products)

    print("Знижки:")

    for product_name, details in discounts.items():
        if details["applied"]:
            print(
                f"{product_name}: знижка {details['discount_amount']:.2f} грн "
                f"(нова ціна {details['discounted_price']:.2f} грн)"
            )
        else:
            print(f"{product_name}: знижка не застосовується")

    print()


def print_search_result(products):
    target_name = input("Введіть назву товару для пошуку: ").strip()
    result = find_product_by_name(products, target_name)

    if result is None:
        print("Товар не знайдено.")
    else:
        product_name, details = result
        print(
            f"Товар знайдено: {product_name}, ціна {details['price']:.2f} грн, "
            f"залишок {details['stock']} од."
        )


def choose_products():
    print("Система управління товарами")
    print("1 - ручне введення")
    print("2 - демо-дані")

    choice = input("Оберіть режим роботи: ").strip()
    print()

    if choice == "1":
        return input_products()

    return get_demo_products()


def main():
    products = choose_products()

    if not products:
        print("Список товарів порожній.")
        return

    print_products(products)
    print_stock_value_report(products)
    print_discount_report(products)

    print("Список назв товарів:")
    print_product_names(list(products.keys()))
    print()

    print_search_result(products)


if __name__ == "__main__":
    main()
