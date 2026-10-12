total = 8000000000
north = 7200000000
south = total - north

print("World population: ", total)

print("Northern Hemisphere: ", north)
print("Northern Hemisphere in %: ", int(north/total*100),"%")

print("Southern Hemisphere: ", south)
print("Southern Hemisphere in %: ", int(south/total*100), "%")