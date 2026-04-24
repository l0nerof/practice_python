def get_student_count():
    while True:
        try:
            student_count = int(input("Введіть кількість студентів: ").strip())

            if student_count <= 0:
                print("Кількість студентів має бути більшою за 0!")
                continue

            return student_count
        except ValueError:
            print("Помилка! Введіть ціле число.")


def get_student_name(existing_names):
    while True:
        name = input("Введіть ім'я студента: ").strip()

        if not name:
            print("Ім'я не може бути порожнім!")
            continue

        if name in existing_names:
            print("Студент з таким ім'ям уже існує. Введіть інше ім'я.")
            continue

        return name


def get_student_scores(name):
    while True:
        try:
            raw_scores = input(f"Введіть оцінки {name} через пробіл: ").strip().split()
            scores = list(map(int, raw_scores))

            if not scores:
                print("Оцінки не можуть бути порожніми!")
                continue

            if any(score < 0 or score > 100 for score in scores):
                print("Оцінки мають бути в межах 0-100!")
                continue

            return scores
        except ValueError:
            print("Помилка! Введіть числа через пробіл.")


def get_student_data():
    students = {}
    student_count = get_student_count()

    for _ in range(student_count):
        name = get_student_name(students)
        scores = get_student_scores(name)
        students[name] = scores

    return students


def calculate_average(grades_dict):
    total_sum = 0
    total_count = 0

    for scores in grades_dict.values():
        total_sum += sum(scores)
        total_count += len(scores)

    if total_count == 0:
        return 0

    return total_sum / total_count


def find_students_below_average(grades_dict, group_average):
    below_average_students = {}

    for student, scores in grades_dict.items():
        student_average = sum(scores) / len(scores)

        if student_average < group_average:
            below_average_students[student] = student_average

    return below_average_students


def main():
    students_data = get_student_data()
    group_average = calculate_average(students_data)
    below_average_students = find_students_below_average(students_data, group_average)

    print()
    print(f"Середній бал групи: {group_average:.2f}")
    print()
    print("Студенти з балом нижче середнього:")

    if below_average_students:
        for student, average in below_average_students.items():
            print(f"- {student}: {average:.2f}")
    else:
        print("Усі студенти мають оцінки не нижче середнього.")


if __name__ == "__main__":
    main()
