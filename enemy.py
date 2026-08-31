
import pygame
from constants import *
from bullet import Bullet
import random

class Enemy:
    def __init__(self, x, y):
        self.image = pygame.image.load('images/enemy.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (SIZE_ENEMY_X, SIZE_ENEMY_Y))
        self.rect = self.image.get_rect(topleft=(x, y))
    def move_enemy_left(self):
        self.rect.x -= SPEED_MOVE_ENEMY
        return self.rect
    def move_enemy_right(self):
        self.rect.x += SPEED_MOVE_ENEMY
        return self.rect
    def move_enemy_down(self):
        self.rect.y += SPEED_MOVE_ENEMY
        return self.rect
    def shooting(self):
        return Bullet(self.rect.x + 5, self.rect.y + 15,'images/bullet_enemy_1.png',SPEED_BULLET)

def move_enemy_down(enemy) :
    for i in range(len(enemy)):
        for j in range (len(enemy[i])):
            if enemy[i][j] is not None:
                if enemy[i][j].rect.y <= SIZEY - SIZE_ENEMY_Y:
                    enemy[i][j].move_enemy_down()

def move_enemy_right(enemy):
    for y in range(len(enemy)):
        for x in range(len(enemy[y])):
            if enemy[y][x] is not None:
                enemy[y][x].move_enemy_right()

def move_enemy_left(enemy):
    for y in range(len(enemy)):
        for x in range(len(enemy[y])):
            if enemy[y][x] is not None:
                enemy[y][x].move_enemy_left()

def border_check(enemy,bolean_T_R_F_L):
    if bolean_T_R_F_L is True:
        for y in range(len(enemy)-1,-1,-1):
            for x in range(len(enemy[y])):
                if enemy[y][x] is not None:
                    if enemy[y][x].rect.x >= SIZEX - SIZE_ENEMY_X:
                        move_enemy_down(enemy)
                        return False
        return True
    elif bolean_T_R_F_L is False:
        for y in range(len(enemy)):
            for x in range(len(enemy[y])):
                if enemy[y][x] is not None:
                    if enemy[y][x].rect.x <= 0:
                        move_enemy_down(enemy)
                        return True
        return False

def random_enemy(enemy):
    while True:
        value_nubmer_y = random.randint(0,len(enemy)-1)
        value_nubmer_x = random.randint(0,len(enemy[value_nubmer_y])-1)
        if enemy[value_nubmer_y][value_nubmer_x] is not None:
            return value_nubmer_y,value_nubmer_x

def add_enemy() :
    enemy_rect= [[None for _ in range(11)] for _ in range(5)]
    xenemy = 0
    yenemy = 40
    for i in range(5):
        for j in range(11):
            enemy_rect[i][j] = (Enemy(xenemy, yenemy))
            xenemy += SIZE_ENEMY_X + 10
        yenemy += 40
        xenemy = 0
    return enemy_rect