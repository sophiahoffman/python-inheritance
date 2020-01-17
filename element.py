from vehicle import Vehicle

class Element(Vehicle):
    def __init__ (self, make, model, year, color, body_type):
        super().__init__(make, model, year, color, body_type)

    def drive(self, speed):
        print(f"My {self.make} {self.model} can drive 0 - {speed} in a hearbeat")