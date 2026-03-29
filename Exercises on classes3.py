#1
#כתוב מחלקה בשם  עם מאפיינים:
#הוסף מתודה שמחזירה מחרוזת המתארת את הרכב.

# class Car:
#     def __init__(self,year,brand):
#         self.year = year
#         self.brand = brand
#
#     def __repr__(self):
#         return f'Year:{self.year},Brand:{self.brand}'


#2
#צור מחלקה ElectricCar שיורשת מ־Car ומוסיפה מאפיין battery_capacity .
#האם צריך לכתוב מחדש את ה־__init__? הסבר.

# class ElectricCar(Car):
#     def __init__(self,year,brand,battery_capacity):
#         super().__init__(year,brand)
#         self.battery_capacity = battery_capacity
#
#     def __str__(self):
#         return f'{super().__str__()},Battery_Capacity:{self.battery_capacity}'
#
#
# car1 = Car(2018, "Mazda")
# car2 = Car(2022, "Hyundai")
#
# electric1 = ElectricCar(2024, "Tesla", 100)
# electric2 = ElectricCar(2025, "BYD", 60)
#
# print(car1)
# print(car2)
# print(electric1)
# print(electric2)

#3. פולימורפיזם
#כתוב שתי מחלקות: Dog ו־Cat, שלכל אחת מתודה make_sound.
#כתוב פונקציה שמקבלת רשימת חיות ומפעילה את המתודה על כל אחת

# class Cat:
#     def __init__(self,name,type,sound):
#         self.name = name
#         self.type = type
#         self.sound = sound
#
#     def make_sound(self):
#         return f"{self.sound}"
#
#     def __str__(self):
#         return f'Name:{self.name}\n Type:{self.type}\n Sound:{self.sound}'
#
# class Dog:
#     def __init__(self,name,type,sound):
#         self.name = name
#         self.type = type
#         self.sound = sound
#
#     def make_sound(self):
#         return f"{self.sound}"
#
#     def __str__(self):
#         return f'Name:{self.name}\n Type:{self.type}\n Sound:{self.sound}'
#
#
# cat1 = Cat("Mizi","Cat","Miwo")
# cat2 = Cat("Clara","Cat","Miwo")
# dog1 = Dog("lossi","Dog","ooooo")
# dog2 = Dog("moki","Dog","ooooo")
# print(cat1.make_sound())
# print(cat2.make_sound())
# print(dog1.make_sound())
# print(dog2.make_sound())

class Cat:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Meow"

    def __str__(self):
        return f"Cat: {self.name}"


class Dog:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Woof"

    def __str__(self):
        return f"Dog: {self.name}"


def animal_sounds(animals):
    for animal in animals:
        print(f"{animal}: {animal.make_sound()}")


cat1 = Cat("Mizi")
cat2 = Cat("Clara")
dog1 = Dog("Lossi")
dog2 = Dog("Moki")

animals = [cat1, cat2, dog1, dog2]
animal_sounds(animals)
