from pathlib import Path

from database_manager import DatabaseManager
from desired_performance import DesiredPerformance
from real_performance import RealPerformance
from student import Student
from student_data import StudentData
from student_repository import StudentRepository


def build_first_student():
    return StudentData(
        student=Student(
            full_name="Ivanenko Olena Petrivna",
            group_number="IPZ-21",
            birth_date="15.04.2005",
            address="Kyiv",
        ),
        real_performance=RealPerformance(
            subjects=["Python", "Math", "English"],
            grades=[88, 92, 79],
        ),
        desired_performance=DesiredPerformance(
            subjects=["Python", "Math", "English"],
            grades=[95, 98, 90],
        ),
    )


def build_second_student():
    return StudentData(
        student=Student(
            full_name="Petrenko Maksym Ivanovych",
            group_number="KN-22",
            birth_date="03.11.2004",
            address="Lviv",
        ),
        real_performance=RealPerformance(
            subjects=["Python", "Math", "English"],
            grades=[75, 81, 84],
        ),
        desired_performance=DesiredPerformance(
            subjects=["Python", "Math", "English"],
            grades=[90, 92, 95],
        ),
    )


def print_student_data(prefix, student_data):
    print(prefix)
    print(f"ID: {student_data.record_id}")
    print(f"ПІБ: {student_data.student.full_name}")
    print(f"Група: {student_data.student.group_number}")
    print(f"Дата народження: {student_data.student.birth_date}")
    print(f"Адреса: {student_data.student.address}")
    print(f"Реальний середній бал: {student_data.real_performance.average_score():.2f}")
    print(f"Бажаний середній бал: {student_data.desired_performance.average_score():.2f}")
    print()


def main():
    db_path = Path(__file__).parent / "students_sr4.db"

    if db_path.exists():
        db_path.unlink()

    db_manager = DatabaseManager(str(db_path))
    db_manager.create_table_if_not_exists()
    repository = StudentRepository(db_manager)

    first_student = build_first_student()
    second_student = build_second_student()

    repository.insert(first_student)
    repository.insert(second_student)

    print("Після додавання записів:")
    for student_data in repository.get_all():
        print_student_data("Запис у базі даних", student_data)

    first_student.student.address = "Dnipro"
    first_student.desired_performance.grades = [96, 99, 95]
    repository.update(first_student)

    updated_student = repository.get_by_id(first_student.record_id)
    print("Після оновлення першого запису:")
    print_student_data("Оновлений запис", updated_student)

    repository.delete(second_student.record_id)
    print("Після видалення другого запису:")
    remaining_records = repository.get_all()
    print(f"Кількість записів у базі: {len(remaining_records)}")
    print()

    for student_data in remaining_records:
        print_student_data("Запис, що залишився", student_data)

    db_manager.close()
    print("Роботу з базою даних завершено успішно.")


if __name__ == "__main__":
    main()
