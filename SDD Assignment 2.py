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
coin = 16
gameoverflag = False # SET TO TRUE TO INITIATE GAME OVER... ADD DIFFERENT MESSAGES FOR FAILURE AT THE RUNTIME.

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
    print('\n=====    Here are the rules to the game.    =====\n')
    print("{:17}{}\n".format("Residential (R):","""If it is next to an industry (I), then it scores 1 point only. Otherwise, it scores 1
                 point for each adjacent residential (R) or commercial (C), and 2 points for each adjacent park (O)."""))
    print("{:17}{}\n".format("Industry (I):","""Scores 1 point per industry in the city. Each industry generates 1 coin per residential
                 building adjacent to it."""))
    print("{:17}{}\n".format("Commercial (C): ","""Scores 1 point per commercial adjacent to it. Each commercial generates 1 coin
                 per residential adjacent to it."""))
    print("{:17}{}\n".format("Park (O): ","Scores 1 point per park adjacent to it."))
    print("{:17}{}\n".format("Road (*)","Scores 1 point per connected road (*) in the same row."))
    return first_screen()

def start_game(buildings, building_count):
    global coin
    coin = 16
    global gameoverflag
    gameoverflag = False
    global turn
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
    
def display_board(board,turn,coin):
    #TODO print header for columns
    print('\n' + 'Turn ' + str(turn) + '\n')
    print("Coin(s): " + str(coin) + "\n")
    print('    01    02    03    04    05    06    07    08    09    10    11    12    13    14    15    16    17    18    19    20   ')
    print('  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+')
    
    for row in range(NUM_ROWS):  
        print('{}'.format(str(row+1).zfill(2)),end='')#TODO print row numbering
        for column in range(NUM_COLUMNS):
            
            print('| {:3s} '.format(board[row][column]), end = '')
        print('|')
        
        print('', end = '')
        for column in range(1, NUM_COLUMNS + 1):
            if column == 1:
                print('  +-----', end = '')
            else:
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

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def place_buildings(board):
    #get building list
    global building_list
    global turn
    global coin

    selected_buildings = []
    #obtaining building queue for the turn

    building1 = building_list[randint(0,4)]
    building2 = building_list[randint(0,4)]
    selected_buildings.append(building1)
    selected_buildings.append(building2)
    print("Building Selection: ",selected_buildings[0] , " , " , selected_buildings[1])
    choice = input("Your choice: ")
    choice = choice.upper()
    if choice in selected_buildings:
        location = input("Where? (Provide xy coordinates in x,y format) \n")
        location = location.split(",")
        x_coord = location[0]
        y_coord = location[1]
        if is_integer(x_coord) == True and is_integer(y_coord) == True:
            x_coord = int(x_coord) - 1
            y_coord = int(y_coord) - 1
            if x_coord <= 19 and x_coord >= 0 and y_coord <=19 and y_coord >=0:
                print(x_coord,y_coord)
                if turn == 1:
                    allowplace = True
                else:
                    checkup, checkleft, checkright, checkdown, checkcurrent = prox_check(x_coord,y_coord,turn,board)
                    allowplace = False
                    if checkup == True and checkcurrent == False:
                        if board[y_coord-1][x_coord] !=  '   ': #checks if there IS something on its direction. (Being UP)
                            allowplace = True
                    if checkleft == True and checkcurrent == False:
                        if board[y_coord][x_coord-1] != '   ': #check the cell on the left!
                            allowplace = True
                    if checkright == True and checkcurrent == False:
                        if board[y_coord][x_coord+1] != '   ': #checks the cell on the right!
                            allowplace = True
                    if checkdown == True and checkcurrent == False:
                        if board[y_coord+1][x_coord] !=  '   ': #checks the cell below!
                            allowplace = True
                if allowplace == True:
                   board[y_coord][x_coord] = choice
                   coin -= 1
                   losscheck(coin,board)
                else:
                     print('Invalid location, choose a different quadrant.')
                     turn -= 1                         #Resets back to what it was before the illegal placement.
            else:
                print('Invalid location, choose a different quadrant.')
                turn -= 1                         #Resets back to what it was before the illegal placement.
        else:
             print('Invalid location, retype your location.')
             turn -= 1                         #Resets back to what it was before the illegal placement.
    else:
         print('Invalid building type, please retype your choice.')
         turn -=1


def prox_check(row,column,turn,board):
    if turn != 1:
#        checkup = True
#        checkleft = True
#        checkright = True
#        checkdown = True
#        checkcurrent = True
        
        if column == 0:
            checkup = False
        else:
            checkup = True
        if column == 19:
            checkdown = False
        else:
            checkdown = True
        if row == 0:
            checkleft = False
        else:
            checkleft = True
        if row == 19:
            checkright= False 
        else:
            checkright = True
        if board[column][row] == '   ':
            checkcurrent = False
        else:
            checkcurrent = True

        print(checkup,checkleft,checkright,checkdown,checkcurrent)
        return checkup, checkleft, checkright, checkdown, checkcurrent
    else:
        pass
            
def losscheck(coin,board):
    global gameoverflag
    if coin == 0:
        gameoverflag = True
        display_board(board,turn,coin)
        print("You ran out of money to develop the city, and are ousted by your people.\nGame Over...")

def score_calc():
    global coin
    residentialList = []
    industryPoints = 0
    commercialList = []
    parkList = []
    roadList = []

    # Industry
    for row in range (NUM_ROWS):
        for column in range (NUM_COLUMNS):
            if board[row][column] == 'I':
                industryPoints += 1
    print(f"Industry Points: {industryPoints}") #Test print to see if it adds.
    
    #Road (not fully done yet)
    for row in range (NUM_NUM_ROWS):  
        for column in range (num_columns):
            if map_grid[row][column] == '*':
                numberofRoad += 1
            else:   
                continue

# RUNTIME CODE BELOW

while True:
    option = first_screen()
    exit_main_screen = False        
    start_game(buildings, building_count)  
    while gameoverflag == False:
        display_board(board,turn,coin)
        place_buildings(board)
        turn+=1
    print()


    

