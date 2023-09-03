'''
Test Code
Kindly enter the number of days: 5
Kindly enter the hours: 4
Kindly enter the minutes: 45
Enter the seconds: 23
The result in seconds is 449123
'''
days = int(input('Kindly enter the number of days: '))
day_in_seconds = (24*3600) * days
hours = int(input('Kindly enter the hours: '))
hours_in_seconds = hours * 3600
minutes = int(input('Kindly enter the minutes: '))
minutes_in_seconds = minutes * 60
seconds = int(input('Enter the seconds: '))
total_seconds = day_in_seconds + hours_in_seconds + minutes_in_seconds + seconds
print(f'The result in seconds is {total_seconds}') # using formatted strings