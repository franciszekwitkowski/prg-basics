'''
A washing machine allows you to wash a jacket, which takes 40 minutes, wash underwear, which takes 70 minutes, and wash shoes, which takes 20 minutes. In addition, it is possible to program an additional rinse (15 minutes) and an additional spin (9 minutes). The washing machine settings are saved in variables. Write a program that calculates and prints the total washing time. Sample result:

    washing_product = \"shoes\"\
    rinse = True\
    spin = False\
    Total washing time: 35 minutes

'''

program = input('Select washing program: jacket, underwear, shoes: ')
extra_rinse = input('Extra rinse? (yes/no) ')
extra_spin = input('Extra spin? (yes/no) ')


washing_products = {
  "jacket" : 40,
  "underwear" : 70,
  "shoes" : 20
}

Total_Washing_Time = washing_products.get(program.lower().strip(), 0)

if extra_rinse.lower().strip() == "yes":
  Total_Washing_Time += 15
if extra_spin.lower().strip() == "yes":
  Total_Washing_Time += 9

print(f"washing_product:\"{program}\"")
print(f"rinse:{extra_rinse}")
print(f"spin:{extra_spin}")
print(f"Total washing time: {Total_Washing_Time} minutes")
