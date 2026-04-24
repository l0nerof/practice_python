def parse_number(value):
    number = float(value.strip())

    if number.is_integer():
        return int(number)

    return number


def get_number_statistics(numbers):
    maximum = max(numbers)
    minimum = min(numbers)
    average = sum(numbers) / len(numbers)

    return maximum, minimum, average


numbers = [
    parse_number(item)
    for item in input("Введіть числа через кому: ").split(",")
    if item.strip()
]

if numbers:
    maximum, minimum, average = get_number_statistics(numbers)

    print("Максимальне число:", maximum)
    print("Мінімальне число:", minimum)
    print("Середнє арифметичне:", average)
else:
    print("Список чисел порожній")
