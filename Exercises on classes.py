#1
#צור מחלקה  עם מאפיינים: חברה, דגם, שנה. Car
# class Car:
#     def __init__(self,company,model,year):
#         self.company = company
#         self.model = model
#         self.year = year
#
#     def __str__(self):
#         return (f'Company Car is :{self.company}, '
#                 f'Model Car is:{self.model},'
#                 f'Year Car is:{self.year}')
#
# car1 = Car("Nessan","GTR",2025)
# print(car1)

#2
#צור מחלקה  עם פעולות הפקדה ומשיכה.   BankAccount
# class BankAccount:
#     def __init__(self,account_balance):
#         self.account_balance = account_balance
#
#     def depositing_money(self,money):
#         self.account_balance += money
#         print(f"Deposited {money}$")
#
#     def cash_withdrawal(self,money):
#         if self.account_balance >= money:
#             self.account_balance -= money
#             print(f"Withdrew {money}$")
#         else:
#             print("Not enough money to withdraw")
#
#
#     def __str__(self):
#         return f'The money account is {self.account_balance}$'
#
#
# costumer1 = BankAccount(5000)
# costumer1.cash_withdrawal(5000)
# costumer1.depositing_money(1000)
# print(costumer1)

#4
#צור מחלקה  עם שם, גיל ורשימת ציונים. Student
#5
#הוסף ל־Student פונקציה שמחזירה ממוצע ציונים
# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self.grades = []
#     def add_score(self,s):
#         self.grades.append(s)
#     def avg_score(self):
#         if len(self.grades) == 0:
#             return 0
#         sum_all_grades = 0
#         for i in self.grades:
#             sum_all_grades += i
#         result =int( sum_all_grades / len(self.grades))
#         return result
#
# student1 = Student("Avi",35)
# student1.add_score(90)
# student1.add_score(80)
# student1.add_score(99)
# print(student1.avg_score())


#6
#צור מחלקה  עם פונקציה שמחזירה שטח והיקף.   Rectangle
# class Rectangle:
#     def __init__(self,width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def scope(self):
#         return 2 * (self.width + self.height)
#
#     def __str__(self):
#         return f'Rectangle width is:{self.width}, height is:{self.height}'
#
# r1 = Rectangle(5,5)
# print(r1.scope())
# print(r1.area())
# print(r1)

#7
#צור מחלקה  וממנה ירושה  ו־. Animal , Cat,Dog
# class Animal:
#     def __init__(self,name,age,color,voice):
#         self.name = name
#         self.age = age
#         self.color = color
#         self.voice = voice
#
#     def make_sound(self):
#         return f'The voice is : {self.voice}'
#
#     def __str__(self):
#         return (f'Name: {self.name} ,'
#                 f'Age: {self.age}'
#                 f'Color: {self.color}')
#
#
# class Cat(Animal):
#     def __init__(self, name, age, color, voice):
#         super().__init__(name, age, color,voice)
#
#
#     def make_sound(self):
#         self.voice = "Meow"
#         return f'The voice is : {self.voice}'
#
#     def __str__(self):
#         return f'{super().__str__()}'
#
#
# class Dog(Animal):
#     def __init__(self,name,age,color,voice):
#         super().__init__(name,age,color,voice)
#     def make_sound(self):
#         self.voice = "Auu"
#         return  f'The voice is : {self.voice}'
#
#     def __str__(self):
#         return f'{super().__str__()}'
#
# c = Cat("Mizi", 3, "White", "Meow")
# d = Dog("Rex", 5, "Brown", "Auu")
#
# print(c.make_sound())  # Meow
# print(d.make_sound())  # Auu
#
# print(c)
# print(d)
