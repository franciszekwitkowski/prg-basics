current_price = int(input("current_price: "))
previous_price = int(input("previous_price: "))
percentage = int(((previous_price - current_price)/previous_price)*100)


if current_price < previous_price:
  if percentage < 10:
    print(f"Price reduced by {percentage}%" )
  else:
    print("Buy this product!")
    print(f"Price reduced by {percentage}%")
else:
  print("Price is not reduced")