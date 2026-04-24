from academic_performance import AcademicPerformance


class RealPerformance(AcademicPerformance):
    def average_score(self):
        return sum(self.grades) / len(self.grades)
