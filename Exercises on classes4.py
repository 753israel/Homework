#1
#כתוב מחלקה בשם Car עם מאפיינים brand ו־year, ושיטה get_info שמחזירה מחרוזת עם פרטי הרכב.
# class Car:
#     def __init__(self, brand, year):
#         if year < 1885:
#             raise ValueError("Year must be 1885 or later — cars did not exist before that.")
#
#         self.brand = brand
#         self.year = year
#
#     def check_car(self):
#         if self.year < 1885:
#             return "Car is old"
#         else:
#             return "Car is new"
#
#     def get_info(self):
#         return f"Brand: {self.brand}, Year: {self.year}"
#
#
# # דוגמה תקינה
# car1 = Car("Mazda", 2023)
# print(car1.get_info())
# print(car1.check_car())

# דוגמה שתגרום לחריגה
#car2 = Car("Ford", 1700)



#2
#. שימוש ב־__init__
#הרחב את המחלקה Car כך שתבדוק אם השנה גדולה מ־1885 (שנת המצאת הרכב). אם לא — תזרוק חריגה.

#3
#צור מחלקה ElectricCar שיורשת מ־Car ומוסיפה מאפיין battery_capacity.
#הוסף שיטה שמחזירה את זמן הטעינה המשוער לפי נוסחה כלשהי.

# class ElectricCar(Car):
#     def __init__(self, brand, year, km, speed, battery_capacity):
#         super().__init__(brand, year)
#         self.km = km
#         self.speed = speed
#         self.battery_capacity = battery_capacity
#
#     def battery_capacity_now(self):
#         # לדוגמה: כמה אחוז סוללה נצרך לכל ק"מ
#         consumption = self.km / self.speed
#         return f"Battery consumption estimate hours: {consumption:.2f}"
#
#
#
# e1 = ElectricCar("Tesla", 2022, 150, 75, 100)
# print(e1.get_info())
# print(e1.battery_capacity_now())

# שאלה 4 — מחלקת Student
# צור מחלקה בשם Student עם:
# שם (name)
# גיל (age)
# רשימת ציונים (grades)
# הוסף פונקציות:
#
# add_grade(grade) — מוסיפה ציון
#
# get_average() — מחזירה ממוצע ציונים
#
# is_passing() — מחזירה True אם הממוצע ≥ 60

# class Student:
#     def __init__(self,name,age,grades=None):
#         self.name = name
#         self.age = age
#         self.grades = grades if grades is not None else []
#
#     def add_grade(self,grade):
#         self.grades.append(grade)
#
#     def get_average(self):
#         s = sum(self.grades)
#         result = s / len(self.grades)
#         return result
#
#     def is_passing(self):
#         return self.get_average() >=60
#
# s1 = Student("David", 17)
# s1.add_grade(80)
# s1.add_grade(50)
# s1.add_grade(70)
#
# print(s1.get_average())   # 66.6
# print(s1.is_passing())    # True
#########################################
# שאלה 5 — מחלקת BankAccount
# צור מחלקה בשם BankAccount עם:
# שם בעל החשבון
# יתרה התחלתית
# פעולות:
# deposit(amount) — מפקיד כסף
#
# withdraw(amount) — מושך כסף (אם אין מספיק — זרוק חריגה)
#
# get_balance() — מחזיר יתרה

# class BankAccount:
#     def __init__(self, name_account, account_balance=0):
#         self.name_account = name_account
#         self.account_balance = account_balance
#
#     def deposit(self, amount):
#         if amount <= 0:
#             raise ValueError("Deposit amount must be positive")
#         self.account_balance += amount
#
#     def withdraw(self, amount):
#         if amount <= 0:
#             raise ValueError("Withdraw amount must be positive")
#         if amount > self.account_balance:
#             raise ValueError("Insufficient funds")
#         self.account_balance -= amount
#
#     def get_balance(self):
#         return self.account_balance
#
#     def __str__(self):
#         return f"Name: {self.name_account}\nAccount Balance: {self.account_balance}"
#
# acc = BankAccount("Israel", 500)
#
# acc.deposit(200)
# print(acc.get_balance())   # 700
#
# acc.withdraw(150)
# print(acc.get_balance())   # 550
#
# print(acc)
#####################################################################
#6
#מחלקה Book
# class Book:
#     def __init__(self, title, author, year, is_borrowed=False):
#         self.title = title
#         self.author = author
#         self.year = year
#         self.is_borrowed = is_borrowed
#
#     def borrow(self):
#         if self.is_borrowed:
#             raise ValueError("Book is already borrowed")
#         self.is_borrowed = True
#
#     def return_book(self):
#         if not self.is_borrowed:
#             raise ValueError("Book was not borrowed")
#         self.is_borrowed = False
#
#     def get_info(self):
#         return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"
#
# class Library:
#     def __init__(self):
#         self.books = []
#
#     def add_book(self, book):
#         self.books.append(book)
#
#     def remove_book(self, title):
#         for book in self.books:
#             if book.title == title:
#                 self.books.remove(book)
#                 return
#         raise ValueError("Book not found in library")
#
#     def find_book(self, title):
#         for book in self.books:
#             if book.title == title:
#                 return book
#         return None
#
#     def get_available_books(self):
#         available = []
#         for book in self.books:
#             if not book.is_borrowed:
#                 available.append(book)
#         return available
#
#
# class DigitalBook(Book):
#     def __init__(self, title, author, year, file_size, file_format, is_borrowed=False):
#         super().__init__(title, author, year, is_borrowed)
#         self.file_size = file_size      # במגה־בייט
#         self.file_format = file_format  # PDF, EPUB וכו'
#
#     def download_time(self, speed):
#         if speed <= 0:
#             raise ValueError("Speed must be positive")
#
#         time = self.file_size / speed
#         return f"Estimated download time: {time:.2f} seconds"
# d = DigitalBook("Python Guide", "Guido", 2020, 50, "PDF")
#
# print(d.get_info())
# print(d.download_time(10))   # 5.00 seconds
################################################
#7
# class TodoList:
#     def __init__(self):
#         self.tasks = []
#
#     def add_task(self, task):
#         self.tasks.append(task)
#
#     def remove_task(self, task):
#         for t in self.tasks:
#             if t == task:
#                 self.tasks.remove(t)
#                 return
#         raise ValueError("Task not found")
#
#     def has_task(self, task):
#         for t in self.tasks:
#             if t == task:
#                 return True
#         return False
#
#     def count(self):
#         return len(self.tasks)
#
#     def get_all(self):
#         return self.tasks





