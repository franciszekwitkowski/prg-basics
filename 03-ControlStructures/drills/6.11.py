dog_age = int(input("Enter the dog's age in human years: "))

if dog_age <= 2:
  dog_years = dog_age * 10.5
else:
  dog_years = 2 * 10.5 + (dog_age - 2) * 4

print("Your dog's age in dog years is {:g}".format(dog_years))