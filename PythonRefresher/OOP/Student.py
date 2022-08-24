"""
Object Oriented Programming
"""


class Student:
    number_of_students = 0
    school = 'hongik university'

    def __init__(self, first_name, last_name, major):

        self.first_name = first_name
        self.last_name = last_name
        self.major = major

        Student.number_of_students += 1

    def fullname_with_major(self):
        return f'{self.first_name} {self.last_name} majored in {self.major}'

    def fullname_major_school(self):
        return f'{self.first_name} {self.last_name} is a {self.major} goes to {self.school}'

    @classmethod
    def set_online_school(cls, new_school):
        cls.school = new_school

    @classmethod
    def split_students(cls, student_str):
        first_name, last_name, major = student_str.split('.')
        return cls(first_name, last_name, major)


print(f'Number of students = {Student.number_of_students}')
student_1 = Student("joeun", "park", "computer engineering")
print(f'Number of students = {Student.number_of_students}')
student_2 = Student("john", "miller", "math")
print(f'Number of students = {Student.number_of_students}')

print(student_1.school)
print(student_2.school)
Student.set_online_school('I use a Google Hangouts for class!')
print(student_1.school)
print(student_2.school)

new_student = 'Adil.Yutzy.English'
student_3 = Student.split_students(new_student)
print(f'Number of students = {Student.number_of_students}')
print(student_3)