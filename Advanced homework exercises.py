# #1
# #1.	כתוב פונקציה שמקבלת רשימה מקוננת (nested list) ומחזירה רשימה שטוחה.
#
# def flatten_list(l):
#     flat = []
#     for item in l:
#         if isinstance(item, list):      # אם הפריט הוא רשימה
#             flat.extend(flatten_list(item))   # נפתח אותה ונוסיף את התוכן שלה
#         else:
#             flat.append(item)           # אם זה מספר רגיל – נוסיף אותו
#     return flat
#
#
#
# def flatten_list_no_recursion(l):
#     stack = l[:]      # מעתיקים את הרשימה למחסנית
#     flat = []         # כאן תבוא הרשימה השטוחה
#     print(stack)
#     while stack:
#         item = stack.pop(0)   # מוציאים פריט מההתחלה
#
#         if isinstance(item, list):
#             stack = item + stack   # מוסיפים את תוכן הרשימה למחסנית
#         else:
#             flat.append(item)      # מספר רגיל → מוסיפים לרשימה השטוחה
#
#     return flat
#
# d = flatten_list_no_recursion([50,[[40,30],20],10])

#2
#כתוב פונקציה שמדמה זריקת קובייה 100 פעמים ומחזירה סטטיסטיקה
# import random
#
# def ra():
#     result = []
#     stats = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
#
#     # 100 זריקות
#     for i in range(100):
#         roll = random.randint(1, 6)
#         result.append(roll)
#         stats[roll] += 1   # מעלה את המונה של המספר שיצא
#
#     return stats
#
#
# print(ra())

#3
#כתוב פונקציה שמקבלת מחרוזת ומחזירה את המילה הארוכה ביותר
# def big_len_word(s):
#     big_words = s.split(" ")
#     result = big_words[0]
#     for i in big_words:
#         if len(i) > len(result):
#             result = i
#     return result

# words = input("enter a string:")
# print(big_len_word(words))

#4
#	כתוב אלגוריתם שממיין רשימה בלי להשתמש ב־sort.
# def sort_list(l):
#     temp = None
#     for i in range(len(l)):
#         for j in range(i+1,len(l)):
#             if l[i] > l[j]:
#                 temp = l[i]
#                 l[i] = l[j]
#                 l[j] = temp
#     return l
#
# num = [10,7,3,1]
# print(sort_list(num))


#5
#תוב פונקציה שמקבלת מספר ומחזירה את כל הצירופים האפשריים של ספרותיו.
# def addb(d):
#     d = str(d)  # הופך למחרוזת
#     if len(d) == 1:
#         return [d]
#
#     result = []
#     for i in range(len(d)):
#         for perm in addb(d[:i] + d[i+1:]):
#             result.append(d[i] + perm)
#
#     return result
#
#
#
# num = int(input("enter a number:"))
# print(addb(num))