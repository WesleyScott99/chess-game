import pygame
import sys
import random
from math import *

import chessAI
import main
import pieces
import interface

pygame.init()
width = 1800
height = 700
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

pieces.init(display)
main.init(display)
interface.init(display)

background = (51, 51, 51)

def close():
    pygame.quit()
    sys.exit()

def start_game(map):
    map.draw_map()

def GAME():
    welcome = interface.Label(700, 100, 400, 200, None, background)
    welcome.add_text("chess 2", 80, "Fonts/helvetica.ttf", (236, 240, 241))

    start = interface.Button(500, 400, 300, 100, start_game, (244, 208, 63), (247, 220, 111))
    start.add_text("START GAME", 60, "Fonts/helvetica.ttf", background)

    exit = interface.Button(1000, 400, 300, 100, close, (241, 148, 138), (245, 183, 177))
    exit.add_text("QUIT", 60, "Fonts/helvetica.ttf", background)

    mandav = interface.Button(width - 300, height - 80, 300, 100, None, background)
    mandav.add_text("MANDAV", 60, "Fonts/helvetica.ttf", (41, 41, 41))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit.isActive():
                    exit.action()
                if start.isActive():
                    start_game(map)

        display.fill(background)

        start.draw()
        exit.draw()
        welcome.draw()
        mandav.draw()

        pygame.display.update()
        clock.tick(60)

GAME()
