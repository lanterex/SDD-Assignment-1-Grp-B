import random # To be able to get a random number
import sys    # To close the game
from random import random, randint
import shelve

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

totalPoints = 0
residentialPoints = 0
industryPoints = 0
commPoints = 0
parkPoints = 0
roadPoints = 0
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
        return 2
    if sogchoice == 3:
        return 3
    if sogchoice ==4:
        return 4
    if sogchoice == 0:
        print('Thanks for playing!')
        return 0

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
    print('\n- When reading the grid, the x-coordinates is obtained from the top of the graph,\n  and the y-coordinates is obtained from the left of the graph.')
    print('\n- If you run out of coins, you lose the game.\n')


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
    print("\nCoin(s): " + str(coin) + "\n")

def check_input(choice):
    coords = choice.split(',')
    
    # Check that there are exactly two parts
    if len(coords) != 2:
        return False
    
    # Check that both parts are integers within the range 1-20 inclusive
    for i in coords:
        if not i.isdigit():
            return False
        if not 1 <= int(i) <= 20:
            return False
    
    # If we get here, the input is valid
    return True


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
    while True:
        try:
            choice = input("Your choice: ")
            choice = choice.upper()
            if choice == building1 or choice == building2:
                break
            print("\nPlease enter one of the buildings in the options given.\n")
        except ValueError:
            print("\nInvalid input! Please enter one of the buildings in the options given.\n")
            continue
    if choice in building_list:
        while True:
            try:
                location = input("Where? (Provide xy coordinates in x,y format) \n")
                inputBool = check_input(location)
                if inputBool == False:
                    print("Please enter a set of valid coordinates, (x,y) format.")
                else:
                    location = location.split(',')
                    break
            except ValueError:
                print("Invaild input! Please enter a set of valid coordinates, (x,y) format.")
                continue
        x_coord = int(location[0]) - 1
        y_coord = int(location[1]) - 1
        if turn == 1:
            allowplace = True
        else:
            checkup, checkleft, checkright, checkdown, checkcurrent = prox_check(x_coord,y_coord,board)
            allowplace = False
            if checkup == True and checkcurrent == False:
                if board[y_coord-1][x_coord] !=  '   ': #checks if there IS something on its direction. (Being UP)
                    allowplace = True
            if checkdown == True and checkcurrent == False:
                if board[y_coord+1][x_coord] !=  '   ': #checks the cell below!
                    allowplace = True
            if checkleft == True and checkcurrent == False:
                if board[y_coord][x_coord-1] != '   ': #check the cell on the left!
                    allowplace = True
            if checkright == True and checkcurrent == False:
                if board[y_coord][x_coord+1] != '   ': #checks the cell on the right!
                    allowplace = True
        if allowplace == True:
            board[y_coord][x_coord] = choice
            coin -= 1
            losscheck(coin,board)
            if choice in ['I', 'C']:
                coin_calc(choice,x_coord, y_coord)
        else:
            print('Invalid location, retype your location.')
            turn -= 1                         #Resets back to what it was before the illegal placement.
    else:
        print('Invalid building type, please retype your choice.')
        turn -=1

def prox_check(row,column,board):
        checkup = True
        checkleft = True
        checkright = True
        checkdown = True
        checkcurrent = True
        
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
        return checkup, checkleft, checkright, checkdown, checkcurrent       
def losscheck(coin,board):
    global gameoverflag
    global totalPoints
    global turn
    if coin == 0:
        gameoverflag = True
        display_board(board,turn,coin)
        print("You ran out of money to develop the city, and are ousted by your people.\nGame Over...\n")
    elif turn > 400:
        gameoverflag = True
        display_board(board,turn,coin)
        print("You ran out of space to develop the city, your services were no longer required...\nGame over...\n")
    if gameoverflag == True:
        totalPoints = score_calc()
        savehighscore(totalPoints)


