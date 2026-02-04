class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        fahrenheit = lambda c: (c * 1.8)+32
        kelvin = lambda c: c + 273.15
        return [kelvin(celsius), fahrenheit(celsius)]