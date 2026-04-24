from abc import ABC, abstractmethod


class AcademicPerformance(ABC):
    def __init__(self, subjects, grades):
        self.subjects = subjects
        self.grades = grades

    @property
    def subjects(self):
        return self.__subjects

    @subjects.setter
    def subjects(self, value):
        if not value or not all(isinstance(subject, str) and subject.strip() for subject in value):
            raise ValueError("Subjects must be a non-empty list of strings.")
        self.__subjects = [subject.strip() for subject in value]

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, value):
        if not value or not all(isinstance(grade, (int, float)) for grade in value):
            raise ValueError("Grades must be a non-empty list of numbers.")
        if any(grade < 0 or grade > 100 for grade in value):
            raise ValueError("Grades must be in the range 0-100.")
        if hasattr(self, "_AcademicPerformance__subjects") and len(value) != len(self.subjects):
            raise ValueError("Subjects and grades must have the same length.")
        self.__grades = list(value)

    @abstractmethod
    def average_score(self):
        pass
