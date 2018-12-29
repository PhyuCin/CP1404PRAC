from Prac_08.car_copy import Car
import random


class UnreliableCar(Car):
    """Specialised version of a Car"""

    def __init__(self, name, fuel, car_reliability=0):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.car_reliability = car_reliability

    def drive(self, distance):
        reliability = random.uniform(0, 100)
        if reliability < self.car_reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
