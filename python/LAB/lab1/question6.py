'''
Test Code
The sum of 5 and 4 is 9
The difference between 5 and 4 is 1      
The product is 20
The quotient is 1.25
The remainder when 5 is divided ny 4 is 1
5 raised to 4 is 625
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
{a} raised to {b} is {exponent}') # using formatted strings