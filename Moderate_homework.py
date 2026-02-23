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
