# Class -> Blueprint for creating object
# aka Related information bundled toghter
# It contains two things
# 1. Data (Properties)
# 2. Methods (Function)


# Majority time we define class with Pascal Case or Upper Camel case
# First Letter of every word in CAPITAL
class Car:
    # Intilizer aka Constructor in Python
    def __init__(self, model: str, brand: str) -> None:
        # Self refers the current instance of the class , we can called it anything but by convation we called as self
        # It is similar to this keyword in java / javascript
        # By Mentioning self in to the method / function parameter that function became part of the instance
        self.model: str = model  # Data
        self.brand: str = brand  # Data
        self.is_ev: bool = False

    # Method
    def make_it_ev(self) -> None:
        if self.is_ev:
            print(f"{self.model} is already EV :)")
        else:
            self.make_it_ev = True
            print(f"{self.model} is Now convert to EV :)")
            print("SAVE EARTH 🌏🌍🌎")

    # Dunder methods
    def __add__(self, other):
        return f"{self.model} + {other.model} became super car"

    def __mul__(self, num: int):
        return f"{self.model * num} "

    def __str__(self):  # Usefull for printing or direct use of object
        return f"{self.model} belongs to {self.brand} brand"

    def __repr__(self):  # usedull for developer for represention
        return f"Car(model='{self.model}',brand='{self.brand}')"

    def lol():
        return "Hi LOl"


# ob1: Car = Car("Model S", "Tesla")  # instance of the class
# ob1.is_ev = True

# print(ob1.model)
# print(ob1.brand)
# ob1.make_it_ev()

# ob2: Car = Car("Porshe 911", "Porshe")  # instance of the class
# print(ob2.model)
# print(ob2.brand)
# ob2.make_it_ev()
# print(repr(ob2))
# print(ob1 + ob2)
# print(ob1 * 9)

hs = {tuple(["12"]): "utsa"}
print(hs)