def score_calc():
    global coin
    global board
    commercialList = []
    parkList = []
    roadList = []
    totalPoints = 0
    residentialPoints = 0
    industryPoints = 0
    commPoints = 0
    parkPoints = 0
    roadPoints = 0
    print("\n=== Points gathered for each building ===\n")

    # Residential
    for row in range (NUM_ROWS):
        for column in range (NUM_COLUMNS):
            if board[column][row] == 'R':
                residentialList = []
                resPointList = []
                checkup, checkleft, checkright, checkdown, checkcurrent = prox_check(row,column,board)
                if checkup == True:             
                    residentialList.append(board[column-1][row])
                if checkdown == True:              
                    residentialList.append(board[column+1][row])
                if checkleft == True:
                    residentialList.append(board[column][row-1])
                if checkright == True:             
                    residentialList.append(board[column][row+1])
                for building in residentialList:
                    indCount = residentialList.count('I')
                    if indCount > 0:
                        resPointList.append(1)
                        break 
                    elif building in ["R", "C"]:
                        resPointList.append(1)
                    elif building == 'O':
                        resPointList.append(2)
                residentialPoints = sum(resPointList)
    print(f"Residential Points: {residentialPoints}")


    # Industry
    for row in range (NUM_ROWS):
        for column in range (NUM_COLUMNS):
            if board[column][row] == 'I':
                industryPoints += 1
    print(f"Industry Points: {industryPoints}") #Test print to see if it adds.

    # Commercial
    for row in range (NUM_ROWS):
        for column in range (NUM_COLUMNS):
            if board[column][row] == 'C':
                checkup, checkleft, checkright, checkdown, checkcurrent = prox_check(row,column,board)
                if checkup == True:             
                    commercialList.append(board[column-1][row])
                if checkdown == True:              
                    commercialList.append(board[column+1][row])
                if checkleft == True:
                    commercialList.append(board[column][row-1])
                if checkright == True:             
                    commercialList.append(board[column][row+1])
    commPoints = commercialList.count("C")

    print(f"Commercial Points: {commPoints}")

    #Park
    for row in range(NUM_ROWS):
        for column in range(NUM_COLUMNS):
            if (board[column][row] == 'O'):
                checkup, checkleft, checkright, checkdown, checkcurrent = prox_check(row,column,board)
                if checkup == True:             
                    parkList.append(board[column-1][row])
                if checkdown == True:              
                    parkList.append(board[column+1][row])
                if checkleft == True:
                    parkList.append(board[column][row-1])
                if checkright == True:             
                    parkList.append(board[column][row+1])
    parkPoints = parkList.count("O")

    print(f"Park Points: {parkPoints}")

    #Road (not fully done yet)
    for row in range(NUM_ROWS):
        for column in range(NUM_COLUMNS):  
            if(board[column][row] == '*'):
                checkup, checkleft, checkright, checkdown, checkcurrent = prox_check(row,column,board)
                if checkup == True:             
                    continue
                if checkdown == True:              
                    continue
                if checkleft == True:
                    roadList.append(board[column][row-1])
                if checkright == True:             
                    roadList.append(board[column][row+1])
    roadPoints = roadList.count("*")
    print(f"Road Points: {roadPoints}")

    totalPoints = residentialPoints+ industryPoints + commPoints + parkPoints + roadPoints
    print(f"\nTotal points: {totalPoints}")
    return totalPoints


def coin_calc(choice,row,column):
    global coin
    global resiCount
    tempList = []
    if choice in ['I', 'C']:
        checkup, checkleft, checkright, checkdown, checkcurrent = prox_check(row,column,board)
        if checkup == True and checkcurrent == True:             
            tempList.append(board[column-1][row])
        if checkdown == True and checkcurrent == True:              
            tempList.append(board[column+1][row])
        if checkleft == True and checkcurrent == True:
            tempList.append(board[column][row-1])
        if checkright == True and checkcurrent == True:             
            tempList.append(board[column][row+1])
    for building in tempList:
        if building == "R":
            coin += 1
    resiCount = tempList.count("R")
    if resiCount > 0:
        print(f"\n'{choice}' placed next to {resiCount} 'R' building(s)! +{resiCount} coin(s)! ")

