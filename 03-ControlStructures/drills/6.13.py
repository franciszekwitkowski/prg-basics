Amount_of_products = int(input("Amount of products: "))
Price_of_product = int(input("Price: "))
All_products_price = Amount_of_products * Price_of_product
Final_price = 0

if Amount_of_products > 2:
  Final_price = (Amount_of_products -2) * Price_of_product * 0.75 + 2 * Price_of_product
else:
  Final_price = All_products_price

print(f"Final price: {Final_price}")