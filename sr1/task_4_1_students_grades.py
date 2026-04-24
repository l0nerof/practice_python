students = {}

while True:
    name = input("Введіть ім'я студента або 'стоп' для завершення: ")

    if name.strip().lower() in ("стоп", "stop"):
        break

    grade = int(input("Введіть оцінку студента: "))
    students[name] = grade

print("Оцінки студентів:")

for name, grade in students.items():
    print(f"{name}: {grade}")
