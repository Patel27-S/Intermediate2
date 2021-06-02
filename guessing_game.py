import random

try:  
    num = int(input('Please enter the upper bound you want to play the game until : '))
except:
    print('Error : Please print an integral value for the upper bound.')
    exit()

random_number = random.randint(1,num)

'''
Number of chances you want to give :- num-1 #Otherwise the game has no meaning

Means, num-1 times at maximum if (prompt != random_number), then the prompt should
prompt and the comparison should happen.


'''
flag = True

counter = 0

while flag:

    counter += 1  # This variable will count the number of loop iterations/chances/guesses used.

    try:  # Putting a try, except block to cover the wrong value input error.
        prompt = int(input('Please enter your guessed number : '))
    except:
        print('Please enter a numerical guess!')

    if prompt == random_number:  # Correct guess implies loop termination.
        print('Congratulations....Yayyyy!! You got that right!!')
        print('You took', counter, 'number of guess(es).')
        flag = False  # Loop gets terminated.
    else:
        print('Oh no! Please try again!')
        print(num-1-counter, 'guess(es) are left for you.')  # max_allowed_guess minus no-guesses-taken.
    
    if counter >= num-1 and num > 1:  # (num-1) guesses at max. are kept as otherwise can be plain boring.
        print('Please re-play the game for another round!')
        flag = False




