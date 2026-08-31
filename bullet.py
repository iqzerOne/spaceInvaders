import pygame
from constants import *

class Bullet:
    def __init__(self, x, y,image,speed):
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (SIZE_BULLET_X, SIZE_BULLET_Y))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed
    def movement_bullet(self):
        self.rect.y += self.speed
        return self.rect