number = int(input("Enter number from 1 to 10: "))

for i in range(1, 11):
  answer = number * i
  print(f"{number} * {i} = {answer}")