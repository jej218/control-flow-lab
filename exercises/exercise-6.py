# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month:
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season>

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

from datetime import datetime

month_input = input("Enter the month of the year (Jan - Dec): ")
day_input = input("Enter the day of the month: ")

x = datetime.strptime(month_input + " " + day_input +
                      " 2020", "%b %d %Y").timetuple()

print(month_input + " " + day_input + " is in ", end="")

if(x.tm_yday <= 79 or x.tm_yday >= 356):
    print("Winter")
elif(x.tm_yday <= 172):
    print("Spring")
elif(x.tm_yday <= 265):
    print("Summer")
else:
    print("Fall")
