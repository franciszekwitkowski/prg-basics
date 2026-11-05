EAN13 = input("Enter EAN-13 article number: ").strip()


if EAN13.isdigit() and len(EAN13) == 13:
  print("Article number is correct")
  if EAN13[:3] == "590":
    print("The Article was manufactured in Poland")
  else:
    print("The Article was not manufactured in Poland")
else:
  print("Article number is incorrect")

  

