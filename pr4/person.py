from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age, practice_score_sum, practice_count, exam_score):
        self.name = name
        self.age = age
        self.practice_score_sum = practice_score_sum
        self.practice_count = practice_count
        self.exam_score = exam_score

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty.")
        self._name = value.strip()

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value <= 0:
            raise ValueError("Age must be greater than 0.")
        self._age = value

    @property
    def practice_score_sum(self):
        return self._practice_score_sum

    @practice_score_sum.setter
    def practice_score_sum(self, value):
        if value < 0:
            raise ValueError("Practice score sum cannot be negative.")
        self._practice_score_sum = value

    @property
    def practice_count(self):
        return self._practice_count

    @practice_count.setter
    def practice_count(self, value):
        if value < 0:
            raise ValueError("Practice count cannot be negative.")
        self._practice_count = value

    @property
    def exam_score(self):
        return self._exam_score

    @exam_score.setter
    def exam_score(self, value):
        if value < 0 or value > 100:
            raise ValueError("Exam score must be in the range 0-100.")
        self._exam_score = value

    def avg_practice_score(self):
        if self.practice_count == 0:
            return 0.0
        return self.practice_score_sum / self.practice_count

    def display_info(self):
        lines = [
            f"Ім'я: {self.name}",
            f"Вік: {self.age}",
        ]

        if self.practice_count > 0:
            lines.append(f"Середній бал за практичні: {self.avg_practice_score():.2f}")

        return "\n".join(lines)

    @abstractmethod
    def total_score(self):
        pass
