from person import Person


class PartTimeStudent(Person):
    def __init__(self, name, age, practice_score_sum, practice_count, exam_score):
        super().__init__(name, age, practice_score_sum, practice_count, exam_score)

    def total_score(self):
        practice_avg = self.avg_practice_score()
        return 0.7 * practice_avg + 0.3 * self.exam_score

    def display_info(self):
        base_info = super().display_info()
        return (
            "Форма навчання: заочна\n"
            f"{base_info}\n"
            f"Загальний бал: {self.total_score():.2f}"
        )
