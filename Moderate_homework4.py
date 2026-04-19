#1.
#ספירת מילים: כתוב פונקציה שמקבלת מחרוזת ומחזירה מילון שבו המפתח הוא המילה והערך הוא מספר הפעמים שהיא הופיעה.

# def con_dic(s):
#     dic = {}
#     sp = s.split(" ")
#     for i in sp:
#        if i not in dic:
#             dic[i] = 1
#        else:
#         dic[i] += 1
#     return dic
# text = input("enter a word please:")
# print(con_dic(text))

#2.
# סינון רשימה: כתוב "List Comprehension" שיוצר רשימה חדשה רק מהמספרים הזוגיים בתוך רשימה קיימת, ומכפיל אותם ב-10.

# list_even = []
# list_all = [10,5,7,8,11,13]
# for i in list_all:
#     if i % 2 == 0:
#         list_even.append(i*10)
# print(list_even)
#
# list_all_number = [10,5,7,8,11,13]
# list_new_even = [i * 10 for i in list_all_number if i % 2 == 0]
# print(list_new_even)

#3.
#הסרת כפילויות: כתוב פונקציה שמקבלת רשימה עם איברים כפולים ומחזירה רשימה עם איברים ייחודיים בלבד בלי להשתמש ב-set.

# def list_unique(l):
#     list_new = []
#     for i in l:
#         if i not in list_new:
#             list_new.append(i)
#
#     return list_new
#
# number_list = [9,9,5,7,3,5,3]
# print(list_unique(number_list))

# #4
# #פונקציית ממוצע גמישה: כתוב פונקציה שמשתמשת ב-*args כדי לקבל מספר לא ידוע של מספרים ומחזירה את הממוצע שלהם.
#
# def average(*args):
#     length = len(args)
#     result = sum(args)
#     total  = result / length
#     return total
#
# print(average(10,20,30))

#5
#בדיקת פלינדרום: כתוב פונקציה שבודקת אם מחרוזת היא פלינדרום (נקראת אותו דבר מהסוף להתחלה), תוך התעלמות מרווחים ואותיות גדולות/קטנות.
#זה פלינדרום רגיל
# def pal(s):
#     t = s[::-1]
#     if t == s:
#         return True
#     return False
# # זה לפי השאלה
# def pal1(s):
#     s = s.replace(" ", "").lower()
#     return s == s[::-1]
#
#
# text = input("enter a pal:")
# print(pal(text))
# # Bab (False)
# text1 = input("enter a pal:")
# print(pal1(text))
# # Bab(True)

#6
#ניהול קבצים: כתוב סקריפט שפותח קובץ טקסט בשם data.txt, קורא את כל השורות בו, ומדפיס רק את השורות שמתחילות במילה "Python".

# text = open("data.txt","r")
# row = text.readlines()
# for i in row:
#     if i.startswith("Python"):
#         print(i, end="")
# print()
#
# with open("data.txt", "r") as text:
#     for line in text:
#         if line.startswith("Python"):
#             print(line, end="")




