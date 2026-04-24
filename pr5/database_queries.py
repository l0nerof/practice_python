import sqlite3


class DatabaseQueries:
    def __init__(self, db_name="students.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def get_all_students(self):
        self.cursor.execute(
            """
            SELECT id, first_name, last_name
            FROM students
            ORDER BY id
            """
        )
        return self.cursor.fetchall()

    def find_student_by_lastname(self, last_name):
        self.cursor.execute(
            """
            SELECT id, first_name, last_name
            FROM students
            WHERE last_name = ?
            """,
            (last_name,),
        )
        return self.cursor.fetchone()

    def get_student_grades(self, student_id):
        self.cursor.execute(
            """
            SELECT courses.name, grades.grade
            FROM grades
            JOIN courses ON grades.course_id = courses.id
            WHERE grades.student_id = ?
            ORDER BY courses.id
            """,
            (student_id,),
        )
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
