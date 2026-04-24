n = int(input("Введіть число n: "))

squares = [number ** 2 for number in range(1, n + 1)]

print("Список квадратів:", squares)
