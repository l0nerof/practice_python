import sqlite3


class DatabaseInitializer:
    def __init__(self, db_name="students.db"):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL
            )
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE
            )
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS grades (
                student_id INTEGER NOT NULL,
                course_id INTEGER NOT NULL,
                grade INTEGER NOT NULL,
                PRIMARY KEY (student_id, course_id),
                FOREIGN KEY(student_id) REFERENCES students(id),
                FOREIGN KEY(course_id) REFERENCES courses(id)
            )
            """
        )

        self.connection.commit()

    def close(self):
        self.connection.close()
