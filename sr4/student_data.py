class StudentData:
    def __init__(self, student, real_performance, desired_performance, record_id=None):
        self.record_id = record_id
        self.student = student
        self.real_performance = real_performance
        self.desired_performance = desired_performance

    @property
    def record_id(self):
        return self.__record_id

    @record_id.setter
    def record_id(self, value):
        if value is not None and value <= 0:
            raise ValueError("Record id must be greater than 0.")
        self.__record_id = value

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, value):
        from student import Student

        if not isinstance(value, Student):
            raise TypeError("student must be an instance of Student.")
        self.__student = value

    @property
    def real_performance(self):
        return self.__real_performance

    @real_performance.setter
    def real_performance(self, value):
        from real_performance import RealPerformance

        if not isinstance(value, RealPerformance):
            raise TypeError("real_performance must be an instance of RealPerformance.")
        self.__real_performance = value

    @property
    def desired_performance(self):
        return self.__desired_performance

    @desired_performance.setter
    def desired_performance(self, value):
        from desired_performance import DesiredPerformance

        if not isinstance(value, DesiredPerformance):
            raise TypeError("desired_performance must be an instance of DesiredPerformance.")
        self.__desired_performance = value
