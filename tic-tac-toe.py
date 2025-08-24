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
# Function to check win condition
def win_check(board, mark):
            if board[0] == board[1] == board[2] == mark:
                return True
        # to be continued
def win_check(board, mark):
    # Check rows
    if board[0] == board[1] == board[2] == mark:
        return True
    if board[3] == board[4] == board[5] == mark:
        return True
    if board[6] == board[7] == board[8] == mark:
        return True
    # Check columns
    if board[0] == board[3] == board[6] == mark:
        return True
    if board[1] == board[4] == board[7] == mark:
        return True
    if board[2] == board[5] == board[8] == mark:
        return True
    # Check diagonals
    if board[0] == board[4] == board[8] == mark:
        return True
    if board[2] == board[4] == board[6] == mark:
        return True
    return False
# The main game function
def game():
    cur_player = 'X'
    list_board = ['1','2','3','4','5','6','7','8','9']
    count = 1
    # repeat 9 times because that's the max number of moves a game can have (3x3=9)
    while count < 10:
        draw_board_list(list_board)
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
        # convert str to int
        move = int(move) - 1
        # check to make sure the cell is not already filled
        if list_board[move] != 'X' and list_board[move] != 'O':
            print() #update player's move on the list
        else:
            print("That cell is already filled.\nKey in another move?")
            continue
        # update player's move on the list
        list_board[move] = cur_player
        # Check for win after each move
        if win_check(list_board, cur_player):
            draw_board_list(list_board)
            print(f"Player {cur_player} wins!")
            return  # End the game
        # switch the current player
        cur_player = 'O' if cur_player == 'X' else 'X'
        count += 1
    # If no winner after 9 moves
    draw_board_list(list_board)
    print("It's a draw!")
#main
game()
# # Function to print the score-board
# def print_scoreboard(score_board):
#     print("--------------------------------")
#     print('         SCOREBOARD         ')
#     print("--------------------------------")2
#     players = list(score_board.keys())
#     print("  ", players[0], "  ",)
