def calculate_stock_value(products):
    stock_values = {}
    total_value = 0.0

    for product_name, details in products.items():
        product_value = details["price"] * details["stock"]
        stock_values[product_name] = product_value
        total_value += product_value

    return stock_values, total_value


def calculate_discount(products, low_stock_threshold=10, discount_rate=0.05):
    discounts = {}

    for product_name, details in products.items():
        if details["stock"] < low_stock_threshold:
            discount_amount = details["price"] * discount_rate
            discounted_price = details["price"] - discount_amount
            discounts[product_name] = {
                "discount_amount": discount_amount,
                "discounted_price": discounted_price,
                "applied": True,
            }
        else:
            discounts[product_name] = {
                "discount_amount": 0.0,
                "discounted_price": details["price"],
                "applied": False,
            }

    return discounts
