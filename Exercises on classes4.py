#1
#כתוב מחלקה בשם Car עם מאפיינים brand ו־year, ושיטה get_info שמחזירה מחרוזת עם פרטי הרכב.
class Car:
    def __init__(self, brand, year):
        if year < 1885:
            raise ValueError("Year must be 1885 or later — cars did not exist before that.")

        self.brand = brand
        self.year = year

    def check_car(self):
        if self.year < 1885:
            return "Car is old"
        else:
            return "Car is new"

    def get_info(self):
        return f"Brand: {self.brand}, Year: {self.year}"


# דוגמה תקינה
car1 = Car("Mazda", 2023)
print(car1.get_info())
print(car1.check_car())

# דוגמה שתגרום לחריגה
#car2 = Car("Ford", 1700)



#2
#. שימוש ב־__init__
#הרחב את המחלקה Car כך שתבדוק אם השנה גדולה מ־1885 (שנת המצאת הרכב). אם לא — תזרוק חריגה.

#3
#צור מחלקה ElectricCar שיורשת מ־Car ומוסיפה מאפיין battery_capacity.
#הוסף שיטה שמחזירה את זמן הטעינה המשוער לפי נוסחה כלשהי.

class ElectricCar(Car):
    def __init__(self, brand, year, km, speed, battery_capacity):
        super().__init__(brand, year)
        self.km = km
        self.speed = speed
        self.battery_capacity = battery_capacity

    def battery_capacity_now(self):
        # לדוגמה: כמה אחוז סוללה נצרך לכל ק"מ
        consumption = self.km / self.speed
        return f"Battery consumption estimate hours: {consumption:.2f}"



e1 = ElectricCar("Tesla", 2022, 150, 75, 100)
print(e1.get_info())
print(e1.battery_capacity_now())
