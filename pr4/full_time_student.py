from person import Person


class FullTimeStudent(Person):
    def __init__(self, name, age, practice_score_sum, practice_count, exam_score, attendance_pct):
        super().__init__(name, age, practice_score_sum, practice_count, exam_score)
        self.attendance_pct = attendance_pct

    @property
    def attendance_pct(self):
        return self._attendance_pct

    @attendance_pct.setter
    def attendance_pct(self, value):
        if value < 0 or value > 100:
            raise ValueError("Attendance percent must be in the range 0-100.")
        self._attendance_pct = value

    def total_score(self):
        practice_avg = self.avg_practice_score()
        return 0.6 * practice_avg + 0.3 * self.exam_score + 0.1 * self.attendance_pct

    def display_info(self):
        base_info = super().display_info()
        return (
            "Форма навчання: очна\n"
            f"{base_info}\n"
            f"Загальний бал: {self.total_score():.2f}"
        )
