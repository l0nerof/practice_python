from pathlib import Path

from csv_reader import CsvReader
from data_analyzer import DataAnalyzer
from data_preprocessor import DataPreprocessor
from database_initializer import DatabaseInitializer
from data_uploader import DataUploader
from database_queries import DatabaseQueries


def main():
    base_dir = Path(__file__).parent
    csv_source = str(base_dir / "students.csv")
    db_path = str(base_dir / "students.db")

    reader = CsvReader()
    raw_data = reader.read_data(csv_source)
    print(f"CSV-файл успішно зчитано: {len(raw_data)} запис(и).")

    preprocessor = DataPreprocessor(raw_data)
    processed_data = preprocessor.add_student_ids()

    analyzer = DataAnalyzer(processed_data)
    students = analyzer.get_students()
    courses = analyzer.get_courses()
    grades = analyzer.get_grades()

    print("Дані підготовлено:")
    print(f"- студентів: {len(students)}")
    print(f"- курсів: {len(courses)}")
    print(f"- оцінок: {len(grades)}")
    print()

    initializer = DatabaseInitializer(db_path)
    initializer.create_tables()
    initializer.close()
    print("База даних і таблиці успішно створені.")

    uploader = DataUploader(db_path)
    uploader.upload_students(students)
    uploader.upload_courses(courses)
    uploader.upload_grades(grades)
    uploader.close()
    print("Дані успішно завантажені в базу даних.")
    print()

    queries = DatabaseQueries(db_path)

    print("Усі студенти:")
    for student_id, first_name, last_name in queries.get_all_students():
        print(f"{student_id}. {first_name} {last_name}")
    print()

    search_last_name = "Barbak"
    student = queries.find_student_by_lastname(search_last_name)

    print(f"Пошук студента за прізвищем '{search_last_name}':")
    if student is None:
        print("Студента не знайдено.")
    else:
        student_id, first_name, last_name = student
        print(f"Знайдено: {first_name} {last_name} (ID: {student_id})")
        print("Оцінки студента:")

        for course_name, grade in queries.get_student_grades(student_id):
            print(f"- {course_name}: {grade}")

    queries.close()


if __name__ == "__main__":
    main()
