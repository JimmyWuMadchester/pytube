# Snake Tutorial Python

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

COLOR_RED = (255, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_GREEN = (0, 255, 0)


class cube(object):
    rows = 20
    w = 500

    def __init__(self, start, dirnx=1, dirny=0, color=COLOR_RED):
        self.pos = start
        self.dirnx = dirnx
        self.dirny = dirny
        self.color = color


    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i*dis +1, j*dis +1, dis -2, dis -2))

        if eyes:
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis +centre-radius, j*dis +8)
            circleMiddle2 = (i*dis + dis -radius*2, j*dis +8)
            pygame.draw.circle(surface, COLOR_BLACK, circleMiddle, radius)
            pygame.draw.circle(surface, COLOR_BLACK, circleMiddle2, radius)


class snake(object):
    body = []
    turns = {}
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx, self.dirny = 0, 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:     self.dirnx, self.dirny = -1, 0
                elif keys[pygame.K_RIGHT]:  self.dirnx, self.dirny = 1, 0
                elif keys[pygame.K_UP]:     self.dirnx, self.dirny = 0, -1
                elif keys[pygame.K_DOWN]:   self.dirnx, self.dirny = 0, 1

            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i, c in enumerate(self.body):
            p = c.pos

            if p in self.turns:
                (dirnx, dirny) = self.turns[p]
                c.move(dirnx, dirny)

                # check if tail turned then remove position in turns dict
                if i == len(self.body) - 1:
                    self.turns.pop(p)

            else:
                if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0,c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0],c.rows-1)
                else: c.move(c.dirnx, c.dirny)

    def reset(self, pos):
        pass

    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        last_pos = (tail.pos[0]-dx, tail.pos[1]-dy)
        new_tail = cube(last_pos, dx, dy)
        self.body.append(new_tail)



    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)


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
    global rows, width, s, snack
    surface.fill(color=COLOR_BLACK)
    s.draw(surface)
    snack.draw(surface)
    drawGrid(width, rows, surface)
    
    pygame.display.update()


def randomSnack(rows, item):
    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)

        # regenerate snack if it is generated in snake's body
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break
    
    return (x, y)


def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


def main():
    global width, rows, s, snack
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = snake(COLOR_RED, (10, 10))
    snack = cube(randomSnack(rows, s), color=COLOR_GREEN)

    flag = True

    clock = pygame.time.Clock()
    redrawWindow(win)
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        s.move()

        if s.head.pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows, s), color=COLOR_GREEN)

        redrawWindow(win)
        

    pass

main()
