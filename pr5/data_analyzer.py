class DataAnalyzer:
    def __init__(self, data):
        self.data = data
        self.course_columns = self._extract_course_columns()

    def _extract_course_columns(self):
        if not self.data:
            return []

        ignored_columns = {"student_id", "first_name", "last_name"}
        return [column for column in self.data[0].keys() if column not in ignored_columns]

    def get_students(self):
        return [
            {
                "id": student["student_id"],
                "first_name": student["first_name"],
                "last_name": student["last_name"],
            }
            for student in self.data
        ]

    def get_courses(self):
        return [
            {"id": index, "name": course_name}
            for index, course_name in enumerate(self.course_columns, start=1)
        ]

    def get_grades(self):
        grades = []

        for student in self.data:
            for course_id, course_name in enumerate(self.course_columns, start=1):
                raw_grade = student.get(course_name, "")

                if raw_grade == "":
                    continue

                grades.append(
                    {
                        "student_id": student["student_id"],
                        "course_id": course_id,
                        "grade": int(raw_grade),
                    }
                )

        return grades
