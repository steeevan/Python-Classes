#-------------------------------------------------------------------------------------------------------------------------------
# Class implementation
# # vehicle.py
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self,make,model):
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):

    def start_engine(self):
        print(f"Starting the engine of {self.make} {self.model}")

    def stop_engine(self):
        print(f"Stopping the engine of {self.make} {self.model}")

    def drive(self):
        print(f"Driving the {self.make} {self.model} Car.")

class Truck(Vehicle):

    def start_engine(self):
        print(f"Starting the engine of {self.make} {self.model}")

    def stop_engine(self):
        print(f"Stopping the engine of {self.make} {self.model}")

    def drive(self):
        print(f"Driving the {self.make} {self.model} Truck")

if __name__ == "__main__":
    buggy = Car("Volkswagon", "BuG")
    buggy.start_engine()
    buggy.drive()
#-----------------------------------------------------------------------------------------------------------
# Second file
# main.py
#---------
from vehicle import Car, Truck

def main():
    # Create instances of Car and Truck
    car = Car("Toyota", "Corolla")
    truck = Truck("Ford","F-150")

    #Demonstrate Polymorphism
    dealership = [car,truck]        # dealership.append(car)

    for vehicle in dealership:
        vehicle.start_engine()
        vehicle.drive()
        vehicle.stop_engine()
        print()


if __name__ == "__main__":
    main()
