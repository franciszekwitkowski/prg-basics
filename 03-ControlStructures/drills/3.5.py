days31month = [1, 3, 5, 7, 8, 10, 12]
days30month = [4, 6, 9, 11]

month = int(input('Enter month number (1..12): '))

if month in days31month:
    days = 31 ## months with 31 days
elif month in days30month:
    days = 30 ## months with 30 days
else:
    days = 28 ## February 28 days

print('Month {} has {} days'.format(month, days))