def ingameMenu():
    global gameoverflag
    global turn
    print('\n1. Place Buildings\n2. See Current Score\n3. Save Game\n\n0. Exit\n')
    while True:
        try:
            choice = input("Your choice: \n")
            if choice == '1':
                place_buildings(board)
                break
            elif choice =='2':
                #scorecheck
                score_calc()
                turn -=1
                break
            elif choice =='3':
                #savegame
                print("\nSaving...\n")
                save_game()
                print("\nSaved!\n")
                turn -=1
                break
            elif choice =='0':
                print('\nReturning...')
                gameoverflag = True
                break
            else:
                print("Please enter a valid choice.")
        except ValueError:
                    print('Please enter a valid choice.')

def save_game():
    mapFile = "board.txt"
    with open(mapFile, "w") as file:
        for row in board:
            line = "{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]) #formats it in rows
            file.write(line)

    turnFile = "savedata.txt"
    datafile = open(turnFile, 'w')
    datafile.write("{},{}".format(turn,coin)) #Writes the turnnumber into the file
    datafile.close()

def open_game():

    board_datafile = "board.txt"
    openmap_grid = open(board_datafile,'r')
    boardList = []
    for line in openmap_grid:
        boardList.append(line.split(','))
    for index in range (len(boardList)):
        boardList[index][-1] = boardList[index][-1].replace('\n','')
    board = boardList

    savedata_datafile = "savedata.txt"
    opensavedata = open(savedata_datafile,'r')
    for line in opensavedata:
        savedata = line
    savedata = savedata.split(',')
    savedata[-1] = savedata[-1].replace('\n','')
    turn = savedata[0]
    turn = int(turn)
    coin = savedata[1]
    coin = int(coin)
    return building_list, board, turn, coin

def takesecond(item):
    return item[1]

def leaderboard():
    leaderboard_file = 'leaderboard.txt'
    leaderboard = []
    entry = []
    openleaderboard = open(leaderboard_file,'r')
    for line in openleaderboard:
        line = line.replace('\n','')   #removes the \n from the retrieval
        entry = line.split(',')        #splits into the required playername field and score
        entry[-1] = int(entry[-1])
        leaderboard.append(entry)      #adds to leaderboard
    leaderboard = sorted(leaderboard,reverse=True,key=takesecond)  #executes a descending order sort with the score as the key
    print('=== Leaderboard ===')
    count = 1
    for entry in leaderboard:
        if count <= 10:
            print('{:<4}{:14}{}'.format(count,entry[0],entry[1]))
            count += 1

def savehighscore(totalPoints):
    print('\nNaming rules: Do not use "," in your given name, it will be removed.')
    player = input('Enter your name: ')
    player = player.replace(',','')
    totalscore = str(totalPoints)
    leaderboard_file = open('leaderboard.txt','a')
    leaderboard_file.write('{},{}\n'.format(player,totalscore))
    leaderboard_file.close()
    

# RUNTIME CODE BELOW

while True:
    option = first_screen()
    exit_main_screen = False
    gameoverflag = False
    if option == 1:
        start_game(buildings, building_count)
        while gameoverflag == False:
            display_board(board,turn,coin)
            ingameMenu()
            turn+=1
    elif option == 2:
        print('\nLoading...\n')
        open_game()
        saved_numbers = open_game()
        board = saved_numbers[1]
        turn = saved_numbers[2]
        coin = saved_numbers[3]
        while gameoverflag == False:
            display_board(board,turn,coin)
            ingameMenu()
            turn +=1
    elif option == 3:
        print('\nLoading...\n')
        leaderboard()
    elif option == 4:
        game_rule()
    elif option == 0:
        sys.exit()
    else:
        print('Invalid option.')
    
    print()


    

