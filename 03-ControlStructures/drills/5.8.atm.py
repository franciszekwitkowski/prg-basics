###
# ATM (cash machine) simulator
#
balance = 1000  # Initial balance
pin = '1111' # initial 4-digit PIN code

while True:
    entered_pin = input("Enter your 4-digit PIN code: ")
    if entered_pin == pin:

        print()
        print("ATM Menu:")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")
        print()
        
        if choice == '1':
                print(f"Your current balance is: €{balance}")
        elif choice == '2':
                amount = float(input("Enter the amount to deposit: "))
                balance += amount
                print(f"€{amount} has been deposited. New balance: €{balance}")
        elif choice == '3':
                amount = float(input("Enter the amount to withdraw: "))
                if amount <= balance:
                    balance -= amount
                    print(f"€{amount} has been withdrawn. New balance: €{balance}")
                else:
                    print("Insufficient balance.")
        elif choice == '4':
              new_pin = input("Enter your new 4-digit PIN code: ")
              if len(new_pin) == 4 and new_pin.isdigit():
                pin = new_pin
                print("PIN code has been changed successfully.")
              else:
                print("Entered PIN code format is Invalid. Please try again.")
        elif choice == '5': 
                print("Exiting... Thank you for using the ATM!")
                break  # Exit the loop
        else:
                print("Invalid option. Please try again.")


    else:
        print("Incorrect PIN. Please try again.")

    
