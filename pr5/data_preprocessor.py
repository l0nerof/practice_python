class DataPreprocessor:
    def __init__(self, data):
        self.data = data

    def add_student_ids(self):
        processed_data = []

        for index, student in enumerate(self.data, start=1):
            normalized_student = {}

            for key, value in student.items():
                normalized_student[key.strip()] = value.strip() if isinstance(value, str) else value

            normalized_student["student_id"] = index
            processed_data.append(normalized_student)

        self.data = processed_data
        return self.data
