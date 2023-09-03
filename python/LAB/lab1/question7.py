'''
Test Code
Enter your height in feet: 6
Enter the inches: 4
Your height in centimetres is 193.04
'''
feet = float(input('Enter your height in feet: '))
feet_in_cm = (2.54 * 12) * feet
inches = float(input('Enter the inches: '))
inches_in_cm = inches * 2.54
print(f'Your height in centimetres is {feet_in_cm + inches_in_cm}') # using formatted strings