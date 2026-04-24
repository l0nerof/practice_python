def parse_number(value):
    number = float(value.strip())

    if number.is_integer():
        return int(number)

    return number


def has_pair_with_sum(numbers, n):
    seen_numbers = set()

    for number in numbers:
        needed_number = n - number

        if needed_number in seen_numbers:
            return True

        seen_numbers.add(number)

    return False


numbers = [
    parse_number(item)
    for item in input("Введіть числа через кому: ").split(",")
    if item.strip()
]
n = parse_number(input("Введіть число n: "))

print(has_pair_with_sum(numbers, n))
