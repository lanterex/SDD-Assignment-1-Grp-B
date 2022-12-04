import random # To be able to get a random number
import sys    # For me to be able to close the game   

print('Welcome, Mayor of Ngee Ann City!')
print('----------------------------')

def first_screen():
    global buildingList,turnnumber,map_grid
    print('1. Start new game')
    print('2. Load saved game')
    print('\n0. Exit')
    sogchoice = int(input('Your choice? '))
    if sogchoice == 1:                
        return 1
    if sogchoice == 2:
        print('\n Loading... \n')
        return 1
    if sogchoice == 0:
        print('Thanks for playing!')
        sys.exit()
        
while True:
    option = first_screen()
    exit_main_screen = False
