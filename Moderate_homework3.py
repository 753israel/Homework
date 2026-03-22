#1
#כתוב פונקציה שמקבלת מחרוזת ומחזירה אותה ללא רווחים (כולל רווחים באמצע).

# def string_perfect(s):
#     l = s.split(" ")
#     b = ""
#     for h in l:
#         b += h
#     return b
#
# text = input("enter a string:")
# print(string_perfect(text))

#2
#קבל רשימת מספרים והחזר רשימה חדשה שמכילה רק את המספרים הגדולים מהממוצע.

# list_number = [2,8,6,8]
# list_big_avg = []
# result = sum(list_number)/len(list_number)
# for num in list_number:
#     if num > result:
#         list_big_avg.append(num)
# print(list_big_avg)


# עוד דרך
# def avg_list(numbers):
#     result = sum(numbers)/len(numbers)
#     return result
#
# list_numbers = [2,8,6,8]
# avg = avg_list(list_numbers)
# list_big = []
# for i in list_numbers:
#     if i > avg:
#         list_big.append(i)
# print(list_big)

#3
#כתוב פונקציה שמקבלת מחרוזת ומחזירה אותה כשהאות הראשונה בכל מילה היא גדולה.

# def big_first(s):
#     split_string = s.split()
#     word_new = split_string
#     w = ""
#     for word in range(len(word_new)):
#         w += str(word_new[word]).capitalize()+ " "
#
#     return w


# text = input("enter a string:")
# print(big_first(text))

#4
#כתוב פונקציה שמקבלת מחרוזת ומחזירה אותה כשהיא הפוכה, אבל רק האותיות — מספרים וסימנים נשארים במקום.
# def revers_new(s):
#     rev = ""
#     letters = []
#     # שלב 1: אוספים את כל האותיות
#     for ch in s:
#         if ch.isalpha():
#             letters.append(ch)
#     # שלב 2: הופכים את רשימת האותיות
#     letters = letters[::-1]
#     # שלב 3: בונים מחרוזת חדשה
#     for ch in s:
#         if ch.isalpha():
#             rev += letters.pop(0)   # לוקחים את האות הבאה מהרשימה ההפוכה
#         else:
#             rev += ch               # משאירים סימנים/מספרים במקום
#     return rev
#
# text = input("enter your string: ")
# print(revers_new(text))

#5
# כתוב פונקציה שמקבלת רשימת מספרים ומחזירה את המספר שמופיע הכי הרבה פעמים

# def number_is_big(numbers):
#     n = {}
#     max_count = 0
#     max_number = None
#
#     for i in numbers:
#         if i not in n:
#             n[i] = 1
#         else:
#             n[i] += 1
#
#     for k, v in n.items():
#         if v > max_count:
#             max_count = v
#             max_number = k
#
#     return max_number

# num = [2,6,5,2,1,6,6]
# print(number_is_big(num))


#6
#קבל מחרוזת והחזר מחרוזת חדשה שבה כל אות מופיעה פעמיים.
#לדוגמה: "abc" → "aabbcc".

# def double_string(s):
#     l = ""
#     for i in s:
#          l += i * 2
#     return l
#
# text = input("enter a string:")
# print(double_string(text))


#7
#קבל רשימת מילים והחזר רשימה חדשה של מילים שהאות האחרונה שלהן היא "a".

# def new_list(l):
#     new_list_end_a = []
#     for word in l:
#         if word.endswith("a"):
#             new_list_end_a.append(word)
#     return new_list_end_a

# list_word = ["pasta", "dog", "pizza", "cola", "tree"]
# print(new_list(list_word))


