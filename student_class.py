import os

os.system("cls")


class Student:
    def __init__(self, first, last, grade):
        self.first = first
        self.last = last
        self.grade = grade
        self.full_name = self.full_name

    def fancy_print(self):
        print("First Name:", self.first)
        print("Last Name:", self.last)
        print("Grade:", self.grade)
        print()

    def full_name(self):
        return self.first + " " + self.last


# Mail Program
student1 = Student("Abigail", "Lightle", 4)
student1.fancy_print()

student2 = Student("Emily", "Lightle", 1)
student2.fancy_print()

print(student1.full_name())
print(student2.full_name())
print()

students = []
students.append(student1)
students.append(student2)

for s in students:
    print(s.first)
    print(s.last)
    print(s.grade)
    print(s.full_name())
    print()
