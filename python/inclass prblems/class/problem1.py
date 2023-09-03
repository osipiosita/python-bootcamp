'''
ACTION VERBS
1. Accepts <input>
2. Converts <input> into <seconds only>
'''
user_input_min =  int(input('Kindly input a number representing a number in minutes: '))
user_input_sec =  int(input('Kindly input a number representing a number in seconds: '))

#Multiply the number in minutes by 60 to get number in seconds
# 1 = 60 = 60 x 1
# 2 = 120 =  60 x 2
minutes_to_seconds = user_input_min * 60
result = minutes_to_seconds + user_input_sec
print(f'The answer is {result} in secomds')
