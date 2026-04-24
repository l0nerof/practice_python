from academic_performance import AcademicPerformance


class DesiredPerformance(AcademicPerformance):
    def average_score(self):
        return sum(self.grades) / len(self.grades)
