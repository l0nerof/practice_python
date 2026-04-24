import sqlite3


class DataUploader:
    def __init__(self, db_name="students.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def upload_students(self, students):
        self.cursor.executemany(
            """
            INSERT OR REPLACE INTO students (id, first_name, last_name)
            VALUES (?, ?, ?)
            """,
            [(student["id"], student["first_name"], student["last_name"]) for student in students],
        )
        self.connection.commit()

    def upload_courses(self, courses):
        self.cursor.executemany(
            """
            INSERT OR REPLACE INTO courses (id, name)
            VALUES (?, ?)
            """,
            [(course["id"], course["name"]) for course in courses],
        )
        self.connection.commit()

    def upload_grades(self, grades):
        self.cursor.executemany(
            """
            INSERT OR REPLACE INTO grades (student_id, course_id, grade)
            VALUES (?, ?, ?)
            """,
            [(grade["student_id"], grade["course_id"], grade["grade"]) for grade in grades],
        )
        self.connection.commit()

    def close(self):
        self.connection.close()
