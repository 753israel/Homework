"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

i = Person("Israel", 36)
print(i.greet())

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return f"Name: {self.name}\nPrice: {self.price}₪"

b = Product("Bamba", 5.5)
print(b.info())

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def show(self):
        return f"({self.x}, {self.y})"


p = Point(3, 7)
print(p.show())   # לפני הזזה

p.move(2, -1)
print(p.show())   # אחרי הזזה

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        return f"Title: {self.title}, Author: {self.author}"

b = Book("BK", "Avi")
print(b.describe())

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return self.celsius * 1.8 + 32

t = Temperature(50)
print(f"{t.to_fahrenheit()}°F")



class Cart:
    def __init__(self):
        self.list_cart = []

    def add_product(self, name, price):
        self.list_cart.append((name, price))

    def total_price(self):
        total = 0
        for product in self.list_cart:
            total += product[1]   # המחיר
        return total

    def remove_product(self, name):
        for product in self.list_cart:
            if product[0] == name:   # השם
                self.list_cart.remove(product)
                return
        raise ValueError("Product not found")
c = Cart()
c.add_product("Bamba", 5.5)
c.add_product("Bisli", 4)

print(c.total_price())   # 9.5

c.remove_product("Bamba")
print(c.total_price())   # 4


class Student:
    def __init__(self,name):
        self.name = name
        self.score = []

    def add_grade(self,grade):
        self.score.append(grade)
    def average(self):
        sum = 0
        total = len(self.score)
        for i in self.score:
            sum += i
        return sum / total

    def passed(self):
        if self.average() > 60:
            return True
        return False

s = Student("Israel")
s.add_grade(90)
s.add_grade(70)
s.add_grade(50)

print(s.average())   # 70
print(s.passed())    # True

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
        else:
            return "Not enough money"

    def show_balance(self):
        return f"Balance: {self.balance}"


b = BankAccount("Israel", 5000)

print(b.deposit(100))
print(b.show_balance())

print(b.withdraw(2000))
print(b.show_balance())

class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, name, length):
        self.songs.append((name, length))

    def total_length(self):
        total = 0
        for song in self.songs:
            total += song[1]   # אורך השיר
        return total

    def find_song(self, name):
        for song in self.songs:
            if song[0] == name:
                return song
        return "not found"
p = Playlist()
p.add_song("Hello", 3.5)
p.add_song("World", 4)

print(p.total_length())      # 7.5
print(p.find_song("Hello"))  # ('Hello', 3.5)
print(p.find_song("ABC"))    # not found

______________________________________________________________
'1. כתוב פונקציה שמקבלת מספר ומחזירה אם הוא זוגי או אי־זוגי.'
def even(n):
    if n % 2 == 0:
        return f"is even"
    else:
        return f'not even'
num = int(input("enter a number:"))
print(even(num))

'2. קבל מהמשתמש מחרוזת והדפס כמה תווים יש בה.'
def numstring(s):
    return len(s)
st = input("enter a word:")
print(numstring(st))

' 3 כתוב לולאה שמדפיסה את כל המספרים מ־1 עד 50, אבל רק את אלה שמתחלקים ב־5.'
for i in range(1,51):
    if i % 5 == 0:
        print(i,end=",")


'4 כתוב פונקציה שמקבלת רשימת מספרים ומחזירה את הממוצע שלהם.'
def avg(n):
    s = sum(n)
    avg1 = s / len(n)
    return avg1
num = [10,10]
print(avg(num))

'5 קבל מהמשתמש משפט והפוך אותו (מילה אחרונה ראשונה).'
def reverse_sentence(s):
    words = s.split()
    return " ".join(words[::-1])

st = input("enter a sentence: ")
print(reverse_sentence(st))



'כתוב תוכנית שבודקת אם מילה היא פלינדרום (נקראת אותו דבר מהסוף להתחלה).'
def ispla(s):
    w = s[::-1]
    if w == s:
        return True
    else:
        return False

st = input("enter a str :")
print(ispla(st))
"""
"""
רמה מתקדמת


8. כתוב פונקציה שמקבלת רשימת מילים ומחזירה מילון שבו המפתח הוא המילה והערך הוא מספר ההופעות שלה.

9. כתוב פונקציה שמקבלת מספר N ומחזירה את כל המספרים הראשוניים עד N.

10. כתוב סימולציה פשוטה: יש רשימת אנשים, כל אחד עם גיל. צור רשימה חדשה שמכילה רק את האנשים מעל גיל 18.

'7. כתוב מחלקה בשם BankAccount עם פעולות: הפקדה, משיכה, והצגת יתרה.'
class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
        
    def deposit(self,num):
        self.balance += num
            return f"Deposited {num}. New balance: {self.balance}
            
    def withdraw(self,money):
        if self.balance >= money:
            self.balance -= money
                return f"Withdrawal from the account:{money},You have a remaining balance in your account {self.balance}"
        else:
           return f"You don't have enough money in your account."
           
    def view_balance(self):
        return f"{self.owner}, your balance is: {self.balance}


isr = BankAccount("israel",5000)
isr.deposit(500)
print(isr.view_balance())
isr.withdraw(5000)
print(isr.view_balance())
"""