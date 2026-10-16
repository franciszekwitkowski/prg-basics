first = ord(input('Enter first letter: '))
last = ord(input("Enter last letter: "))
distance = last - first - 1
print(f'Between {chr(first)} and {chr(last)} is {distance} letters')
