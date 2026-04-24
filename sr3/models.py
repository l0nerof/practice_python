from abc import ABC, abstractmethod


class Student:
    def __init__(self, full_name, group_number, birth_date, address=""):
        self.full_name = full_name
        self.group_number = group_number
        self.birth_date = birth_date
        self.address = address

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        if not value.strip():
            raise ValueError("Full name cannot be empty.")
        self.__full_name = value.strip()

    @property
    def group_number(self):
        return self.__group_number

    @group_number.setter
    def group_number(self, value):
        if not value.strip():
            raise ValueError("Group number cannot be empty.")
        self.__group_number = value.strip()

    @property
    def birth_date(self):
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, value):
        if not value.strip():
            raise ValueError("Birth date cannot be empty.")
        self.__birth_date = value.strip()

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value.strip()

    def to_dict(self):
        return {
            "full_name": self.full_name,
            "group_number": self.group_number,
            "birth_date": self.birth_date,
            "address": self.address,
        }


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

    def to_dict(self):
        return {
            "subjects": self.subjects,
            "grades": self.grades,
            "average_score": round(self.average_score(), 2),
        }


class RealPerformance(AcademicPerformance):
    def average_score(self):
        return sum(self.grades) / len(self.grades)


class DesiredPerformance(AcademicPerformance):
    def average_score(self):
        return sum(self.grades) / len(self.grades)


class StudentData:
    def __init__(self, student, real_performance, desired_performance):
        self.student = student
        self.real_performance = real_performance
        self.desired_performance = desired_performance

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, value):
        if not isinstance(value, Student):
            raise TypeError("student must be an instance of Student.")
        self.__student = value

    @property
    def real_performance(self):
        return self.__real_performance

    @real_performance.setter
    def real_performance(self, value):
        if not isinstance(value, RealPerformance):
            raise TypeError("real_performance must be an instance of RealPerformance.")
        self.__real_performance = value

    @property
    def desired_performance(self):
        return self.__desired_performance

    @desired_performance.setter
    def desired_performance(self, value):
        if not isinstance(value, DesiredPerformance):
            raise TypeError("desired_performance must be an instance of DesiredPerformance.")
        self.__desired_performance = value

    def to_dict(self):
        return {
            "student": self.student.to_dict(),
            "real_performance": self.real_performance.to_dict(),
            "desired_performance": self.desired_performance.to_dict(),
        }
