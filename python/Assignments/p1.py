'''
One semester, there were 62 students in the Computer Programming for CS class. The
following semester, there were 133 students registered for Computer Programming for CS.
What is the percentage increase in the number of students that took programming in the
second semester, compared to the first semester?
Store the result in a variable named percent_increase. Also display your answer
'''
sem1 = 62
sem2 = 133
percent_increase = ((sem2-sem1)/sem1) * 100
print(f'The percentage increase compared to the first semester is {percent_increase}')