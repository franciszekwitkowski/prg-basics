Amount = int(input("Enter the amount in PLN: "))
'''
PLN5 = 0
PLN2 = 0
PLN1 = 0

while Amount > 0:
  if Amount / 5 >= 1:
    PLN5 += 1
    Amount -= 5
  elif Amount / 2 >= 1:
    PLN2 += 1
    Amount -= 2
  elif Amount /1 == 1:
    PLN1 += 1
    Amount -= 1
'''
PLN5 = Amount // 5
Amount %= 5
PLN2 = Amount // 2
Amount %= 2
PLN1 = Amount // 1

print(f"The amount of PLN {Amount} in coins:")
print(f"5 PLN coins: {PLN5} ")
print(f"2 PLN coins: {PLN2} ")
print(f"1 PLN coins: {PLN1} ")