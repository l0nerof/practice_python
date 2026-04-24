import json

from desired_performance import DesiredPerformance
from real_performance import RealPerformance
from student import Student
from student_data import StudentData


class StudentRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def insert(self, student_data):
        query = """
            INSERT INTO student_records (
                full_name,
                group_number,
                birth_date,
                address,
                real_subjects,
                real_grades,
                real_average,
                desired_subjects,
                desired_grades,
                desired_average
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        values = self._to_db_tuple(student_data)
        self.db_manager.cursor.execute(query, values)
        self.db_manager.connection.commit()
        student_data.record_id = self.db_manager.cursor.lastrowid
        return student_data.record_id

    def update(self, student_data):
        if student_data.record_id is None:
            raise ValueError("Student data must have record_id before update.")

        query = """
            UPDATE student_records
            SET
                full_name = ?,
                group_number = ?,
                birth_date = ?,
                address = ?,
                real_subjects = ?,
                real_grades = ?,
                real_average = ?,
                desired_subjects = ?,
                desired_grades = ?,
                desired_average = ?
            WHERE id = ?
        """

        values = self._to_db_tuple(student_data) + (student_data.record_id,)
        self.db_manager.cursor.execute(query, values)
        self.db_manager.connection.commit()

    def delete(self, record_id):
        self.db_manager.cursor.execute(
            "DELETE FROM student_records WHERE id = ?",
            (record_id,),
        )
        self.db_manager.connection.commit()

    def get_by_id(self, record_id):
        self.db_manager.cursor.execute(
            "SELECT * FROM student_records WHERE id = ?",
            (record_id,),
        )
        row = self.db_manager.cursor.fetchone()
        return self._from_db_row(row) if row else None

    def get_all(self):
        self.db_manager.cursor.execute(
            "SELECT * FROM student_records ORDER BY id"
        )
        rows = self.db_manager.cursor.fetchall()
        return [self._from_db_row(row) for row in rows]

    def _to_db_tuple(self, student_data):
        return (
            student_data.student.full_name,
            student_data.student.group_number,
            student_data.student.birth_date,
            student_data.student.address,
            json.dumps(student_data.real_performance.subjects, ensure_ascii=False),
            json.dumps(student_data.real_performance.grades, ensure_ascii=False),
            round(student_data.real_performance.average_score(), 2),
            json.dumps(student_data.desired_performance.subjects, ensure_ascii=False),
            json.dumps(student_data.desired_performance.grades, ensure_ascii=False),
            round(student_data.desired_performance.average_score(), 2),
        )

    def _from_db_row(self, row):
        student = Student(
            full_name=row[1],
            group_number=row[2],
            birth_date=row[3],
            address=row[4],
        )

        real_performance = RealPerformance(
            subjects=json.loads(row[5]),
            grades=json.loads(row[6]),
        )

        desired_performance = DesiredPerformance(
            subjects=json.loads(row[8]),
            grades=json.loads(row[9]),
        )

        return StudentData(
            student=student,
            real_performance=real_performance,
            desired_performance=desired_performance,
            record_id=row[0],
        )
