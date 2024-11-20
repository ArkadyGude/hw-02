class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):

        if not isinstance(lecturer, Lecturer):
            raise ValueError("Оценка может быть поставлена только лектору")
        elif course not in self.courses_in_progress:
            raise ValueError("Курс не числится в списке изучаемых")
        elif course not in lecturer.courses_attached:
            raise ValueError("Курс не закреплен за лектором")
        elif course in lecturer.grades:
            lecturer.grades[course] += [grade]
        else:
            lecturer.grades[course] = [grade]

    def averagegrade(self):
        return calculateaverage(self.grades)

    def __lt__(self, student):
        if not isinstance(other, Student):
            raise TypeError("Сравнение возможно только между студентами")
        return (self.averagegrade() < averagegrade())

    def __gt__(self, student):
        if not isinstance(other, Student):
            raise TypeError("Сравнение возможно только между студентами")
        return (self.averagegrade() > averagegrade())

    def __str__(self):
        return f'Студент\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.averagegrade()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}\n'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

class Lecturer(Mentor):

    def averagegrade(self):
        return calculateaverage(self.grades)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Сравнение возможно только между лекторами")
        return (self.averagegrade() < other.averagegrade())

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Сравнение возможно только между лекторами")
        return (self.averagegrade() > other.averagegrade())

    def __str__(self):
        return f'Лектор\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{self.averagegrade()}\n'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):

        if not isinstance(student, Student):
            raise ValueError("Оценка может быть поставлена только студенту")
        elif course not in student.courses_in_progress:
            raise ValueError("Курс не числится в списке изучаемых")
        elif course not in self.courses_attached:
            raise ValueError("Курс не закреплен за лектором")
        elif course in student.grades:
            student.grades[course] += [grade]
        else:
            student.grades[course] = [grade]

    def __str__(self):
        return f'Ревьюер\nИмя: {self.name}\nФамилия: {self.surname}\n'


# Универсальная функция расчета средних оценок для студентов и лекторов
def calculateaverage(grades):
    """Универсальная функция подсчета средней оценки."""
    totalgrades = [grade for gradeslist in grades.values() for grade in gradeslist]
    return sum(totalgrades) / len(totalgrades) if totalgrades else 0


# Создание экземпляров классов

student1 = Student('Иван', 'Петров', 'мужской')
student1.courses_in_progress += ['Python']
student1.finished_courses += ['Java']

student2 = Student('Александр', 'Коржов', 'мужской')
student2.courses_in_progress += ['GIT']
student2.finished_courses += ['HTML']

reviewer1 = Reviewer('Семен', 'Афанасьев')
reviewer2 = Reviewer('Григорий', 'Савельев')

reviewer1.courses_attached += ['Python', 'Java']
reviewer2.courses_attached += ['GIT', 'HTML']

reviewer1.rate_hw(student1, 'Python', 10)
reviewer2.rate_hw(student2, 'GIT', 10)

lecturer1 = Lecturer('Дмитрий', 'Базаров')
lecturer2 = Lecturer('Василий', 'Романов')

lecturer1.courses_attached += ['Python']
lecturer2.courses_attached += ['GIT']

student1.rate_lecturer(lecturer1, 'Python', 9)
student2.rate_lecturer(lecturer2, 'GIT', 8)


# Расчет средних оценок

student1_average_grades = student1.averagegrade()
student2_average_grades = student2.averagegrade()

lecturer1_average_grades = lecturer1.averagegrade()
lecturer2_average_grades = lecturer2.averagegrade()


# Вывод списков студентов, лекторов и ревьюеров

print(student1)
print(student2)
print(reviewer1)
print(reviewer2)
print(lecturer1)
print(lecturer2)

# Вывод сравнительных оценок для лекторов

if lecturer1_average_grades > lecturer2_average_grades:
    print(f'У лектора {lecturer1.name} оценка {lecturer1_average_grades} выше чем у лектора {lecturer2.name} с оценкой {lecturer2_average_grades}')
elif lecturer1_average_grades < lecturer2_average_grades:
    print(
        f'У лектора {lecturer1.name} оценка {lecturer1_average_grades} ниже чем у лектора {lecturer2.name} с оценкой {lecturer2_average_grades}')
else:
    print(f'У лектора {lecturer1.name} и у лектора {lecturer2.name} оценки одинаковые {lecturer1_average_grades} и {lecturer2_average_grades}')

# Вывод сравнительных оценок для студентов

if student1_average_grades > student2_average_grades:
    print(f'У студента {student1.name} оценка {student1_average_grades} выше чем у студента {student2.name} с оценкой {student2_average_grades}')
elif student1_average_grades < student2_average_grades:
    print(
        f'У студента {student1.name} оценка {student1_average_grades} ниже чем у студента {student2.name} с оценкой {student2_average_grades}')
else:
    print(f'У студента {student1.name} и у студента {lecturer2.name} оценки одинаковые {student1_average_grades} и {student2_average_grades}')
