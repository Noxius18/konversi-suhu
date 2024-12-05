class Celcius():
    def __init__(self, celcius: float):
        self.celcius = celcius

    def fahrenheit(self):
        konversi = (self.celcius * (9 / 5)) + 32
        return konversi
    
    def reamur(self):
        konversi = (4 / 5) * self.celcius
        return konversi
    
    def kelvin(self):
        konversi = self.celcius + 273.15
        return konversi

class Fahrenheit():
    def __init__(self, fahrenheit: float):
        self.fahrenheit = fahrenheit
    
    def celcius(self):
        konversi = (self.fahrenheit - 32) / 1.8
        return konversi
    
    def reamur(self):
        konversi = (self.fahrenheit - 32) * 4/9
        return konversi
    
    def kelvin(self):
        konversi = (self.fahrenheit - 32) * (5 / 9) + 273.15
        return konversi
    
class Reamur():
    def __init__(self, reamur: float):
        self.reamur = reamur
    
    def celcius(self):
        konversi = (5 / 4) * self.reamur
        return konversi
    
    def fahrenheit(self):
        konversi = (self.reamur * 9 / 4) + 32
        return konversi
    
    def kelvin(self):
        konversi = (5 / 4) * self.reamur + 273.
        return konversi

class Kelvin():
    def __init__(self, kelvin: float):
        self.kelvin = kelvin

    def celcius(self):
        konversi = self.kelvin - 273.15
        return konversi
    
    def fahrenheit(self):
        konversi = (self.kelvin - (9 * 5)) - 459.67
        return konversi
    
    def reamur(self):
        konversi = (self.kelvin - 273.15) * 4 / 5
        return konversi