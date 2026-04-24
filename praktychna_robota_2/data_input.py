def get_demo_products():
    return {
        "Laptop": {"price": 32000.0, "stock": 8},
        "Mouse": {"price": 850.0, "stock": 25},
        "Keyboard": {"price": 2100.0, "stock": 6},
        "Monitor": {"price": 7800.0, "stock": 12},
    }


def input_products():
    products = {}

    while True:
        name = input("Введіть назву товару або 'stop' для завершення: ").strip()

        if name.lower() == "stop":
            break

        if not name:
            print("Назва товару не може бути порожньою.")
            continue

        try:
            price = float(input("Введіть ціну товару: ").strip())
            stock = int(input("Введіть залишок товару на складі: ").strip())
        except ValueError:
            print("Помилка: введіть коректні числові значення.")
            continue

        if price < 0 or stock < 0:
            print("Помилка: ціна та залишок не можуть бути від'ємними.")
            continue

        products[name] = {"price": price, "stock": stock}
        print(f"Товар '{name}' додано.")

    return products
