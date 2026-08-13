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