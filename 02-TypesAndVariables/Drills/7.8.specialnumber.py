from random import randint
dice_roll = randint(1, 6)
print(f"Dice roll: {dice_roll}")
if dice_roll == 6 or dice_roll == 1:
    print("Special number: True")
else:
    print("Special number: False")