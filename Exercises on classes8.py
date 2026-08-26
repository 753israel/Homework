#צור מחלקה בשם Car עם משתנה אחד color. צור אובייקט והדפס את הצבע.1
#הוסף למחלקה Car פונקציה drive() שמדפיסה "Driving...". צור אובייקט וקרא לפונקציה.2
# class Car:
#     def __init__(self,color):
#         self.color = color
#
#     def __str__(self):
#         return f"{self.color}"
#     def drive(self):
#         return "...Driving"
#
#
# c1 = Car("green")
# print(c1)
# print(c1.drive())

#צור מחלקה Person עם name ו־age. הוסף פונקציה introduce() שמדפיסה משפט עם השם והגיל.3
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def introduce(self):
#         return f'my name is {self.name} i am {self.age} years old'
#
# p1 = Person("israel",36)
# print(p1.introduce())

#צור מחלקה Rectangle עם width ו־height, והוסף פונקציה area() שמחזירה את השטח.4
# class Rectangle:
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return (self.width * self.height)
#
# r1 = Rectangle(16,3)
# print(r1.area())

#5
# class ShoppingCart():
#     def __init__(self):
#         self.items = []
#
#     def count_items(self):
#         total = 0
#         for item in self.items:
#             if item:
#                 total += 1
#         return total
#         # (or) total = len(self.items)
#     def remove_item(self,name):
#             if name in self.items:
#                 self.items.remove(name)
#                 return f'deleted'
#             else:
#                 return f'no name item'
#
#     def add_item(self,name):
#         self.items.append(name)
#
#     def __str__(self):
#         return f'{self.items}'
#
# s1 = ShoppingCart()
# s1.add_item("bisli")
# s1.add_item("bamba")
# print(s1.count_items())
# print(s1.remove_item("bamba"))
# print(s1)

# class LightSwitch:
#     def __init__(self,is_on = False):
#         self.is_on = is_on
#
#     def status(self):
#           if self.is_on:
#               return "ON"
#           else:
#               return "OFF"
#
#     def turn_off(self):
#         self.is_on = False
#
#
#     def turn_on(self):
#         self.is_on = True
#
#
#
# l1 = LightSwitch()
# print(l1.status())
# l1.turn_on()
# print(l1.status())
#
# l1.turn_off()
# print(l1.status())

class Speed:

    def __init__(self, kmh):
        self.kmh = kmh

    def to_mph(self):
        # מחזירים את החישוב מבלי לשנות את המהירות המקורית
        return self.kmh / 1.609

    def set_speed(self, new_speed):
        self.kmh = new_speed


# בדיקה
s = Speed(160)

print(s.to_mph())  # מדפיס בערך 99.44 (160 / 1.609)

s.set_speed(100)  # שינוי המהירות ל-100
print(s.kmh)  # מדפיס 100
print(s.to_mph())  # מדפיס בערך 62.15