#!/usr/bin/env python3

import os
import pygame, sys

SCREEN_SIZE = (800, 800)
MAZE_SIZE = (28, 28)

ASCII_MAZE = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP           XX            X",
    "X XXXX XXXXX XX XXXXX XXXX X",
    "X XXXX XXXXX XX XXXXX XXXX X",
    "X XXXX XXXXX XX XXXXX XXXX X",
    "X                          X",
    "X XXXX XX XXXXXXXX XX XXXX X",
    "X XXXX XX XXXXXXXX XX XXXX X",
    "X XXXX XX X G  G X XX XXXX X",
    "X XXXX XX X  G     XX XXXX X",
    "X XXXX XX XXXXXXXX XX XXXX X",
    "X XXXX XX XXXXXXXX XX XXXX X",
    "X                          X",
    "X XXXX XXXXX XX XXXXX XXXX X",
    "X XXXX XXXXX XX XXXXX XXXX X",
    "X XXXX XXXXX XX XXXXX XXXX X",
    "XP           XX            X",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
]

def convert_to_pixel(maze_size, screen_size) -> int:



class Board:
    def __init__():

    def draw(self, screen):
        for x, a in enumerate(self.ascii_maze):
            for y, b in enumerate(x):



class Pacman(pygame.sprite.Sprite):
    lifes : int = 3
    coordinate : (int, int) = (14, 11)
    direction : str = 'right'


    def __init__(self):
        super(Pacman, self).__init__()
        self.image = pygame.image.load(os.path.join('resources', 'pacman.png'))
        self.rect = self.image.get_rect()
        self.rect.center = self.coordinate

    def update(self, keys) -> None:
        pass


def loop():
    pygame.init()

    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Pacman")

    player = Pacman()
    running = True

    group = pygame.sprite.RenderPlain()
    group.add(player)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break

        keys = pygame.key.get_pressed()
        player.update(keys)
        group.draw(screen)
        pygame.display.flip()

    pygame.quit()


def main():
    loop()


main()
