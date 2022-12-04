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

    
    
    
    
    
board = []
buildings = []
building_count = {}
building_list = ['R', 'I', 'C', 'O', '*']
MAX_COUNT = 20
NUM_ROWS = 20
NUM_COLUMNS = 20
turn = 1
option = -1



start_game(buildings, building_count, turn)  
display_board(board)

    
def start_game(buildings, building_count, turn):
    turn = 1
    global board
    board = [['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
             ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
             ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
             ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
             ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
             ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
             ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
             ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
             ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
             ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
             ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
             ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
             ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
             ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
             ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
             ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
             ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
             ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
             ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
             ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ']]
    buildings = building_list * MAX_COUNT
    #print(buildings)
    for building in building_list:
        building_count[building] = MAX_COUNT
    #print(building_count)
    return buildings, building_count, turn
    
def display_board(board):
    #TODO print header for columns
    print('+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+')
    for row in range(NUM_ROWS):  
        #TODO print row numbering
        for column in range(NUM_COLUMNS):
                print('| {:3s} '.format(board[row][column]), end = '')
        print('|')

        print('', end = '')
        for column in range(1, NUM_COLUMNS + 1):
            print('+-----', end = '')
        print('+')
