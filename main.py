import pygame, sys
from pygame.locals import *
pygame.init()
from constants import *
from bullet import *
from enemy import *
from player import *
from screens import *
from game import *
    

def game_change():
    game_state = "main_menu"
    score = SCORE
    while True:
        if game_state == "main_menu":
            game_state = main_menu(game_state)
        elif game_state == "play":
            game_state, score = play()
        elif game_state == "win":
            game_state = win(score,game_state)
        elif game_state == "lose":
            game_state = game_over(score,game_state)
    

if __name__ == '__main__':
    game_change()