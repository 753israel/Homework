#1
#הדפסת מספרים
#כתוב קוד שמדפיס את כל המספרים מ־1 עד 20.
# for i in range(1,21):
#     print(i)

#2
#סכום רשימה
#קבל רשימת מספרים והדפס את סכומם בלי להשתמש ב־sum().
# numbers = [1,2,3,10]
# result = 0
# for i in numbers:
#     result += i
# print(result)

#3
# ספירת אותיות
#קבל מחרוזת והדפס כמה פעמים מופיעה האות 'a'.
# count = 0
# text = input("enter a string text:")
# for i in text:
#     if i in 'a':
#         count += 1
# print(count)

#4
#מספר זוגי או לא
#כתוב פונקציה שמקבלת מספר ומחזירה אם הוא זוגי.
# def odd_or_even(num):
#     if num % 2 == 0:
#         return f"the number is even {num}"
#     return f"the number is odd {num}"
# n = int(input("enter a number:"))
# print(odd_or_even(n))

#5
#רשימת שמות
#קבל 5 שמות מהמשתמש ושמור אותם ברשימה.
# name_list = []
# for i in range(5):
#     name = input("enter a name:")
#     name_list.append(name)
# print(name_list)

#6
#מספר גדול יותר
#כתוב פונקציה שמקבלת שני מספרים ומחזירה את הגדול מביניהם.
# def big_num(n1,n2):
#     if n1 > n2:
#         return f"the number is big {n1}"
#     else:
#         return f"the number is big {n2}"
#
# num1 = int(input("enter a number please:"))
# num2 = int(input("enter a number please:"))
# print(big_num(num1,num2))

#7
#הדפסת כל האיברים
#כתוב לולאה שמדפיסה כל איבר ברשימה.
# list_name = ["israel","rachel","orin","magi"]
# for name in list_name:
#     print(name)

#8
# מחרוזת הפוכה
#כתוב פונקציה שמחזירה מחרוזת הפוכה.
# def revers_string(s):
#     revers = s[::-1]
#     return revers
#
# text = input("enter a string please:")
# print(revers_string(text))

#9
#בדיקת סיסמה
#קבל סיסמה מהמשתמש. אם היא קצרה מ־8 תווים – הדפס "חלשה".
# def password_check(t):
#     if len(t) < 8:
#         return f"the password is weak !!!!"
#     return f"the password is strong !!!!"
#
# text = input("enter a password :")
# print(password_check(text))

#10
#מספר ראשוני
#כתוב פונקציה שבודקת אם מספר הוא ראשוני.
# def prime_number(num):
#     if num <= 1:
#         return f"{num} is not prime"
#     for i in range(2, num):
#         if num % i == 0:
#             return f"{num} is not prime"
#     return f"{num} is prime"
#
# n = int(input("enter a number i am cheek is prime or not :"))
# print(prime_number(n))



