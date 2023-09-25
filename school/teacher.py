from school.person import Person
import random


class Teacher(Person):

    def __init__(self, num_of_teached_stud, *args):
        self.name = args[0]
        self.age = args[1]
        self.gender = args[2]
        super().__init__(self.name, self.age, self.gender)
        self.num_of_teached_stud = num_of_teached_stud

    def teach(self, dscpl, *args):
        for std in list(args):
            std.take(dscpl)
            self.num_of_teached_stud += 1

    def __len__(self):
        return len(self.num_of_teached_stud)


class Discipline:

    def __init__(self, *args):
        self.dscpl_list = list(args)


class Student(Person):

    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.gender = args[2]
        super().__init__(self.name, self.age, self.gender)
        self.knowledge = []

    def take(self, dscpl):
        self.knowledge.append(dscpl)

    def __len__(self):
        return len(self.knowledge)

    def forget(self):
        fgt = random.choice(self.knowledge)
        self.knowledge.remove(fgt)
        print(self.name + ' забыл ' + fgt)


discipline = Discipline('Python', "Version Control Systems", "Relational Databases", "NoSQL databases", "Message Brokers")
teacher_one = Teacher(0, "Teacher One", 26, "male")
student_one = Student("Student One", 20, "male")
student_two = Student("Student Two", 19, "female")
student_three = Student("Student Three", 19, "female")
student_four = Student("Student Four", 21, "female")

teacher_one.teach(discipline.dscpl_list[0], student_one, student_four, student_three)
teacher_one.teach(discipline.dscpl_list[1], student_one, student_two, student_three)
teacher_one.teach(discipline.dscpl_list[2], student_two, student_four, student_three)
teacher_one.teach(discipline.dscpl_list[3], student_one, student_four, student_two)
teacher_one.teach(discipline.dscpl_list[4], student_one, student_four)

student_one.forget()

print(student_one.name + '\t' + student_one.gender + '\t обладает следующими знаниями')
for i in range(len(student_one)):
    print(student_one.knowledge[i])
print(student_two.name + '\t' + student_two.gender + '\t обладает следующими знаниями')
for i in range(len(student_two)):
    print(student_one.knowledge[i])
print(student_three.name + '\t' + student_three.gender + '\t обладает следующими знаниями')
for i in range(len(student_three)):
    print(student_three.knowledge[i])
print(student_four.name + '\t' + student_four.gender + '\t обладает следующими знаниями')
for i in range(len(student_four)):
    print(student_four.knowledge[i])
