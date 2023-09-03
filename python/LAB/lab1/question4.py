'''
Test Code
Enter the radius of cylinder: 4
Enter the height of the radius: 5
Volume of cylinder is 251.3 cubic units
'''
import math
radius = float(input('Enter the radius of cylinder: '))
height = float(input('Enter the height of the radius: '))
volume = math.pi * ((radius**2) * height)
print(f'Volume of cylinder is {round(volume,1)} cubic units') # Using formatted string