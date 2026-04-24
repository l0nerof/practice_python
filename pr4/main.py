from full_time_student import FullTimeStudent
from part_time_student import PartTimeStudent


def main():
    university_students = [
        FullTimeStudent("KOLA", 24, 910, 10, 95, 85),
        FullTimeStudent("Klavdia Petrivna", 19, 930, 10, 99, 20),
        PartTimeStudent("CHEEV", 22, 390, 4, 78),
        PartTimeStudent("YAKTAK", 21, 480, 5, 82),
    ]

    print("Результати розрахунку успішності студентів:")
    print()

    for index, student in enumerate(university_students, start=1):
        print(f"Студент {index}:")
        print(student.display_info())
        print()


if __name__ == "__main__":
    main()
