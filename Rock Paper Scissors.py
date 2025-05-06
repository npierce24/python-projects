import random
import time
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Rock Paper Scissors")

usr_wins = 0
my_wins = 0

choices = ["rock", "paper", "scissors"]

while True:
    time.sleep(1)
    print( "Thanks for starting the program!")
    usr_input = input('\ntype rock/paper/scissors OR Q TO QUIT:  ').lower()
    if usr_input == 'q':
        break
    
    if usr_input not in choices:
        continue

    r_number = random.randint(0, 2)
    #rock:0 ; paper:1 ; scissors: 2
    my_pick = choices[r_number]
    print("\nRock")
    time.sleep(1)
    print("\npaper")
    time.sleep(1)
    print("\nscissors")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("\nSHOOT!")
    print("\nI picked", my_pick + ".")

    if usr_input == "rock" and my_pick == "scissors":
        time.sleep(3)
        print('\nrOcK WHY ROCK, YOU BEAT ME BUT I BET I CAN WIN NEXT TIME!')
        usr_wins += 1

    elif usr_input == "paper" and my_pick == "rock":
        time.sleep(3)
        print('\nWHY WOULD YOU CHOOSE PAPER, ughh YOU BEAT ME I BET I CAN WIN NEXT TIME!')
        usr_wins += 1
    
    elif usr_input == "scissors" and my_pick == "paper":
        time.sleep(3)
        print('\nWHO CHOOSES SCISSORS, YOU BEAT ME BUT I KNOW I CAN WIN NEXT TIME!')
        usr_wins += 1
        
    else:
        time.sleep(3)
        print('\nYOU LOST HAHAHAHA YOU WONT BEAT ME AGAIN!')
        my_wins += 1

time.sleep(2)
print("\nYou won", usr_wins,"time(s)!")
time.sleep(2)
print("\nI won", my_wins,"time(s)!" )
time.sleep(1)
print('\nTHANKS FOR PLAYING... DID YOU BEAT ME!?')