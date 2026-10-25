cm = input("Enter your height in centimeters: ")
feet = float(cm) / 30.48
inches = float(cm) / 2.54
print("Your height in centimeters: " + str(round(float(cm), 2)))
print("Your height in feet: " + str(round(feet, 2)))
print("Your height in inches: " + str(round(inches, 2)))
