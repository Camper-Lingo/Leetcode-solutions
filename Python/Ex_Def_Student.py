'''

Student grades system

Create:

class Student:

with:

name: str
grades: list[float]

Create:

add_grade(nota: float) -> None
calculate_avg() -> float



'''





class Student:
    def __init__(self, name: str, grades: list[float]):
        self.name = name
        self.grades = grades

    def add_grade(self, grade: float) -> None:
        if grade > 0 and grade <= 10:
            self.grades.append(grade)

    def calculate_avg(self) -> float:
        sum = 0
        for grade in self.grades:
            sum += grade
        return round(sum/len(self.grades), 1)

    

grades = [5.5,7.8,4.3]

John = Student("John", grades)
John.add_grade(3.8)
print(John.calculate_avg())

