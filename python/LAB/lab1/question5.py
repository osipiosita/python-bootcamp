'''
Test Code
Enter the amount deposited into the account: 100
Year 1: 104.0 
Year 2: 108.16
Year 3: 112.49
'''
deposit = float(input('Enter the amount deposited into the account: '))
for i in range(1,4):
    balance = (4/100 * deposit) + deposit
    deposit = balance # updating value of deposit
    print(f'Year {i}: {round(balance,2)}') # using formatted strings