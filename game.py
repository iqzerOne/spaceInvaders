import pygame, sys
from pygame.locals import *
from constants import *
from bullet import *
from enemy import *
from player import *
from screens import *

def next_level():
    pass

def play():
    clock = pygame.time.Clock()
    pygame.display.flip()
    player = Player()
    bullets_player = []
    direction = False
    boolean_T_R_F_L = True
    k_fire = False
    bullet_enemy= []
    level = 1
    time_shoot_enemy = TIME_SHOOT_ENEMY
    last_shoot = 0
    live = LIVE
    score = SCORE
    start_time = pygame.time.get_ticks()
    b_pause = False
    enemy_rect = add_enemy()
    while True:
        #Обновление дисплея
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:#Если нажата кнопка
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:#esc или p пауза  
                    b_pause = not b_pause
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :#Изменение переменной и добавление в нее значения клавиши
                    direction = event.key
            if event.type == KEYUP:  
                direction = False#если клавиша поднята флаг меняется на ложь и запись клавиши стирается
                k_fire = event.key#кнопка стрельбы

        if b_pause:
            SCREEN.blit(im_pause,im_pause_rect)
        if not b_pause:
            current_time = pygame.time.get_ticks()
            SCREEN.blit(bg,(0,0)) #Задний фон
            SCREEN.blit(player.player,(player.rect.x,player.rect.y))

            draw_live(live,FONT_GAME,SCREEN,20,20)
            draw_live(score,FONT_GAME,SCREEN,SIZEX - 100,SIZEY - SIZEY + 20)
            # ----Прорисовка врагов
            value_enemy = 0
            for i in range(len(enemy_rect)) :
                for j in range(len(enemy_rect[i])):
                    if enemy_rect[i][j] is not None:
                        value_enemy += 1
                        SCREEN.blit(enemy_rect[i][j].image,(enemy_rect[i][j].rect.x,enemy_rect[i][j].rect.y))
                        if enemy_rect[i][j].rect.colliderect(player.rect):
                            return "lose",score
            if live <= 0:
                return "lose",score
            if value_enemy == 0:
                if level >= 2:
                    return "win",score
                level += 1
                del bullets_player[:]
                del bullet_enemy [:]
                time_shoot_enemy = 700
                enemy_rect = add_enemy()
            #------Изменение координат игрока
            player.move(direction)
            #------Добавление снаряда игрока если переменная равна Пробелу.
            if current_time - last_shoot >= player.cooldown_shoot:
                if k_fire == K_SPACE:
                    bullets_player.append(player.shooting())
                    k_fire = False
                    last_shoot = current_time
            else:
                k_fire = False
                        
            bullets_player,score = bullet_player(bullets_player,enemy_rect,score)

            if boolean_T_R_F_L is True:
                move_enemy_right(enemy_rect)
            elif boolean_T_R_F_L is False:
                move_enemy_left(enemy_rect)

            boolean_T_R_F_L = border_check(enemy_rect,boolean_T_R_F_L)
            # ----Переодичность стрельбы врагов
            if current_time - start_time > time_shoot_enemy:
                value_nubmer_y,value_nubmer_x = random_enemy(enemy_rect)
                bullet_enemy.append(enemy_rect[value_nubmer_y][value_nubmer_x].shooting())
                start_time = pygame.time.get_ticks()
            bullet_alive_enemy = []

            if bullet_enemy is not None: 
                for bullet in bullet_enemy:
                    bullet.movement_bullet()
                    SCREEN.blit(bullet.image,(bullet.rect.x,bullet.rect.y))
                    if bullet.rect.colliderect(player.rect):
                        live-=1
                    if bullet.rect.y < SIZEY and not bullet.rect.colliderect(player.rect):
                        bullet_alive_enemy.append(bullet)
            bullet_enemy = bullet_alive_enemy
            #---- Ограничение кадров.
            clock.tick(30)