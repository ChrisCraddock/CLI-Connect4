import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT)) #Matrix of 6 rows by 7 columns
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT): #r counts from 0 to row_count - 1
        if board[r][col] == 0: #check board position
            return r

def print_board(board):
    print(np.flip(board,0))

def winning_move(board, piece):
    #Check Horizontal locations
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c +1] == piece and board[r][c +2] == piece and board[r][c +3]:
                return True
    #Check Vertical locations
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT -3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c]:
                return True
    #Check Pos Slope locations
    for c in range(COLUMN_COUNT -3):
        for r in range(ROW_COUNT -3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3]:
                return True
    #Check Neg Slope locations
    for c in range(COLUMN_COUNT -3):
        for r in range(3,ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3]:
                return True



board = create_board()
print_board(board)
game_over = False
turn = 0

while not game_over:
    #Ask P1 input6
    if turn == 0:
        col = int(input("Player 1 make selection (0-6): "))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board,row, col, 1)

            if winning_move(board, 1):
                print("Player 1 Wins")
                game_over == True
                break
    #Ask P2 input
    else:
        col = int(input("Player 2 make selection (0-6)"))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board,row, col, 2)

            if winning_move(board, 2):
                print("Player 2 Wins")
                game_over == True
                break
    
    print_board(board)

    turn += 1 #Increases the turn count
    turn = turn % 2  #Alternate between player turns
