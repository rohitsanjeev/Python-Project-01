# 1)# Create a base class Shape with a method area() and create two subclasses Circle 
# and Square that override area() differently. # Call area() polymorphically for each shape.

# 2)# Write a program where a function play_sound(animal) can take different
# # animal objects like Dog, Cat, Cow, and call the make_sound() method on each.

# 3)# Make a class Payment and subclasses CreditCard, UPI, and Cash. All should have
# #  a method pay(amount) with different messages. Write a function process_payment(payment_method) that works polymorphically.

# animals = [Dog(), Cat(), Animal()] 


class Shape:
    def area(self):
        print("shape")
    

class Circle(Shape):
    def area(self):
        print("its circle")



class Square(Shape):
    def area(self):
            print("its square")



poly = [Shape(), Circle(), Square()]


for Shape in poly:
     Shape.area()



# Problem Title: Document Export System
# Difficulty: Medium
# OOP Concept: Polymorphism, Method Overriding

# 📝 Problem Description
# You are building a document export system that supports multiple document types.

# Implement a class Document with the following methods:

# export() → prints an export message (to be overridden by subclasses)

# file_size() → returns the size of the document in MB (to be overridden by subclasses)

# Implement three subclasses:

# PDFDocument

# WordDocument

# ExcelDocument

# Each subclass must override export() and file_size().


# object = # documents = [PDFDocument(), WordDocument(), ExcelDocument()]
# # export_all(documents)



class Document:
    def export(self):
        print("exported the doc")
    def file_size(self):
        print("the size of the document 2.5 MB")

class PDFDocument(Document):
    def export(self):
        print("exported the pdf")
    def file_size(self):
        print("the size of the document 3.5 MB")

class WordDocumentt(Document):
    def export(self):
        print("exported the word")
    def file_size(self):
        print("the size of the document 4 MB")

class ExcelDocument(Document):
    def export(self):
        print("exported the excel")
    def file_size(self):
        print("the size of the document 5 MB")


docs = [PDFDocument(),WordDocumentt(),ExcelDocument()]


for Document in docs:
    Document.export()
    Document.file_size()

              

