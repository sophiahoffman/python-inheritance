# Define 5 of your favorite vehicles
# Move all common properties in your vehicles to a new Vehicle class.
# Create an instance of each vehicle.
# Define a different value for each vehicle's properties.
# Create a drive() method in the Vehicle class.
# Override the drive() method in all the other vehicle classes. Include the vehicle's color in the message (i.e. "The blue Ram drives past. RRrrrrrummbbble!").
# Create a turn(self, direction) method, and a stop(self) method on Vehicle. Define a basic implementation of each.
# Override all three of those methods on some of the vehicles. For example, the stop() method for a plane would be to output the message "The white Cessna rolls to a stop after rolling a mile down the runway."
# Make your vehicle instances perform all three behaviors.

# Make, Model, Year, Color, Body_Type


class Vehicle:
    def __init__ (self, make, model, year, color, body_type):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.body_type = body_type

    def drive(self):
        print(f"The {self.color} {self.model} drives past. Rrrrrrrummbbble!")
        return None

    def stop(self):
        print(f"The {self.color} {self.model} comes to a screeching halt. SCCCCRREEECHHHH!")
        return None
    
    def turn(self, direction):
        print(f"The {self.color} {self.model} turns {direction}.")
        return None
