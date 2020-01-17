from vehicle import Vehicle
from element import Element

# class Vehicle:
#     def __init__ (self, make, model, year, color, body_type):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.color = color
#         self.body_type = body_type

element = Element("Honda", "Element", 2011, "Gray", "SUV")

# metris = Vehicle("Mercedes", "Metris", 2017, "Black", "Minivan")
# taco = Vehicle("Toyota", "Tacoma", 2003, "Green", "Truck")
# x1 = Vehicle("BMW", "X1", 2017, "Silver", "Hatchback")
# crossfire = Vehicle("Chrysler", "Crossfire", 1994, "Red", "Sports")

# element.Vehicle.drive = print("Now I can control the element")

element.drive(60)
element.stop()
element.turn("right")

