decimal_number = int(input("Enter a decimal number: "))
binary_number = bin(decimal_number)

print(f"{decimal_number}(10) = {binary_number[2:]}(2)")