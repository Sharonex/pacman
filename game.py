#!/usr/bin/env python3

import os
import time
import pygame, sys
from pygame import mixer

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
        self.orig_image = pygame.image.load(os.path.join('resources', asset_name + '.png'))
        self.image = self.orig_image
        self.rect = self.image.get_rect()

    def set_rect(self, coordinate):
        self.rect = self.image.get_rect()
        self.rect.topleft = coordinate

class PacmanSprite(PlayerSprite):
    coordinate : (int, int) = (-1, -1)
    direction : str = 'right'

    def __init__(self):
        super().__init__('pacman')

    def update(self):
        super().update()
        if self.direction == (-1, 0): # up
            self.image = pygame.transform.rotate(self.orig_image, 90)
        elif self.direction == (0, 1): # right
            self.image = self.orig_image
        elif self.direction == (0, -1): # left
            self.image = pygame.transform.rotate(self.orig_image, 180)
            self.image = pygame.transform.flip(self.image, False, True)
        elif self.direction == (1, 0): # down
            self.image = pygame.transform.rotate(self.orig_image, 270)


class GhostSprite(PlayerSprite):
    def __init__(self, name):
        super().__init__(name)

class Board:
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
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
                if b == ' ':
                    pygame.draw.circle(screen, self.WHITE, (y * BLOCK_SIZE[0]+ BLOCK_SIZE[0]/2, x * BLOCK_SIZE[1] + BLOCK_SIZE[1]/2), 2)
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

        self.group.update()
        self.group.draw(screen)

class Pacman():
    lifes : int = 1

    def __init__(self, board) -> None:
        for x, a in enumerate(board.maze_matrix):
            for y, b in enumerate(a):
                if b == 'P':
                    self.INIT_POS = (x, y)
        board.pacman_sprite.coordinate = self.INIT_POS
        self.score = 0

    def update(self, board, direction) -> bool:
        board.pacman_sprite.direction = direction

        next_pos = (board.pacman_sprite.coordinate[0] + board.pacman_sprite.direction[0], board.pacman_sprite.coordinate[1] + board.pacman_sprite.direction[1])
        next_val = board.maze_matrix[next_pos[0]][next_pos[1]]

        if next_val == 'X':
            return
        if next_val == ' ':
            self.score += 1
        elif next_val in ('I', 'Y', 'C', 'B'):
            # need to respawn
            self.lifes -= 1
            if self.lifes == 0:
                return True
            next_pos = self.INIT_POS

        board.maze_matrix[board.pacman_sprite.coordinate[0]][board.pacman_sprite.coordinate[1]] = 'E'
        board.maze_matrix[next_pos[0]][next_pos[1]] = 'P'
        board.pacman_sprite.coordinate = next_pos

        return False


def loop():
    pygame.init()

    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Pacman")

    running = True
    pygame.font.init()
    font = pygame.font.Font(None, 36)


    board = Board()
    player = Pacman(board)
    clock = pygame.time.Clock()
    #Instantiate mixer
    mixer.init()

    #Load audio file
    mixer.music.load(os.path.join('resources', 'pacman_theme.mp3'))

    print("music started playing....")

    #Set preferred volume
    mixer.music.set_volume(0.2)

    #Play the music
    mixer.music.play()

    board.pacman_sprite.direction = (0, 0)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    board.pacman_sprite.direction = (0, -1)
                if event.key == pygame.K_RIGHT:
                    board.pacman_sprite.direction = (0, 1)
                if event.key == pygame.K_UP:
                    board.pacman_sprite.direction = (-1, 0)
                if event.key == pygame.K_DOWN:
                    board.pacman_sprite.direction = (1, 0)

        if player.update(board, board.pacman_sprite.direction):
            mixer.music.stop()
            mixer.music.load(os.path.join('resources', 'game_over.mp3'))
            mixer.music.play()
            image = pygame.image.load(os.path.join('resources', 'game_over.png'))
            screen.blit(image,(0,0))
            pygame.display.flip()

            time.sleep(5)
            running = False


        screen.fill((0, 0, 0))
        board.draw(screen)
        score_text = font.render(f'Score: {player.score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(5)

    pygame.quit()


def main():
    loop()


main()
