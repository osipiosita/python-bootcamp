import math
# Question 1
hw_Weight = 0.4
exam_Weight = 0.5
discussion_Weight = 0.1

hw_Grade = int(input('Enter your homework grade(%): '))
exam_Grade = int(input('Enter your exam grade(%): '))
discussion_Grade = int(input('Enter your discussion grade(%): '))

total_grade = (hw_Grade * hw_Weight) + (exam_Grade * exam_Weight) + (discussion_Grade * discussion_Weight)
print(f'Your overall grade is {total_grade}')
print('\n')

# Question 2
# A void function is a function that returns no value whilse a fruitful function has a return value.

# Question 3
print('Question 3')
principal = 10000
n = 12
rate = 8/100
years = int(input('How many years will the money be compounded for? '))
amount = principal * (1 + (rate/n)) ** (n*years)
result = round(amount, 3)
print('Amount after ' + str(years) + ' years is ' + str(result) )
print('\n')

# Question 4
def calculateGPA(score = int(input('Enter your score: '))):
    gpa = ''
    if 80 <= score <=100:
        gpa = 4.00
    elif 75 <= score <=79:
        gpa = 3.50
    elif 70 <= score <= 74:
        gpa = 3.00
    elif 65 <= score <= 69:
        gpa = 2.50
    elif 60 <= score <= 64:
        gpa = 2.00
    elif 55 <= score <= 59:
        gpa = 1.50
    elif 50 <= score <= 54:
        gpa = 1.00
    elif score < 50:
        gpa = 0.00
    print('Your gpa is', gpa)
    return gpa

def getHonours(gpa):
    honour = ''
    if 3.85 <= gpa <= 4.00:
        honour = 'Summa Cum Laude'
    elif 3.70 <= gpa <= 3.84:
        honour = 'Magna Cum Laude'
    elif 3.50 <= gpa <= 3.69:
        honour = 'Cum Laude'
    print('honour:', honour)
    return honour
gpa = calculateGPA()
getHonours(gpa)

# Question 5
radius = float(input('Enter the radius: '))
area = math.pi * ((radius)**2)
print('Area =', area)
print('\n')

# Question 6
def is_triangle(num1, num2, num3):
    if num1 > (num2 + num3) or num2 >(num1 + num3) or num3 > (num1 + num2):
        return False
    else:
        return True
def stick_length():
    stick1 = int(input('Enter length of stick 1: '))
    stick2 = int(input('Enter length of stick 2: '))
    stick3 = int(input('Enter length of stick 3: '))
    result = is_triangle(stick1,stick2,stick3)
    if result == False:
        print('These sticks CANNOT form a triangle!')
    else:
        print('These sticks CAN form a triangle!')
stick_length()