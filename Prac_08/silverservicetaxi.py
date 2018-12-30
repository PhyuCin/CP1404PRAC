
from Prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):

    def __init__(self, name, fuel, fanciness=1):
        super().__init__(name, fuel)
        self.current_fare_distance = 0
        self.fanciness = fanciness
        self.price_per_km = self.price_per_km * self.fanciness
        self.flagfall = 4.50

    def __str__(self):
        return "{} plus flagfall of $4.50".format(super().__str__())

    def get_fare(self):
        return super().get_fare() + 4.50
