#new # Function to print Tic Tac Toe
def draw_board_list(board):
    print("\n")
    print("\t       |       |")
    print("\t  {}    |  {}    |   {}".format(board[6], board[7],board[8]))
    print('\t_______|_______|______|')
    print("\t       |       |")
    print("\t  {}    |  {}    |   {}".format(board[3], board[4],board[5]))
    print('\t_______|_______|______|')
    print("\t       |       |")
    print("\t  {}    |  {}    |   {}".format(board[0], board[1],board[2]))
    print('\t_______|_______|______|')
    print("\n")
#End of function
# list_board = ['1','2','3','4','5','6','7','8','9']
# draw_board_list(list_board)

# The main game function
def game():
    cur_player = 'X'
    list_board = ['1','2','3','4','5','6','7','8','9']
    count = 1

    #repeat 11 - 1 = 10 times because that's the max number of moves a game can have (3x3=9)
    while count < 11:
        draw_board_list(list_board)

        # get current player's input
        print("Move ", count, "\n", "Player ", cur_player, " turn. Which square? : ", end="")
        move = input()

        if move.isnumeric():
            print("ok, a num")

            # Input validation: check if input is a digit between 1 and 9
            if not (1 <= int(move) <= 9):
                print("Invalid input! Please enter a number between 1 and 9.")
                continue  # ask for input again

        else:
            print("error...")
            continue

        #convert str to int
        move = int(move) - 1

        #check to make sure the cell is not already filled
        if list_board[move] != 'X' and list_board[move] != 'O':
            print() #update player's move on the list
        

        else:
            print("That cell is already filled.\nKey in another move?")
            continue


        #update player's move on the list
        list_board[move] = cur_player

        def win_check(board, mark):
            if board[0] == board[1] == board[2] == mark:
                return True
        # to be continued

        #switch the current player
        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'
        
        count = count + 1  



#main
game()

# # Function to print the score-board
# def print_scoreboard(score_board):
#     print("--------------------------------")
#     print('         SCOREBOARD         ')
#     print("--------------------------------")

#     players = list(score_board.keys())
#     print("  ", players[0], "  ",)
