class student:

   def new(self,name):
        print("hello how are you" ,name)

student1=student()
student2=student()

student1.new("abhinand")


class student:
    pass
student1 = student()
student2 = student()

student1.name = "Amana"
student1.age = 21
student1.course = "python"

print(student1.name)
print(student1.age)
print(student1.course)



class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

    def study(self):
        print(self.name, "is studying")


student1 = Student("Amana", 21, "Python")
student2 = Student("Rahul", 22, "Java")

student1.display()
student1.study()

print()

student2.display()
student2.study()

#encapsulation

class Student:

    def __init__(self, name, mark):
        self.name = name
        self.__mark = mark

    def get_mark(self):
        return self.__mark


student1 = Student("Amana", 85)

print(student1.name)
print(student1.get_mark())



#polymorphism
class Student:

    def role(self):
        print("Student is studying")


class Teacher:

    def role(self):
        print("Teacher is teaching")


student = Student()
teacher = Teacher()

student.role()
teacher.role()
