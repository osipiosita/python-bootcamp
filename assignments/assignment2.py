def compareStrings(garland,flower):
    count = 0
    for i in flower:
        if i in garland:
            count += 1
    return count
test = compareStrings('z','ZZ')
print(test)
print('\n')

# Question 2
def grade_gpa(score):
    if 85<=score<=100:
        return 4.00,'A+'
    elif 80<=score<=84:
        return 4.00, 'A'
    elif 75<=score<=79:
        return 3.50, 'B+'
    elif 70<=score<=74:
        return 3.00, 'B'
    elif 65<=score<=69:
        return 2.50, 'C+'
    elif 60<=score<=64:
        return 2.00, 'C'
    elif 55<=score<59:
        return 1.50, 'D+'
    elif 50<=score<=54:
        return 1.00, 'D'
    elif score<50:
        return 0.00, 'E'

def honours(gpa):
    if 3.85 <= gpa <= 4.00:
        honour = 'Summa Cum Laude'
    elif 3.70 <= gpa <= 3.84:
        honour = 'Magna Cum Laude'
    elif 3.50 <= gpa <= 3.69:
        honour = 'Cum Laude'
    else:
        honour='no honours'
    return honour

def overall():
    count_Aplus, countA, count_Bplus, countB, count_Cplus, countC, count_Dplus, countD, \
    countE = 0,0,0,0,0,0,0,0,0
    scores = []
    credits = []
    cgpas = []
    fcgpa = 0
    total = int(input('How many courses do you want to compute for? '))
    for _ in range(total):
        score = int(input('Enter score: '))
        credit = int(input('Enter credit weighting for the above course: '))
        scores.append(score)
        credits.append(credit)
    for i in range(len(scores)):
        var = grade_gpa(scores[i])
        gpa_credit = var[0] * credits[i]
        cgpas.append(gpa_credit)
        if var[1] == 'A+':
            count_Aplus += 1
        elif var[1] == 'A':
            countA += 1
        elif var[1] == 'B+':
            count_Bplus += 1
        elif var[1] == 'B':
            countB += 1
        elif var[1] == 'C+':
            count_Cplus += 1
        elif var[1] == 'C':
            countC += 1
        elif var[1] == 'D+':
            count_Dplus += 1
        elif var[1] == 'D':
            countD += 1
        elif var[1] == 'E':
            countE += 1
        print(var)
    if count_Aplus >= 1:
            print('You got '+ str(count_Aplus), 'A+')
    if countA >= 1:
        print('You got '+ str(countA), 'A')
    if count_Bplus >= 1:
        print('You got '+ str(count_Bplus), 'B+')   
    if countB >= 1:
        print('You got '+ str(countB), 'B')
    if count_Cplus >= 1:
        print('You got '+ str(count_Cplus), 'C+')
    if countC >= 1:
        print('You got '+ str(countC), 'C') 
    if count_Dplus >= 1:
        print('You got '+ str(count_Dplus), 'D+')
    if countD >= 1:
        print('You got '+ str(countD), 'D')
    if countE >= 1:
        print('You got '+ str(countE), 'E')
    for j in cgpas:
        fcgpa += j
    cgpa =  fcgpa/sum(credits)
    print('Your total gpa is: ',round(cgpa, 2))
    print(honours(round(cgpa,2)))
overall()
print('\n')

# Question 3
numb = int(input('Enter a number: '))
sum = (numb * (numb + 1))/2
print(f'The sum is {sum}')
print('\n')

# Question 4
def customLen(string):
    length = 0
    for _ in string:
        length += 1
    return length
print('\n')

# Question 5
mylist = [1,2,3,4,5,6,7,8,9,10,11,12]
n = int(input('Enter a number: '))
for i in mylist:
    product = n * i
    print(i, '*', n, '=', product)
print('\n')  
   
# Question 7
def is_vowel():
    string = input('enter a character: ')
    vowels = 'aeiou'
    if len(string) > 1:
        print('Enter only ONE character!')
        
    else:
        if string in vowels:
            return True
        return False
print(is_vowel())

print('\n')

# Question 6
magic_number = 27
while True:
    lucky_number = int(input('Guess the magic number(1-100): '))
    if lucky_number > magic_number:
        print('That number is too high!')
    elif lucky_number < magic_number:
        print('That number is too low!')
    else:
        print('Hooray, you guessed right!') 
        break