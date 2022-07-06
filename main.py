# im going to create a simple Loto system that will generate 5 numbers and see if you got the same numbers as it .
# range(10,30) NB!! RANGE FUNCTION
import random

print("Welcome to Kea's legal loto game for teenagers\n\n\t Stand a chance to Win 5 Billion Rand in cash !!")

# player must enter all their information
name = str(input('Name: '))
surname = str(input('Surname: '))
age = int(input('Age: '))


# if player is younger than 12 it must not let him play
if age > 12:
    print(' May the loto game begin!')
else:
    print('You are to young to play,13 and above')

print('\tPick the wining number! ')

# make 3 rows of numbers a,b,c and must display the list to the user
loto_numbers = list(range(1, 31))
print(loto_numbers)
players_wining_number = int(input('Enter the wining number from the list above: '))

p = random.choice(loto_numbers)
print(p)

if players_wining_number == p:
    print(' CONGRATULATION,You have just won 5 BILLION RAND!!')
else:
    print('Better luck next time , Please try again !')

