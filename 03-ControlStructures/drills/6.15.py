true = ["true"]

facebook = input("fb: ") in true
twitter = input("tw: ") in true
instagram = input("ig: ") in true

if sum([facebook, twitter, instagram]) >= 2:
  print("You are a good influencer!")
else:
  print("You are a horrible infulencer!!!")