'''
I have 213 bars of chocolate that I would like to share evenly among the students registered
for Computer Programming for CS in the second semester (see problem 1). How many bars
of chocolate will each student receive, and how many will be left over?
Store the number of bars each student will receive in a variable called
chocolate_per_student and the number of chocolates that will remain in a variable called
remaining_chocolates. Also display your answers
'''
total_bars = 213
num_of_students = 133
chocolate_per_student = total_bars // num_of_students
remaining_chocolates = total_bars % num_of_students
print(f'chocolate per student: {chocolate_per_student}')
print(f'Remaining chocolates: {remaining_chocolates}')