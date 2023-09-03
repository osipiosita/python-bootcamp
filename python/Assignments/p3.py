'''
What is the volume of a cone with radius r = 2.5 cm and height h = 4cm?
Store the answer in a variable called sphere_volume. Also display the answer.
'''
import math
radius = 2.5
height = 4
volume_of_cone = 1/3*(math.pi*radius*radius)*height
print(f'volume of cone is {round(volume_of_cone,2)} cubic metres')
