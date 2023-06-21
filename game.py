#!/usr/bin/env python3

import os
import pygame, sys

SCREEN_SIZE = (800, 715)
MAZE_SIZE = (28, 25)

ASCII_MAZE = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP           XX            X",
    "X XXXX XXXXX XX XXXXX XXXX X",
    "X XXXX XXXXX XX XXXXX XXXX X",
    "X XXXX XXXXX XX XXXXX XXXX X",
    "X                          X",
    "X XXXX XX XXXXXXXX XX XXXX X",
    "X XXXX XX XXXXXXXX XX XXXX X",
    "X      XX    XX    XX      X",
    "XXXXXX XXXXX XX XXXXX XXXXXX",
    "XXXXXX XX          XX XXXXXX",
    "XXXXXX XX XXX  XXX XX XXXXXX",
    "       XX X G  G X XX       ",
    "XXXXXX XX X G  G X XX XXXXXX",
    "XXXXXX XX XXXXXXXX XX XXXXXX",
    "XXXXXX XX          XX XXXXXX",
    "XXXXXX XX XXXXXXXX XX XXXXXX",
    "X            XX            X",
    "X XXXX XXXXX XX XXXXX XXXX X",
    "X   XX                XX   X",
    "XXX XX XX XXXXXXXX XX XX XXX",
    "X      XX    XX    XX      X",
    "X XXXXXXXXXX XX XXXXXXXXXX X",
    "XP                         X",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
]

class PacmanSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(PacmanSprite, self).__init__()
        self.image = pygame.image.load(os.path.join('resources', 'pacman.png'))
        self.rect = self.image.get_rect()

    def set_rect(self, coordinate):
        self.rect = self.image.get_rect()
        self.rect.center = coordinate

class Board:
    BLUE = (0, 0, 255)
    def __init__(self):
        self.group = pygame.sprite.Group()
        self.pacman_sprite = PacmanSprite()
        self.group.add(self.pacman_sprite)
        self.maze_matrix = [list(row) for row in ASCII_MAZE]


    def init_draw(self, screen):
        for x, a in enumerate(self.maze_matrix):
            for y, b in enumerate(a):
                if b == 'X':
                    pygame.draw.rect(screen, self.BLUE, (x * MAZE_SIZE[0], y * MAZE_SIZE[1], 30, 30))

    def draw(self, screen):
        for x, a in enumerate(self.maze_matrix):
            for y, b in enumerate(a):
                if b == 'P':
                    self.pacman_sprite.set_rect((x * MAZE_SIZE[0], y * MAZE_SIZE[1]))
        self.group.draw(screen)




class Pacman():
    INIT_POS = (14, 11)
    lifes : int = 3
    coordinate : (int, int) = INIT_POS
    direction : str = 'right'

    def dir2vector(self):
        if self.direction == 'up':
            return (0, -1)
        elif self.direction == 'down':
            return (0, 1)
        elif self.direction == 'left':
            return (-1, 0)
        elif self.direction == 'right':
            return (1, 0)

    def update(self, board, keys) -> None:
        if keys[pygame.K_UP]:
            self.direction = 'up'
        elif keys[pygame.K_DOWN]:
            self.direction = 'down'
        elif keys[pygame.K_LEFT]:
            self.direction = 'left'
        elif keys[pygame.K_RIGHT]:
            self.direction = 'right'

        vec = self.dir2vector()
        next_pos = (self.coordinate[0] + vec[0], self.coordinate[1] + vec[1])
        next_val = board.maze_matrix[next_pos[0]][next_pos[1]] 

        if next_val == 'X':
            return
        elif next_val == 'G':
            # need to respawn
            self.lifes -= 1
            next_pos = INIT_POS
        
        board.maze_matrix[self.coordinate[0]][self.coordinate[1]] = ' '
        board.maze_matrix[next_pos[0]][next_pos[1]] = 'P'
        self.coordinate = next_pos


def loop():
    pygame.init()

    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Pacman")

    player = Pacman()
    running = True

    board = Board()
    board.init_draw(screen)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break

        keys = pygame.key.get_pressed()
        player.update(board, keys)
        board.draw(screen)
        pygame.display.flip()

    pygame.quit()


def main():
    loop()


main()
