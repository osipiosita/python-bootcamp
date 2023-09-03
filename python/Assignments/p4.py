'''
Mr. Mensah has just moved to a new house. However, water does not flow in his area, so he
needs to buy water to fill the cylindrical polytank on the roof of his house. The water
company sells water by volume. Write a program to help Mr. Mensah determine the volume
of water to order, given the dimensions of his polytank. The program should prompt Mr.
Mensah to enter the height and radius of his polytank.
'''
import math
height = float(input('Enter the height of your polytank: '))
radius = float(input('Enter the radius of your polytank: '))
volume_of_tank = math.pi * radius * radius * height
print(f'Volume of water to order: {round(volume_of_tank,2)} cubic metres')