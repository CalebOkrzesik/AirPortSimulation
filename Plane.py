# Plane class for airport simulator

import random

def generateFlightNumber():
    flight = f"{random.randint(65, 90):c}"
    for i in range(3):
        flight += str(random.randint(0,9))
    return flight

def generateAirline():
    airlines = ["American Airlines", "Southwest Airlines",
                "Spirit Airlines", "Jet Blue", "United Airlines",
                "Delta Airlines", "PanAm", "Joe's Discount Airline",
                "Airline of DuPage", "Crazy Steve's Plane-o-rama"]
    return airlines[random.randint(0, len(airlines)-1)]

class Plane:
    def __init__(self):
        self.__airline = generateAirline()
        self.__flightNumber = generateFlightNumber()

    @property
    def airline(self):
        return self.__airline

    @property
    def flightNo(self):
        return self.__flightNumber

    def __str__(self):
        return self.airline + " Flight " + self.flightNo




