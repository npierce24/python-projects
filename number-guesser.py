import random
import time

print('¿WELCOME TO THE GAME OF GUESS?')
top_range = input("Type a maximum 1number any number: ")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0: 
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()

r_num = random.randint(0, top_range)
guesses = 0
while True:
    guesses += 1
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == r_num:
        print('you got it!')
        break
    elif user_guess > r_num:
        print('You were above the number!')
    else:
        print('You were below the number!')

            
print('You got it in', guesses, "guesses")
time.sleep(5)
print("closing the program in...")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    quit()