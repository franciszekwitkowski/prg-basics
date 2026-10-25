Celcius = input("Enter temperature in Celsius: ")
Fahrenheit = (float(Celcius) * 9/5) + 32
Kelvin = float(Celcius) + 273.15
print("Temperature in Fahrenheit: " + str(round(Fahrenheit, 2)))
print("Temperature in Kelvin: " + str(round(Kelvin, 2)))