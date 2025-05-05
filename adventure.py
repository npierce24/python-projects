import time

name = input("Hello Traveler, what is your name: ")
while len(name) <= 2:
    print('Please Enter Something\n')
    name = input("Hello Traveler, what is your name: ")
    

print("\nWelcome", name,"to this beautiful place!")

drink = input('Wow you are dirty, you must be tired from your travels would you like a drink?').lower()

if drink == "yes":
    print('\nHere, I was given this water by Roy He is a nice guy, he is always traveling these lands, Golly you drank that water down, you poor thing!')
    print("I will be your tour guide", name, "let me know where you want to go and I will take you! Next stop, THE CITY, first I am going to take you to my place you need a change of clothes before you go into the city!\n")
elif drink == 'no':
    tour = input("Would you like me to be your tour guide?" ).lower()
    if tour == "yes":
        print("Well first I want to take you to my place because you need a change of clothes I cant stand to see you all dirty like that!")
    elif tour == "no":
        print("Okay safe travels", name,",goodbye!")
        quit()
else: 
    print('Not a valid option, try yes or no.')
    quit()

print("There thats better now you look good! I hope you dont mind wearing my clothes")

tavern = input('Would you like to go to the tavern now?').lower()

if tavern == "yes":
    print("ALRIGHT! you are awesome", name, "cant wait to learn more about your travels!\n")
    print('You arrive at the tavern together..')
    print('')
    time.sleep(1)
    print('')
    time.sleep(1)
    print('')
    time.sleep(1)
    print('')
    print('')
    print('you eventually decide to leave and travel solo again...')
elif tavern == "no":
    print('Alright, Im going to go to the tavern if you need me thats where I will be, good luck out there!')
else: 
    print('Not a valid option, you lose.')
    quit()

direction = input('You have two different directions you could go North or South which do you choose?').lower()

if direction == "north":
    light = input('It is very dark and you think you see lights do you want to walk towards them?(yes/no)').lower()
elif direction == "south":
    print('You find a steep hill with rocks and try to climb!...\n\n')
    print("You Found Hidden Treasure, Congrats you win!")
    print('\n\n THANKS FOR PLAYING', name)
    quit()
else:
    print('Not a valid option, you lose.')
    quit()

if light == "yes":
    print('\n \n \n')
    print("You hear faint talking...!")
    print('\n You got kidnapped, you lose!')
    print('\n\n THANKS FOR PLAYING', name)
elif light == "no":
    river = input("You chose a safe way out, do you want to go across the river?(yes/no)").lower()
else: 
    print('Not a valid option, you lose.')
    quit()

if river == "yes":
    print('You have mistaken the river for a big waterfall, you end up being stuck in deep waters, you lose')
    print('\n\n THANKS FOR PLAYING', name)
elif river == "no":
    back = input('\nYou have made the right decision, Do you want to go back to the tavern?(yes/no)').lower()
else: 
    print('Not a valid option, you lose.')
    quit()

if back == "yes":
    print("You make it back to the tavern and find your friend, you go back to his place for shelter and a place to sleep for the night\n")
    print('Congratulations you survived safely, you win!')
    print('\n\n THANKS FOR PLAYING', name)

elif back == "no":
    print("You decided to stay, very brave choice!...\n")
    print("You find a place for shelter on your own so you dont have to stay with that cook from the city")
    land = input('Would you like to discover more of the surrounding land?').lower()
else: 
    print('Not a valid option, you lose.')
    quit()
if land == "yes":
    print('You go searching around the land in the dark...\n')
    print('something is shining..')
    print('\n\n\n\n\n')
    print('You found gold and viking jewelry! You decide to take it to your shelter and get some sleep, congrats you won!')
    print('\n\n THANKS FOR PLAYING', name)

elif land == "no":
    print('You decide to get some sleep in your newly found shelter!\n')
    print('You wake up laying next to a bear and he isnt happy, you lose') 
    print('better luck next time')
    print('\n\n THANKS FOR PLAYING', name)
else: 
    print('Not a valid option, you lose.')
    quit()