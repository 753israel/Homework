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
#
# def count_uniq(s):
#     s = s.replace(" ", "").lower()   # מנקה רווחים ומתעלם מאותיות גדולות
#     word_list = {}
#     for char in s:
#         if char in word_list:        # אם התו כבר הופיע
#             word_list[char] += 1
#         else:                        # אם זו הפעם הראשונה
#             word_list[char] = 1
#     return word_list
#שאלה 7 — ספירת תווים ללא רווחים
#כתוב פונקציה שמקבלת מחרוזת ומחזירה מילון שבו כל תו (חוץ מרווח) הוא מפתח
# , והערך הוא מספר הפעמים שהוא הופיע.
# def string_uniq(st):
#     st = st.replace(" ","")
#     word_list = {}
#     for char in st:
#         if char in word_list:
#             word_list[char] += 1
#         else:
#             word_list[char] = 1
#     return word_list
#
#
#
#
# word = input("enter a word:")
#
# print(string_uniq(word))
#
#שאלה 8 — סינון מילים ארוכות
#קבל רשימת מילים והחזר רשימה חדשה שמכילה רק מילים שאורכן גדול מ־4 תווים.
# word = ["cat", "apple", "dog", "banana", "tree"]
# n_word = []
# for new_word in word:
#     if len(new_word) > 4:
#         n_word.append(new_word)
# print(n_word)
#
#שאלה 9 — סכום מספרים זוגיים
#כתוב פונקציה שמקבלת רשימת מספרים ומחזירה את סכום כל המספרים הזוגיים בלבד.
# def sum_even(lis_num):
#     result = 0
#     for i in lis_num:
#         if i % 2 == 0:
#             result += i
#     return result
#
# num = [1, 4, 7, 2, 10, 5]
# print(sum_even(num))
#
#שאלה 4 — מיזוג שתי רשימות
#כתוב פונקציה שמקבלת שתי רשימות
# ומחזירה רשימה חדשה שמכילה את כל האיברים של שתיהן, ללא כפילויות.

# def fix(lis_num1,lis_num2):
#     lis_new = []
#     for i in lis_num1:
#         if i not in lis_new:
#             lis_new.append(i)
#     for j in lis_num2:
#         if j not in lis_new:
#             lis_new.append(j)
#     return lis_new
#
# num1 = [1, 2, 3]
# num2 = [3, 4, 5]
# print(fix(num1,num2))
#דרך שניה
# def fix(lis_num1, lis_num2):
#     lis = []
#     lis += lis_num1 + lis_num2  # מאחד לרשימה אחת
#     s = set(lis)                # הופך ל-set כדי להוריד כפילויות
#     lis = s                     # משנה את שם המשתנה (מיותר)
#     lis1 = list(lis)            # מחזיר לרשימה
#     return lis1
#
#
#
# num1 = [1,2,3]
# num2 = [3,4,5]
# print(fix(num1,num2))