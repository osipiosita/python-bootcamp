import math
def calc_hypotenuse(side1,side2):
    hypotenuse = math.sqrt(side1**2 + side2**2)
    print(f'The length of the hypotenuse is {round(hypotenuse, 3)}')

opp = int(input('Enter side 1 of triangle: '))
adj = int(input('Enter side 2 of triangle: '))
calc_hypotenuse(opp, adj)