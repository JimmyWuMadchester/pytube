import numpy as np
import pygame

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

ROW_COUNT = 6
COL_COUNT = 7
WINNING_PIECE_COUNT = 4


def create_board():
    board = np.zeros((6, 7))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def print_board(board):
    print(np.flip(board, 0))


def is_winning_move(board, move):
    (row, col) = move
    piece = board[row][col]

    # Check horizontal locations for win
    horizontal_pieces = board[row, :] == piece
    horizontal_rolling_sums = np.convolve(horizontal_pieces, np.ones(WINNING_PIECE_COUNT, dtype=int), 'valid')
    win_by_horizontal = np.any(horizontal_rolling_sums == WINNING_PIECE_COUNT)
    if win_by_horizontal:
        print("win by horizontal")
        return True

    # Check vertical locations for win
    vertical_pieces = board[:row+1, col] == piece
    vertical_rolling_sums = np.convolve(vertical_pieces, np.ones(WINNING_PIECE_COUNT, dtype=int), 'valid')
    win_by_vertical = np.any(vertical_rolling_sums == WINNING_PIECE_COUNT)
    if win_by_vertical:
        print("win by vertical")
        return True

    # Check positively sloped diagonals
    pos_diag = np.diag(board, col-row) == piece
    pos_diag_rolling_sums = np.convolve(pos_diag, np.ones(WINNING_PIECE_COUNT, dtype=int), 'valid')
    win_by_pos_diag = np.any(pos_diag_rolling_sums == WINNING_PIECE_COUNT)
    if win_by_pos_diag:
        print("win by pos diag")
        return True

    # Check negatively sloped diagonals
    neg_diag = np.diag(np.flipud(board), col-row) == piece
    neg_diag_rolling_sums = np.convolve(neg_diag, np.ones(WINNING_PIECE_COUNT, dtype=int), 'valid')
    win_by_neg_diag = np.any(neg_diag_rolling_sums == WINNING_PIECE_COUNT)
    if win_by_neg_diag:
        print("win by pos diag")
        return True

    return False


board = create_board()
print_board(board)
game_over = False
turn = 0

pygame.init()

SQUARE_SIZE = 100
window_width = SQUARE_SIZE * COL_COUNT
window_height = SQUARE_SIZE * (ROW_COUNT+1)
window_size = (window_width, window_height)
screen = pygame.display.set_mode(window_size)

while not game_over:
    
    if turn == 0:
        col = int(input("Player one to move (0 .. 6):"))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)
            if is_winning_move(board, (row, col)):
                print("Player One Wins")
                game_over = True

    else:
        col = int(input("Player two to move (0 .. 6):"))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)
            if is_winning_move(board, (row, col)):
                print("Player Two Wins")
                game_over = True

    turn += 1
    turn %= 2
    print_board(board)





# board = np.random.randint(1, 3,