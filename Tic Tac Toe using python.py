
# this is a first porject 

# requierment :
'''
Board
display board
play game 
handle turn 
check win:
    check rows
    check coloumns
    check diagonals 
check tie
flip player     

'''
############################### main code #############################


# --------------------- global variable ---------------------

# if game is still playing

game_still_playing = True

# who win ?
winner = None

# whos turn it is ?

current_player = "X" 

# play game tic tac toe
def play_games():
    display_board()
    
     # while the game is still going
    while game_still_playing:

        # handle the turn 
        handle_turn(current_player)

        # check if the game has ended
        check_if_game_over()

        # check winner

        check_if_win()
        
        # flip to the other player 
        flip_player()

    # the game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")        


def display_board():
    print()
    print( board[0] + " | " + board[1] + " | " + board[2] )
    print( board[3] + " | " + board[4] + " | " + board[5] )
    print( board[6] + " | " + board[7] + " | " + board[8] )

# handle the turn
def handle_turn(current_player):
    print()
    print(current_player + "'s turn :")
    position = input("Choose a position from 1-9 : ")
    
    # position condition
    
    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9",]:
            position = input("\nInvalid input :\nChoose a position from 1-9 : ")

            position = int(position) -  1

            if board[position] != "-":
                print("You can not go there , Go there.")


    board[position] = current_player
    display_board()


# check if the game has ended
def check_if_game_over():
    check_if_win()
    check_if_tie()


# check the game winner
def check_if_win():

    global winner

    # check rows
    row_winner = check_rows()

    # check columns
    column_winner = check_columns()

    # check diagonals
    diagonals_winner = check_diagonals()

    # condition

    if row_winner:
        winner = row_winner

    elif column_winner:
        winner = column_winner

    elif diagonals_winner:
        winner = diagonals_winner        
    # return



# check row
def check_rows():
    global game_still_playing 
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'

    if row_1 or row_2 or row_3:
        game_still_playing = False

    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

    return    




# check columns
def  check_columns():
    global game_still_playing

    col_1 = board[0] == board[3] == board[6] != '-'
    col_2 = board[1] == board[4] == board[7] != '-'
    col_3 = board[2] == board[5] == board[8 ] != '-'

    if col_1 or col_2 or col_3:
        game_still_playing = False

    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return

# check diagonals
def check_diagonals():
    global game_still_playing

    dia_1 = board[0] == board[4] == board[8] != '-'
    dia_2 = board[6] == board[4] == board[2] != '-'

    if dia_1 or dia_2:
        game_still_playing = False

    if dia_1:
        return board[0]
    elif dia_2:
        return board[6]

    return
    


# check the game is tie
def check_if_tie():
    global game_still_playing

    if "-" not in board:
        game_still_playing = False
    return        

# to flip the player
def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"

    elif current_player == "O":
        current_player = "X"    
    return

# board
board = ["-","-","-",
         "-","-","-",
         "-","-","-",] 

play_games()       


