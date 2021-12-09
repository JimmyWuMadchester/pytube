# Snake Tutorial Python

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

COLOR_RED = (255, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)


class cube(object):
    rows = 0
    w = 0

    def __init__(self, start, dirnx=1, dirny=0, color=COLOR_RED):
        pass

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass


class snake(object):

    def __init__(self, color, pos):
        pass

    def move(self):
        pass

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        pass


def drawGrid(width, rows, surface):
    sizeBtwn = width // rows
    x = 0
    y = 0
    for line in range(rows):
        x += sizeBtwn
        y += sizeBtwn

        pygame.draw.line(surface, COLOR_WHITE, (x, 0), (x, width))
        pygame.draw.line(surface, COLOR_WHITE, (0, y), (width, y))


def redrawWindow(surface):
    global rows, width
    surface.fill(color=COLOR_BLACK)
    #drawGrid(width, rows, surface)
    
    pygame.display.update()


def randomSnack(rows, item):
    pass


def message_box(subject, content):
    pass


def main():
    global width, rows
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = snake(COLOR_RED, (10, 10))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redrawWindow(win)


main()
