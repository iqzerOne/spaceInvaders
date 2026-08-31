import pygame

pygame.display.set_caption("space invaders")
TIME_SHOOT_ENEMY = 1000
SIZEX = 700
SIZEY = 700
SIZE_PLAYER_X = 50
SIZE_PLAYER_Y = 30
SIZE_ENEMY_X = 20
SIZE_ENEMY_Y = 20
SIZE_BULLET_X = 15
SIZE_BULLET_Y = 15
SPEED_MOVE_ENEMY = 2
SPEED_MOVE_PLAYER = 5
SPEED_BULLET = 10

LIVE = 5
SCORE = 0

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255,0,0)

SCREEN = pygame.display.set_mode((SIZEX, SIZEY))
FONT_MAIN_MENU = pygame.font.Font(None, 50)
FONT_GAME = pygame.font.Font(None, 30)

im_pause = pygame.image.load('images/pause-button.png').convert_alpha()
im_pause = pygame.transform.scale(im_pause, (200,200))
bg = pygame.image.load('images/bg1.jpg').convert_alpha()
bg = pygame.transform.scale(bg,(SIZEX,SIZEY))  
im_pause_rect = im_pause.get_rect()
im_pause_rect.center = (SIZEX // 2, SIZEY // 2)