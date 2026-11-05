N = int(input("Enter N: "))

number = 2
count = 0

print("Prime numbers: ", end=" ")

while count < N:

  is_prime = True
  divisor = 2

  while divisor * divisor <= number:
    if number % divisor == 0:
      is_prime = False
      break
    divisor += 1

  if is_prime:
    print(number, end=" ")
    count += 1

  number += 1
    
