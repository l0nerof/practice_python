def print_product_names(product_names, index=0):
    if index >= len(product_names):
        return

    print(product_names[index])
    print_product_names(product_names, index + 1)


def find_product_by_name(products, target_name, product_keys=None, index=0):
    if product_keys is None:
        product_keys = list(products.keys())

    if index >= len(product_keys):
        return None

    current_key = product_keys[index]

    if current_key.lower() == target_name.lower():
        return current_key, products[current_key]

    return find_product_by_name(products, target_name, product_keys, index + 1)
