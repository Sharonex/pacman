#!/usr/bin/env python3

import os
import pygame, sys

SCREEN_SIZE = (800, 715)
MAZE_SIZE = (28, 25)

ASCII_MAZE = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "X            XX            X",
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
    "       XX X I  C X XX       ",
    "XXXXXX XX X Y  B X XX XXXXXX",
    "XXXXXX XX XXXXXXXX XX XXXXXX",
    "XXXXXX XX          XX XXXXXX",
    "XXXXXX XX XXXXXXXX XX XXXXXX",
    "X            XX            X",
    "X XXXX XXXXX XX XXXXX XXXX X",
    "X   XX                XX   X",
    "XXX XX XX XXXXXXXX XX XX XXX",
    "X      XX    XX    XX      X",
    "X XXXXXXXXXX XX XXXXXXXXXX X",
    "X           P              X",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
]

class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self,  asset_name):
        super().__init__()
        self.image = pygame.image.load(os.path.join('resources', asset_name + '.png'))
        self.rect = self.image.get_rect()

    def set_rect(self, coordinate):
        self.rect = self.image.get_rect()
        self.rect.topleft = coordinate


class PacmanSprite(PlayerSprite):
    def __init__(self):
        super().__init__('pacman')

class GhostSprite(PlayerSprite):
    def __init__(self, name):
        super().__init__(name)

class Board:
    BLUE = (0, 0, 255)
    def __init__(self):
        self.group = pygame.sprite.Group()
        self.pacman_sprite = PacmanSprite()
        self.inky_sprite = GhostSprite('inky')
        self.clyde_sprite = GhostSprite('clyde')
        self.pinky_sprite = GhostSprite('pinky')
        self.blinky_sprite = GhostSprite('blinky')
        self.group.add(self.pacman_sprite)
        self.group.add(self.inky_sprite)
        self.group.add(self.clyde_sprite)
        self.group.add(self.pinky_sprite)
        self.group.add(self.blinky_sprite)
        self.maze_matrix = [list(row) for row in ASCII_MAZE]

    def draw(self, screen):
        BLOCK_SIZE = (SCREEN_SIZE[0] / MAZE_SIZE[0], SCREEN_SIZE[1] / MAZE_SIZE[1])
        for x, a in enumerate(self.maze_matrix):
            for y, b in enumerate(a):
                if b == 'X':
                    pygame.draw.rect(screen, self.BLUE, (y * BLOCK_SIZE[0], x * BLOCK_SIZE[1], BLOCK_SIZE[0], BLOCK_SIZE[1]))
                if b == 'P':
                    self.pacman_sprite.set_rect((y * BLOCK_SIZE[0], x * BLOCK_SIZE[1]))
                if b == 'I':
                    self.inky_sprite.set_rect((y * BLOCK_SIZE[0], x * BLOCK_SIZE[1]))
                if b == 'Y':
                    self.pinky_sprite.set_rect((y * BLOCK_SIZE[0], x * BLOCK_SIZE[1]))
                if b == 'C':
                    self.clyde_sprite.set_rect((y * BLOCK_SIZE[0], x * BLOCK_SIZE[1]))
                if b == 'B':
                    self.blinky_sprite.set_rect((y * BLOCK_SIZE[0], x * BLOCK_SIZE[1]))

        self.group.draw(screen)

class Pacman():
    lifes : int = 3
    coordinate : (int, int) = (-1, -1)
    direction : (int, int) = (0, 0)

    def __init__(self, board) -> None:
        for x, a in enumerate(board.maze_matrix):
            for y, b in enumerate(a):
                if b == 'P':
                    self.INIT_POS = (x, y)
        self.coordinate = self.INIT_POS

    def update(self, board, direction) -> None:
        self.direction = direction

        next_pos = (self.coordinate[0] + self.direction[0], self.coordinate[1] + self.direction[1])
        next_val = board.maze_matrix[next_pos[0]][next_pos[1]]

        if next_val == 'X':
            return
        elif next_val in ('I', 'Y', 'C', 'B'):
            # need to respawn
            self.lifes -= 1
            next_pos = self.INIT_POS

        board.maze_matrix[self.coordinate[0]][self.coordinate[1]] = ' '
        board.maze_matrix[next_pos[0]][next_pos[1]] = 'P'
        self.coordinate = next_pos


def loop():
    pygame.init()

    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Pacman")

    running = True

    board = Board()
    player = Pacman(board)
    clock = pygame.time.Clock()

    direction = (0, 0)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key == pygame.K_LEFT:
                    direction = (0, -1)
                if event.key == pygame.K_RIGHT:
                    direction = (0, 1)
                if event.key == pygame.K_UP:
                    direction = (-1, 0)
                if event.key == pygame.K_DOWN:
                    direction = (1, 0)

        player.update(board, direction)
        screen.fill((0, 0, 0))
        board.draw(screen)
        pygame.display.flip()
        clock.tick(5)

    pygame.quit()


def main():
    loop()


main()
