import random

usr_wins = 0
my_wins = 0

choices = ["rock", "paper", "scissors"]

while True:
    usr_input = input('TYPE ROCK/PAPER/SCISSORS OR Q TO QUIT.').lower()
    if usr_input == 'q':
        break
    
    if usr_input not in choices:
        continue

    r_number = random.randint(0, 2)
    #rock:0 ; paper:1 ; scissors: 2
    my_pick = choices[r_number]
    print("I picked", my_pick + ".")

    if usr_input == "rock" and my_pick == "scissors":
        print('rOcK WHY ROCK, YOU BEAT ME BUT I BET I CAN WIN NEXT TIME!')
        usr_wins += 1

    elif usr_input == "paper" and my_pick == "rock":
        print('WHY WOULD YOU CHOOSE PAPER, ughh YOU BEAT ME I BET I CAN WIN NEXT TIME!')
        usr_wins += 1
    
    elif usr_input == "scissors" and my_pick == "paper":
        print('WHO CHOOSES SCISSORS, YOU BEAT ME BUT I KNOW I CAN WIN NEXT TIME!')
        usr_wins += 1
        
    else:
        print('YOU LOST HAHAHAHA YOU WONT BEAT ME AGAIN!')
        my_wins += 1


print("You won", usr_wins,"time(s)!")
print("I won", my_wins,"time(s)!" )
print('THANKS FOR PLAYING... DID YOU BEAT ME!?')