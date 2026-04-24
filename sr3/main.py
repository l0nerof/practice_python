from pathlib import Path

from models import DesiredPerformance, RealPerformance, Student, StudentData
from savers import CsvSaver, JsonSaver, XmlSaver, build_file_name, ensure_output_dir


def print_student_data(student_data):
    data = student_data.to_dict()

    print("Дані студента:")
    print(f"ПІБ: {data['student']['full_name']}")
    print(f"Номер групи: {data['student']['group_number']}")
    print(f"Дата народження: {data['student']['birth_date']}")
    print(f"Адреса: {data['student']['address']}")
    print()
    print("Реальна успішність:")
    print(f"Предмети: {', '.join(data['real_performance']['subjects'])}")
    print(f"Бали: {', '.join(map(str, data['real_performance']['grades']))}")
    print(f"Середній бал: {data['real_performance']['average_score']:.2f}")
    print()
    print("Бажана успішність:")
    print(f"Предмети: {', '.join(data['desired_performance']['subjects'])}")
    print(f"Бажані бали: {', '.join(map(str, data['desired_performance']['grades']))}")
    print(f"Бажаний середній бал: {data['desired_performance']['average_score']:.2f}")
    print()


def save_all_formats(student_data, base_dir):
    output_dir = ensure_output_dir(base_dir)
    work_code = "SR3"

    savers = [
        ("json", JsonSaver()),
        ("xml", XmlSaver()),
        ("csv", CsvSaver()),
    ]

    saved_files = []

    for extension, saver in savers:
        file_name = build_file_name(student_data, work_code, extension)
        file_path = output_dir / file_name
        saver.save(student_data, file_path)
        saved_files.append(file_path.name)

    return saved_files


def main():
    student = Student(
        full_name="Ivanenko Olena Petrivna",
        group_number="IPZ-21",
        birth_date="15.04.2005",
        address="Kyiv",
    )

    real_performance = RealPerformance(
        subjects=["Python", "Math", "English"],
        grades=[88, 92, 79],
    )

    desired_performance = DesiredPerformance(
        subjects=["Python", "Math", "English"],
        grades=[95, 98, 90],
    )

    student_data = StudentData(student, real_performance, desired_performance)

    print_student_data(student_data)

    saved_files = save_all_formats(student_data, Path(__file__).parent)

    print("Файли успішно створено:")
    for file_name in saved_files:
        print(f"- {file_name}")


if __name__ == "__main__":
    main()
