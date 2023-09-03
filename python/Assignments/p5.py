'''
The age of babies and young children are often given in months, rather than years. For
example, a mother might say that her toddler is 18 months old, or 24 months old. Write a
program that takes the age of a person in months, and reports the age in the corresponding
number of years and months. For example, a person who is 57 months old is actually 4 years
9 months old
'''
months = int(input('Enter the months: '))
age_in_years = months//12
months_remaining = months % 12
print(f'You are {age_in_years} years and {months_remaining} months old')