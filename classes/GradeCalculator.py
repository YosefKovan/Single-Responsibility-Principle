
class GradeCalculator:

    @staticmethod
    def average_grade(student):
        total_grades = sum(student.grades)
        return total_grades // len(student.grades)

