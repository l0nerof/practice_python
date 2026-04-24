def parse_number(value):
    number = float(value.strip())

    if number.is_integer():
        return int(number)

    return number


numbers = [
    parse_number(item)
    for item in input("Введіть числа через кому: ").split(",")
    if item.strip()
]

print("Список:", numbers)
print("Кортеж:", tuple(numbers))

if numbers:
    total = sum(numbers)
    average = total / len(numbers)

    print("Сума:", total)
    print("Середнє арифметичне:", average)
else:
    print("Сума: 0")
    print("Середнє арифметичне неможливо обчислити для порожнього списку")
