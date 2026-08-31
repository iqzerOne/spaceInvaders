import pygame
from pygame.locals import *
from constants import *
from bullet import Bullet

class Player:
    def __init__(self):
        self.x = SIZEX/2
        self.y = SIZEY-SIZE_PLAYER_Y
        self.image = pygame.image.load('images/weapon1.png').convert_alpha()
        self.player = pygame.transform.scale(self.image, (SIZE_PLAYER_X, SIZE_PLAYER_Y))
        self.rect = self.player.get_rect(topleft = (self.x, self.y))

    def move(self,direction):
        if direction:
            if self.rect.x > 0 and self.rect.x < SIZEX - SIZE_PLAYER_X:
                if direction == K_LEFT:
                    self.rect.x -= SPEED_MOVE_PLAYER
                elif direction == K_RIGHT:
                    self.rect.x += SPEED_MOVE_PLAYER
            else :
                if self.rect.x < 250:
                    self.rect.x +=1
                else :
                    self.rect.x -=1

    def shooting(self):
        return Bullet(self.rect.x + 18, self.rect.y - 15,'images/bullet3.png',-SPEED_BULLET)

def bullet_player(bullets_player,enemy_rect,score):
    bullets_alive = []
    for bullet in bullets_player:
        hit = False
        SCREEN.blit(bullet.image,(bullet.rect.x,bullet.rect.y))
        bullet.movement_bullet()
        for y in range(len(enemy_rect)):
            for x in range(len(enemy_rect[y])):
                if enemy_rect[y][x] is not None:
                    if bullet.rect.colliderect(enemy_rect[y][x].rect):
                        enemy_rect[y][x] = None
                        score += 10
                        hit = True
        if bullet.rect.y > 0 and not hit:
            bullets_alive.append(bullet)
    return bullets_alive,score