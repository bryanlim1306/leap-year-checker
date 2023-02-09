# Input which year to check
year = int(input("Which year do you want to check? "))

# Check for leap year
# Divisible by 4
# If divisible by 100, must also be divisible by 400
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else: 
        print("Leap year.")
else:
    print("Not leap year.")