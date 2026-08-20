# "1. כתוב פונקציה שמקבלת מספר ומחזירה את סכום כל הספרות שלו."
# def s(n):
#     nu = 0
#     while n > 0:
#         nu += n % 10
#         n = n//10
#     return nu
# num1 = int(input("enter a number:"))
# print(s(num1))

# "2.קבל מהמשתמש מחרוזת ובדוק אם היא מכילה רק אותיות (ללא מספרים)."
# def s(st):
#     for i in st:
#         if i.isdigit():
#             print("string is digit")  # הודעה אם נמצאה ספרה
#             return False
#     print("string is perfect")  # הודעה אם עברנו את כל הלולאה ואין ספרות
#     return True
# stri = input("enter a word: ")
# print(s(stri))

#3. כתוב לולאה שמדפיסה את כל המספרים מ־1 עד 100, אבל עוצרת ברגע שמספר מתחלק ב־17.
# for i in range(1,101):
#     if i % 17 == 0:
#         print(i)
#         break
#4. כתוב פונקציה שמקבלת רשימת מספרים ומחזירה רשימה חדשה שמכילה רק את המספרים הזוגיים.
# def listnumber(n):
#     lis =[]
#     for i in n:
#         if i % 2 == 0:
#             lis.append(i)
#     return lis
# l = [10,50,77,85,27]
# print(listnumber(l))
#כתוב פונקציה שמקבלת מחרוזת ומחזירה מילון שבו כל תו הוא מפתח ומספר ההופעות שלו הוא הערך.
# def st(s):
#     dic = {}
#     for i in s:
#         if i not in dic:
#             dic[i] = 1
#         else:
#             dic[i] += 1
#     return dic
# d = "hello"
# print(st(d))
#כתוב תוכנית שמקבלת מהמשתמש משפט, ומחזירה את המילה הארוכה ביותר במשפט.
# def str_big(st):
#     s = st.split(" ")
#     d = ""
#     l1 = 0
#     l2 = len(d)
#     for i in s:
#         if len(i) > len(d):
#             d = i
#     return d
# word = input("Insert a sentence in English:")
# print(str_big(word))
#כתוב מחלקה בשם Rectangle עם שדות: רוחב וגובה.
#הוסף פעולות:
#חישוב שטח
#חישוב היקף
#השוואה בין שני מלבנים (מי גדול יותר בשטח)
# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def area(self):
#         return self.w * self.h
#
#     def perimeter(self):
#         return (self.h * 2) + (self.w * 2)
#
#     def big(self, other):
#         # משווה את השטח של המלבן הנוכחי (self) מול מלבן אחר (other)
#         if self.area() > other.area():
#             return self
#         else:
#             return other
#
#
# s1 = Rectangle(10, 20)
# print("Area 1:", s1.area())
# print("Perimeter 1:", s1.perimeter())
#
# s2 = Rectangle(10, 30)
# print("Area 2:", s2.area())
# print("Perimeter 2:", s2.perimeter())
#
#
# larger_rect = s1.big(s2)
# print("The larger rectangle's area is:", larger_rect.area())

#כתוב סימולציה: יש רשימת אנשים, כל אחד מיוצג כ־dict עם שם וגיל.
#צור רשימה חדשה שמכילה רק את האנשים מעל גיל 18.
# people = [
#     {"name": "Avi", "age": 17},
#     {"name": "Dana", "age": 22},
#     {"name": "Ron", "age": 30}
# ]
# dic = []
# for i in people:
#     if i["age"] > 18:
#         dic.append(i)
# print(dic)

#10. כתוב מחלקה בשם Library:
#יש לה רשימת ספרים
#כל ספר הוא אובייקט עם שם ומחבר
#הוסף פעולות:
#הוספת ספר
#מחיקת ספר לפי שם
#חיפוש ספר לפי מחבר
#ספירת כמות הספרים בספרייה
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
#
# class Library:
#     def __init__(self):
#         self.books = []  # רשימת ספרים
#
#     def add_book(self, title, author):
#         # יוצר אובייקט ספר חדש ומוסיף אותו לרשימה
#         b = Book(title, author)
#         self.books.append(b)
#
#     def delete_book(self, title):
#         # עובר על הספרים ומוחק את הספר שהשם שלו תואם
#         for book in self.books:
#             if book.title == title:
#                 self.books.remove(book)
#                 break
#
#     def find_by_author(self, author):
#         # מחזיר רשימה של כל הספרים שנכתבו על ידי מחבר מסוים
#         result = []
#         for book in self.books:
#             if book.author == author:
#                 result.append(book.title)
#         return result
#
#     def count_books(self):
#         # מחזיר את כמות הספרים בספרייה בעזרת len
#         return len(self.books)
#
#
# # בדיקה:
# lib = Library()
# lib.add_book("Python 101", "John Doe")
# lib.add_book("Advanced Python", "Jane Smith")
# lib.add_book("Data Science", "John Doe")
#
# print("Total books:", lib.count_books())  # ידפיס 3
# print("Books by John Doe:", lib.find_by_author("John Doe"))
#
# lib.delete_book("Python 101")
# print("Total books after deletion:", lib.count_books())  # ידפיס 2