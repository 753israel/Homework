#צור מילון של תלמיד עם השדות: שם, גיל, כיתה. הדפס את הגיל בלבד.1
d ={"name":"israel","age":35,"class":"A1"}
print(d["age"])

# #2יש מילון:
# grades = {"math": 90, "english": 85, "history": 70}
# הוסף מקצוע חדש בשם "science" עם ציון 95.
grades = {"math": 90, "english": 85, "history": 70,"science":95}

#3כתוב קוד שמקבל מילון ומדפיס את כל המפתחות שלו בשורה אחת.
d ={"name":"israel","age":35,"id":305558878}
for k in d.keys():
    print(k,end=" ")

#4כתוב קוד שמקבל מילון ומדפיס את כל הערכים שלו בשורה אחת.
d ={"name":"israel","age":35,"id":305558878}
for i in d.values():
    print(i,end=" ")

#5.יש מילון:
# person = {"name": "David", "age": 30, "city": "Haifa"}
# שנה את הערך של "city" ל־"Tel Aviv".

person = {"name": "David", "age": 30, "city": "Haifa"}
person["city"] = "Tel Aviv"
print(person)

#6.כתוב פונקציה שמקבלת מילון ומחזירה את מספר הזוגות (key:value) שיש בו.
def num(d):
    i = 0
    for k in d.keys():
        if k:
            i +=1
    return i


person = {"name": "David", "age": 30, "city": "Haifa"}
print(num(person))

#7.יש מילון:
# prices = {"apple": 3, "banana": 2, "orange": 4}
# מחק את הפריט "banana".

prices = {"apple": 3, "banana": 2, "orange": 4}
prices.pop("banana")
print(prices)

#8.כתוב קוד שמקבל מילון ומדפיס כל מפתח וכל ערך בפורמט:
#key -> value

prices = {"apple": 3, "banana": 2, "orange": 4}
for k,v in prices.items():
    for k, v in prices.items():
      print(k, "->", v)

#9יש שני מילונים:
# a = {"x": 1, "y": 2}
# b = {"y": 3, "z": 4}
# איחד אותם למילון אחד (כאשר ערכים כפולים – ערך של b גובר).


a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}
c ={}
for k, v in a.items():
    c[k] = v
for k, v in b.items():
    c[k] = v
print(c)

#10.כתוב פונקציה שמקבלת מילון של שמות וציונים, ומחזירה את השם עם הציון הגבוה ביותר.
def max_grade_student(grades):
    best_name = None      # השם הכי טוב שמצאנו עד עכשיו
    best_sum = -1         # סכום הציונים הכי גבוה שמצאנו

    for name, subjects in grades.items():  # name = "israel", subjects = {"math": 90, ...}
        current_sum = 0
        for score in subjects.values():    # עובר על כל הציונים של התלמיד
            current_sum += score

        if current_sum > best_sum:         # אם הסכום של התלמיד הזה יותר גדול מהשיא
            best_sum = current_sum         # מעדכן את השיא
            best_name = name               # מעדכן את השם של התלמיד

    return best_name



grade = {
    "israel": {"math": 90, "english": 85, "history": 70},
    "orin":   {"math": 95, "english": 80, "history": 88},
    "yossi":  {"math": 70, "english": 92, "history": 60}
}
print(max_grade_student(grade))

