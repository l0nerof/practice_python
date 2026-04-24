import sqlite3


class DatabaseManager:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def create_table_if_not_exists(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS student_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                group_number TEXT NOT NULL,
                birth_date TEXT NOT NULL,
                address TEXT NOT NULL,
                real_subjects TEXT NOT NULL,
                real_grades TEXT NOT NULL,
                real_average REAL NOT NULL,
                desired_subjects TEXT NOT NULL,
                desired_grades TEXT NOT NULL,
                desired_average REAL NOT NULL
            )
            """
        )
        self.connection.commit()

    def close(self):
        self.connection.close()
