number = input("Enter a number: ")
binary = bin(int(number))[2:]
hexadecimal = hex(int(number))[2:]
print(f"Binary number: {binary}")
print(f"Hexadecimal number: {hexadecimal}")