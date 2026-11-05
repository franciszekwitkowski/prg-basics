time24 = input("Enter time in 24 hour format: ")
hours, minutes = time24.split(":")
hours = int(hours)

if hours == 0:
  hours = 12
  period = "am"
elif hours < 12:
  period = "am"
elif hours == 12:
  period = "pm"
else:
  hours -= 12
  period = "pm"

print(f"Time in 12-hour format: {hours}:{minutes}")