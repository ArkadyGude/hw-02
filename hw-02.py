class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grades_student(self, student, grades):
        sum_grades = 0
        for k, v in grades.items():
            sum_grades += sum(v)
        self.average_grade_student = sum_grades / len(student.grades.values())
        return self.average_grade_student

    def __lt__(self, student):
        return (self.average_grades_student == average_grades_student)

    def __gt__(self, student):
        return (self.average_grades_student == average_grades_student)

    def __str__(self):
        return f'Студент\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade_student}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}\n'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

class Lecturer(Mentor):

    def average_grades_lecturer(self, lecturer, grades):
        sum_grades = 0
        for k, v in lecturer.grades.items():
            sum_grades += sum(v)
        self.average_grade_lecturer = sum_grades / len(lecturer.grades.values())
        # print(average_grade_lecturer)
        return self.average_grade_lecturer

    def __lt__(self, lecturer):
        return (self.average_grades_lecturer == lecturer.average_grades_lecturer)

    def __gt__(self, lecturer):
        return (self.average_grades_lecturer == lecturer.average_grades_lecturer)

    def __str__(self):
        return f'Лектор\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{self.average_grade_lecturer}\n'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Ревьюер\nИмя: {self.name}\nФамилия: {self.surname}\n'


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

student1_average_grades = student1.average_grades_student(student1, student1.grades)
student2_average_grades = student2.average_grades_student(student2, student2.grades)

lecturer1_average_grades = lecturer1.average_grades_lecturer(lecturer1, lecturer1.grades)
lecturer2_average_grades = lecturer2.average_grades_lecturer(lecturer2, lecturer2.grades)


print(student1)
print(student2)
print(reviewer1)
print(reviewer2)
print(lecturer1)
print(lecturer2)


if lecturer1_average_grades > lecturer2_average_grades:
    print(f'У лектора {lecturer1.name} оценка {lecturer1_average_grades} выше чем у лектора {lecturer2.name} с оценкой {lecturer2_average_grades}')
elif lecturer1_average_grades < lecturer2_average_grades:
    print(
        f'У лектора {lecturer1.name} оценка {lecturer1_average_grades} ниже чем у лектора {lecturer2.name} с оценкой {lecturer2_average_grades}')
else:
    print(f'У лектора {lecturer1.name} и у лектора {lecturer2.name} оценки одинаковые {lecturer1_average_grades} и {lecturer2_average_grades}')


if student1_average_grades > student2_average_grades:
    print(f'У студента {student1.name} оценка {student1_average_grades} выше чем у студента {student2.name} с оценкой {student2_average_grades}')
elif student1_average_grades < student2_average_grades:
    print(
        f'У студента {student1.name} оценка {student1_average_grades} ниже чем у студента {student2.name} с оценкой {student2_average_grades}')
else:
    print(f'У студента {student1.name} и у студента {lecturer2.name} оценки одинаковые {student1_average_grades} и {student2_average_grades}')
