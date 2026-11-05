PIN = "0805"
tries = 3

while tries > 0:
  Entered_PIN = input("Enter the PIN code: ").strip()
  if Entered_PIN == PIN:
    print("Successful. Access granted")
  else:
    print("Incorrect")
    tries -= 1

if tries == 0:
  print("Sorry, your payment card has been blocked.")
  