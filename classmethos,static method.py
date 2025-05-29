# # When a student is created, store their name and marks.

# # Add an instance method display() that prints the student's name and marks.

# # Add a class method change_school_name(cls, name) to update the school name for all students.

# # Add a static method is_passed(marks) that returns True if marks are >= 35, else False.

# # 🎯 Additional:
# # Class variable: school_name = "ABC High School"


# class Student:
#     school_name = "ABC High School"

#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
    
#     def display(self):
#             print(f"student name is: {self.name} and student marks are : {self.marks}")
#     @classmethod
#     def change_school_name(cls,school_name):
#         cls.school_name = school_name
    
#     @staticmethod
#     def is_passed(marks):
#         return marks >= 35


        


        

# s1 = Student("Sanjay", 80)
# s2 = Student("Rahul", 30)

# s1.display()  # Output: Name: Sanjay, Marks: 80
# s2.display()  # Output: Name: Rahul, Marks: 30

# print(Student.is_passed(s1.marks))  # True
# print(Student.is_passed(s2.marks))  # False

# Student.change_school_name("XYZ School")
# print(Student.school_name)  # Output: XYZ School



#  Challenge: Create a Student and GraduateStudent system
# ✅ Requirements:
# 🔹 Base class: Student
# Class variable: school_name = "ABC High School"

# Instance variables: name, marks

# Instance method: display() – show name, marks, school name

# Class method: change_school_name() – update school name

# Static method: is_passed() – return True if marks >= 35

# 🔹 Subclass: GraduateStudent (inherits from Student)
# New instance variable: degree

# Override display() method to also print degree

# Add a static method: is_eligible_for_job(marks) – return True if marks >= 60

class Student:
     school_name = "ABC High School"

     def __init__(self,name, marks):
          self.name = name
          self.marks = marks
          
     def display(self):
          print(f"name:{self.name} marks:{self.marks} school name:{self.school_name}")


     @classmethod
     def change_school_name(cls,school_name):
          cls.school_name = school_name

     @staticmethod
     def is_passed(marks):
          return marks >= 35

class GraduateStudent(Student):
     def __init__(self,name,marks,degree):
          super().__init__(name,marks)
          
          self.degree = degree
    
     def display(self):
          print("degree")

     @staticmethod
     def is_eligible_for_job(marks):
          return marks >= 60
          
    
s1 = GraduateStudent("Sanjay", 75, "B.Tech")
s1.display()

print(GraduateStudent.is_passed(s1.marks))           # True
print(GraduateStudent.is_eligible_for_job(s1.marks)) # True

GraduateStudent.change_school_name("XYZ University")
print(GraduateStudent.school_name)  # Output: XYZ University

