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