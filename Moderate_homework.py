# import random

#1
# כתוב תוכנית שבודקת אם מילה היא פלינדרום
# text = input("enter a words:")
# pal = text[::-1]
# if text == pal:
#     print("is Palindrome")
# else:
#     print("not Palindrome")

#2
#קבל רשימת מספרים והדפס את הממוצע שלהם.
# numbers = [10,15,17,22]
# result = sum(numbers) / len(numbers)
# print(f'The avg in numbers list is: {result}')

#3
#קבל מחרוזת והפוך כל אות גדולה לקטנה ולהפך.
# text = input("enter a string:")
# t = ""
# for i in text:
#     if i.isupper():
#         t += i.lower()
#     elif i.islower():
#         t += i.upper()
# print(t)

#4
#קבל מספר והדפס את כל המספרים הזוגיים עד אליו
# num = int(input("enter a number:"))
# for i in range(1,num):
#     if i %2 == 0:
#         print(i)

#5
#קבל רשימה והסר ממנה כפילויות
# numbers = [10,10,50,70]
# s = set(numbers)
# print(s)
# אם רוצים לשמור על הסדר אז עושים ככה
# numbers = [10, 10, 50, 70]
# unique = list(dict.fromkeys(numbers))
# print(unique)


#6
#קבל מחרוזת והדפס כמה פעמים כל אות מופיעה
# text = input("enter a string:")
# l = {}
# for i in range(len(text)):
#     count = 0
#     for j in range(len(text)):
#         if text[i] == text[j]:
#             count += 1
#     l[text[i]] = count
#
# print(l)

#7
#צור משחק ניחוש מספר בין 1 ל־10.
# rnd = random.randint(1, 10)
# num = int(input("enter a number: "))
#
# while num != rnd:
#     print("try again")
#     num = int(input("enter a number: "))
#
# print("you win")

#8
#קבל רשימת מילים והדפס רק את אלו שמתחילות באות מסוימת
# words = ["Apple", "banana", "peach", "cucumber", "avocado", "bell pepper", "eggplant"]
# new_list_words = []
# letter = input("enter a letter please:")
# for i in words:
#     if i.startswith(letter) :
#         new_list_words.append(i)
# print(new_list_words)


#9
# #קבל מספר והדפס את כל המחלקים שלו.
# num = int(input("enter a number please:"))
# for i in range(1,num+1):
#     if num % i == 0:
#         print(i)


#10
#קבל רשימת מספרים והדפס את המספר השני בגודלו.
# numbers = [10,30,50,60,20]
# temp = 0
# big =  0
# second_number = 0
# for i in numbers:
#     if big < i :
#         second_number = big
#         big = i
#     elif i < big and i > second_number:
#         second_number = i



# print(second_number)




