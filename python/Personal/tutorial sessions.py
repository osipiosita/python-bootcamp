import time
'''
secret_word = 'love'
guess = ''
guess_limit = 3
guess_count = 0
while guess != secret_word and guess_count != guess_limit:
    guess = input('Enter the secret word: ') 
    guess_count += 1
if guess_count == guess_limit:
    print('You ran out of chances, You lose!')
else:
    print('Hooray, You win!!')

row = 4
col = 5
for i in range(row):
    for j in range(col):
        print('@',end=' ')
    print()
    time.sleep(1)

def translate(phrase):
    vowels = 'aieou'
    translation = ''
    for i in phrase:
        if i.lower() in vowels:
            if i.isupper():
                 translation = translation + 'G'
            else:
                translation = translation + 'g'
        else:
            translation = translation + i
    return translation
print(translate('dOg'))
'''
try:
    number = int(input('Enter a number: '))
    print(number)
    result = 10/0
except ValueError:
    print('Invalid input')
except ZeroDivisionError as err:
    print(err)