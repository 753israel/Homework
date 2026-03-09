#1
# מחלקה עם רשימת אובייקטים
#צור מחלקה  שמחזיקה רשימת תלמידים.
#הוסף מתודה להוספת תלמיד ומתודה להצגת כל התלמידים.

# class Student:
#     def __init__(self,name,grade,age):
#         self.name = name
#         self.grade = grade
#         self.age = age
#
#     def __str__(self):
#         return f"Name: {self.name}, Grade: {self.grade}, Age: {self.age}"
#
#
# class StudentList:
#     def __init__(self):
#         self.students = []
#
#     def add_student(self,l):
#         self.students.append(l)
#
#     def __str__(self):
#         result = ""
#         for student in self.students:
#             result += str(student) +"\n"
#         return result
#
# student1 = Student("avi",68,17)
# student2 = Student("orin",99,16.5)
# student3 = Student("israel",88,16.8)
# s = StudentList()
# s.add_student(student1)
# s.add_student(student2)
# s.add_student(student3)
# print(s)

#2
# מחלקה בסיסית עם מאפיינים
#צור מחלקה שמייצגת מוצר בחנות.
#לכל מוצר יש: שם, מחיר וכמות במלאי.
#כתוב מתודה שמחזירה מחרוזת יפה שמציגה את כל המידע על המוצר.

# class Product:
#     def __init__(self,name,price,amount):
#         self.name = name
#         self.price = price
#         self.amount = amount
#
#     def __str__(self):
#         return f"Name Product:{self.name}\n Price:{self.price}\n Amount: {self.amount}"


#3
#מחלקה שמנהלת רשימה של אובייקטים
#צור מחלקה שמנהלת רשימה של מוצרים.
#הוסף מתודה להוספת מוצר לרשימה, ומתודה שמחזירה את כל המוצרים בצורה מסודרת.
# class ProductList:
#     def __init__(self):
#         self.products = []
#
#     def add_product(self,p):
#          self.products.append(p)
#
#     def __str__(self):
#         result = ""
#         for product in self.products:
#             result  += str(product) + "\n"
#         return result
#
# p1 = Product("Bamba",8.99,2)
# p2 = Product("Bisli",4.99,4)
# p3 = Product("tona",6.99,3)
# product_list = ProductList()
# product_list.add_product(p1)
# product_list.add_product(p2)
# product_list.add_product(p3)
# print(product_list)

#4
#מחלקה עם מתודה שמבצעת חישוב
#צור מחלקה שמייצגת עובד.
#לכל עובד יש: שם, שכר לשעה, מספר שעות עבודה.
#כתוב מתודה שמחזירה את השכר החודשי של העובד.

# class Employee:
#     def __init__(self,name,hourly_wage,hour_work):
#         self.name = name
#         self.hourly_wage = hourly_wage
#         self.hour_work = hour_work
#
#     def monthly_salary(self):
#         total = self.hourly_wage * self.hour_work
#         return total
#
#     def __str__(self):
#         return f"Employee Name :{self.name}\n Salary is month: {self.monthly_salary()}"
#
# emp1 = Employee("israel",50,180)
# emp1.monthly_salary()
# print(emp1)