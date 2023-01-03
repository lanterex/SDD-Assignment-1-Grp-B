import random # To be able to get a random number
import sys    # To close the game
from random import random, randint

board = []
buildings = []
building_count = {}
building_list = ['R', 'I', 'C', 'O', '*']
building_names = ['Residential','Industry','Commercial','Park(O)','Road(*)']
MAX_COUNT = 20
NUM_ROWS = 20
NUM_COLUMNS = 20
turn = 1
option = -1
coins = 16

print('Welcome, Mayor of Ngee Ann City!')
print('----------------------------')

def first_screen():
    global buildingList,turnnumber,map_grid
    print('1. Start new game')
    print('2. Load saved game')
    print('3. See High Scores')
    print('4. Rules on how scoring works')
    print('\n0. Exit')
    sogchoice = int(input('Your choice? '))
    if sogchoice == 1:                
        return 1
    if sogchoice == 2:
        print('\n Loading... \n')
        return 1
    if sogchoice == 3:
        print('haha u bad we make later')
    if sogchoice ==4:
        game_rule()
    if sogchoice == 0:
        print('Thanks for playing!')
        sys.exit()

def game_rule():
    print("{:17}{}".format("Residential (R):","""If it is next to an industry (I), then it scores 1 point only. Otherwise, it scores 1
                 point for each adjacent residential (R) or commercial (C), and 2 points for each adjacent park (O)."""))
    print("{:17}{}".format("Industry (I):","""Scores 1 point per industry in the city. Each industry generates 1 coin per residential
                 building adjacent to it."""))
    print("{:17}{}".format("Commercial (C): ","""Scores 1 point per commercial adjacent to it. Each commercial generates 1 coin
                 per residential adjacent to it."""))
    print("{:17}{}".format("Park (O): ","Scores 1 point per park adjacent to it."))
    print("{:17}{}".format("Road (*)","Scores 1 point per connected road (*) in the same row."))

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
    
def display_board(board,turn):
    #TODO print header for columns
    print('\n' + 'Turn ' + str(turn) + '\n')
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

def verify(piece,location):                             #checks which type of piece it is, and parses through the verification using the required verification function
    global board
    if piece == "R":
        residentialPiece(location,board)
    elif piece == "I":
        industrialPiece(location,board)
    elif piece == "C":
        commercialPiece(location,board)
    elif piece == "O":
        parkPiece(location,board)
    elif piece == "*":
        roadPiece(location,board)

def residentialPiece(location,board):
    localscore = 0

    return localscore

def industrialPiece(location,board):
    localscore = 0

    return localscore

def commercialPiece(location,board):
    localscore = 0

    return localscore

def roadPiece(location,board):
    localscore = 0

    return localscore

def parkPiece(location,board):
    localscore = 0

    return localscore

    

def place_buildings(board):
    #get building list
    global building_list
    global turn


    selected_buildings = []
    #obtaining building queue for the turn

    building1 = building_list[randint(0,4)]
    building2 = building_list[randint(0,4)]
    selected_buildings.append(building1)
    selected_buildings.append(building2)
    print("Building Selection: ",selected_buildings[0] , " , " , selected_buildings[1])
    choice = input("Your choice: ")
    choice = choice.upper()
    if choice in building_list:
        location = input("Where? (Provide xy coordinates in x,y format) \n")
        location = location.split(",")
        x_coord = int(location[0]) - 1
        y_coord = int(location[1]) - 1
        if turn == 1:
            allowplace = True
        else:
            allowplace = prox_check(x_coord,y_coord,turn,board,choice)
        if allowplace == True:
            board[y_coord][x_coord] = choice
        else:
            print('You must build next to an existing building')
            board[y_coord][x_coord] = '   '
            turn -= 1                         #Resets back to what it was before the illegal placement.
        


def prox_check(row,column,turn,board,choice):
    if turn != 1:
        checkup = True
        checkleft = True
        checkright = True
        checkdown = True
        allowplace = False
        if row==0:
            checkup = False
        if row==19:
            checkdown = False
        if column ==0:
            checkleft = False
        if column ==19:
            checkright= False        
        if checkup == True:
            if board[column-1][row] !=  '   ': #checks if there IS something on its direction. (Being UP)
                allowplace = True
        if checkleft == True:
            if board[column][row-1] != '   ': #check the cell on the left!
                allowplace = True
        if checkright == True:
            if board[column][row+1] != '   ': #checks the cell on the right!
                allowplace = True
        if checkdown == True:
            if board[column+1][row] !=  '   ': #checks the cell below!
                allowplace = True
        return allowplace
    else:
        pass
            



while True:
    option = first_screen()
    exit_main_screen = False        
    start_game(buildings, building_count, turn)  
    while turn < 401:
        display_board(board,turn)
        place_buildings(board)
        turn+=1
    print()


    

