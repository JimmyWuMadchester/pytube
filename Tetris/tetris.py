import pygame
import random

# creating the data structure for pieces
# setting up global vars
# functions
# - create_grid
# - draw_grid
# - draw_window
# - rotating shape in main
# - setting up the main

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

pygame.font.init()

# GLOBALS VARS
s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

# SHAPE FORMATS

S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      0000.,
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]


# index 0 - 6 represent shape


class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_down(self):
        self.y += 1

    def move_up(self):
        self.y -= 1

    def rotate(self):
        self.rotation += 1


def create_grid(locked_positions={}):
    grid = [[(0, 0, 0) for _ in range(10)] for _ in range(20)]

    # j -> x // i -> y
    # i represents rows in the grid i_max = 20
    for i in range(len(grid)):
        # j represents columns in the grid j_max = 10
        for j in range(len(grid[i])):
            if (j, i) in locked_positions:
                color = locked_positions[(j, i)]
                grid[i][j] = color
    return grid


def convert_shape_format(shape):
    pass


def valid_space(shape, grid):
    pass


def check_lost(positions):
    pass


def get_shape():
    """
    
    :return: a new Piece object
    """
    return Piece(x=5, y=0, shape=random.choice(shapes))


def draw_text_middle(text, size, color, surface):
    pass


def draw_grid(surface, grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j],
                             (top_left_x + j * block_size, top_left_y + i * block_size, block_size, block_size), 0)

    pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 4)


def clear_rows(grid, locked):
    pass


def draw_next_shape(shape, surface):
    pass


def draw_window(surface, grid):
    surface.fill((0, 0, 0))

    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('Tetris', 1, (255, 255, 255))

    surface.blit(label, (s_width // 2 - label.get_width() // 2, 30))

    draw_grid(surface, grid)
    pygame.display.update()


def main(win):
    locked_positions = {}
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.move_left()
                    if not valid_space(current_piece, grid):
                        current_piece.move_right()
                if event.key == pygame.K_RIGHT:
                    current_piece.move_right()
                    if not valid_space(current_piece, grid):
                        current_piece.left()
                if event.key == pygame.K_DOWN:
                    current_piece.move_down()
                    if not valid_space(current_piece, grid):
                        current_piece.move_right()
                if event.key == pygame.K_UP:
                    current_piece.rotation()
                    if not valid_space(current_piece, grid):
                        current_piece.move_right()

        draw_window(win, grid)


def main_menu(win):
    main(win)


win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Tetris')
main_menu(win)  # start game