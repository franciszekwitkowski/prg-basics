import random
    # COMPUTER TURN
computer = random.randint(1, 6)
    # YOUR TURN
you = input("Enter your number (1-6): ")

result = computer == int(you)
    
  
print(f'You won: {result}')
print(f'Computer rolled: {computer}')