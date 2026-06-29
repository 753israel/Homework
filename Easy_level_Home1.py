#1. קבל מספר מהמשתמש והדפס אם הוא חיובי, שלילי או אפס.
num = float(input("Enter a number: "))
if num > 0:
    print(f"The number {num} is positive.")
elif num < 0:
    print(f"The number {num} is negative.")
else:
    print("The number is zero.")

#2. קבל שתי מילים והדפס איזו מהן ארוכה יותר (או אם הן שוות).
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

if len(word1) > len(word2):
    print(f"The longer word is: {word1}")
elif len(word2) > len(word1):
    print(f"The longer word is: {word2}")
else:
    print("Both words have the same length.")

#3. קבל מספר והדפס את כל המספרים הזוגיים עד אליו.
num = int(input("Enter a number: "))

for i in range(1, num + 1):
    if i % 2 == 0:
        print(i)

#4. קבל מחרוזת והדפס כמה פעמים מופיעה האות 'a' (או כל אות שהמשתמש יבחר).
word = input("Enter a word: ")
letter = input("Enter a letter to count: ")

count = 0
for w in word:
    if w == letter:
        count += 1

print(f"The letter '{letter}' appears {count} times.")
#########################################דרך שניה
word = input("Enter a word: ")
print(word.count('a'))

#5. קבל מספר והדפס את כל החזקות שלו מ‑1 עד 5 (num¹, num², num³...).
num = int(input("Enter a number: "))

for i in range(1, 6):
    print(f"{num}^{i} = {num**i}")


#6. קבל מילה והדפס אם היא פלינדרום (נקראת אותו דבר מהסוף ומההתחלה).
word = input("enter a word:")
new_word = word[::-1]
if word == new_word:
    print("is palindrom")
else:
    print("not palindrom")
#7. קבל שלושה מספרים והדפס את הממוצע שלהם.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

total = num1 + num2 + num3
average = total / 3

print(f"The average is: {average}")

#8. קבל מחרוזת והדפס אותה כשהאות הראשונה גדולה (capitalize) בלי להשתמש ב‑.capitalize()
word = input("enter a word: ")
new_word = word[0].upper()

for i in range(1, len(word)):
    new_word += word[i]

print(new_word)

#9. קבל מספר והדפס את סכום כל המספרים מ‑1 עד אליו (ללא לולאה — רק נוסחה).
num = int(input("Enter a number: "))
result = num * (num + 1) // 2
print(result)

#10. קבל רשימת מספרים מהמשתמש (עם split) והדפס את המספר הגדול ביותר.
nums = input("Enter numbers separated by space: ").split()
nums = [float(n) for n in nums]
print(max(nums))
