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

class Board:
    def __init__():
        pass

    def draw(self, screen):
        for x, a in enumerate(self.ascii_maze):
            for y, b in enumerate(x):
                pass



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
