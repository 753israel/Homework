#1
#מילון של תלמידים
#צור מילון שבו המפתחות הם שמות תלמידים והערכים הם ציונים.
# students = {}
# question = int(input("How many students do you want to write down? "))
# for i in range(question):
#     name = input("enter a name: ")
#     val = float(input("enter a grade: "))
#     students[name] = val
#
# print(students)

#2
#מיון רשימה
#כתוב פונקציה שממיינת רשימה בלי להשתמש ב־.
#- לא להשתמש ב־list.sort()
#- לא להשתמש ב־sorted()
# num = [1,9,2,5]
# temp = num[0]
# for i in range(len(num)):
#     for j in range(i+1,len(num)):
#         if num[i] > num[j]:
#             temp = num[i]
#             num[i] = num[j]
#             num[j] = temp
# print(num)

#3
#ספירת מילים
#קבל משפט והחזר מילון שבו כל מילה מופיעה כמה פעמים.
# text = input("Please insert a sentence: ")
# list_count_word = {}
# word = text.split(" ")
# for i in word:
#     if i in list_count_word:
#         list_count_word[i] += 1
#     else:
#         list_count_word[i] = 1
# print(list_count_word)

#4
#עבודה עם קבצים
#כתוב קוד שפותח קובץ טקסט, כותב לתוכו 3 שורות, ואז קורא אותן.

# # פתיחת קובץ לכתיבה
# file = open("myfile.txt", "w", encoding="utf-8")
#
# # כתיבת 3 שורות לקובץ
# file.write("This is line 1\n")
# file.write("This is line 2\n")
# file.write("This is line 3\n")
#
# # סגירת הקובץ
# file.close()
# # פתיחת הקובץ לקריאה
# file = open("myfile.txt", "r", encoding="utf-8")
# # קריאת כל השורות
# content = file.read()
# # הדפסת התוכן
# print(content)
# # סגירת הקובץ
# file.close()


#5
#ספירת תווים במשפט
#קבל מהמשתמש משפט, והחזר מילון שבו כל תו (כולל רווח) מופיע כמה פעמים.
# text = input("Please insert a sentence: ")
# li = {}
# for i in text:
#     if i in li:
#         li[i] += 1
#     else:
#         li[i] = 1
#
# print(li)