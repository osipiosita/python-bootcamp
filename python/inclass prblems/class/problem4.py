'''
#Problem 4
positive_integer = int(input('Kindly enter a positive integer: '))
sum = (positive_integer * (positive_integer+1))/2
print(f'The sum of the first {positive_integer} numbers is {sum}')
'''

a = int(input('Kindly enter the first number: '))
b = int(input('Kindly enter the second number: '))
the_sum = a + b
difference = a - b
product = a*b
quotient = round(a/b, 3)
remainder = a%b
exponent = a**b
print(f'The sum of {a} and {b} is {the_sum}\nThe difference between {a} and {b} is {difference}\n \
The product is {product}\nThe quotient is {quotient}\nThe remainder when {a} is divided ny {b} is {remainder}\n\
{a} raised to {b} is {exponent}')