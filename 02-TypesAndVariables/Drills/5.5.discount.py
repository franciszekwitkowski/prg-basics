Price = input("Enter price: ")
Discount = input("Enter discount %: ")
Discounted_Price = float(Price) / float(Discount)
Reduction = float(Price) - float(Discounted_Price)

print(f"Discounted price: {round(Discounted_Price, 2)}")
print(f"Reduction: {round(Reduction, 2)}")