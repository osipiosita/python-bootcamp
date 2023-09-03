import time
'''
#Problem 2
user_name = input('Kindly enter your name: ')
print(f'Hello {user_name}')
'''
#Drawing a rectangle with symbols
column = 10
row = 5
for i in range(row):
    for j in range(column):
        print('$', end='')
        time.sleep(0.2)
    print()

