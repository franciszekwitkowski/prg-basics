

def sum_digits(number):
    sum = 0
    for i in number:
        i = int(i)
        sum += i
    return sum


number = str(abs(int(input("Enter an integer: "))))
result = sum_digits(number)
print("the sum of digits in the number {} is {}".format(number, result))