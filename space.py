import pygame, sys
from pygame.locals import *
import random

pygame.init()

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
SPEED_BULLET_ENEMY = 10
SPEED_BULLET_PLAYER = 10
LIVE = 5
SCORE = 0
SCREEN = pygame.display.set_mode((SIZEX, SIZEY))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255,0,0)

# Шрифт
FONT_MAIN_MENU = pygame.font.Font(None, 50)
FONT_GAME = pygame.font.Font(None, 30)




def argument1() :
    number = int(sys.argv[1])

    return int(number)
#-----
def argument2() :
    number = int(sys.argv[2])

    return int(number)

#------Движение игрока
def move_player(direction, player):
    if direction:
        if player.x > 0 and player.x < SIZEX - SIZE_PLAYER_X:
            if direction == K_LEFT:
                player.x -= SPEED_MOVE_PLAYER
            elif direction == K_RIGHT:
               player.x += SPEED_MOVE_PLAYER
        else :
            if player.x < 250:
                player.x +=1
            else :
                player.x -=1

    return player
    #----
#------------Движение врагов вниз
def move_enemy_down(enemy_more) :
    for i in range(len(enemy_more)):
        for j in range (len(enemy_more[i])):
            if enemy_more[i][j] is not None:
                if enemy_more[i][j].y != SIZEY - SIZE_ENEMY_Y:
                    enemy_more[i][j].y += 10
    return enemy_more
    #----
#------------Движение врагов налево или направо взависимости от флага
def move_enemy_L_or_R(enemy_more,flag) :
    if flag == 1:
        for i in range (len(enemy_more)) :
            for j in range(len(enemy_more[i])):
                if enemy_more[i][j] is not None:
                    enemy_more[i][j].x += SPEED_MOVE_ENEMY
    if flag == 0:
        for i in range (len(enemy_more)) :
            for j in range(len(enemy_more[i])):
                if enemy_more[i][j] is not None:
                    enemy_more[i][j].x -= SPEED_MOVE_ENEMY

    return enemy_more
#------------Добавление врагов в 2 массив
def add_enemy(enemy) :
    enemy_more_rect= [[None for _ in range(11)] for _ in range(5)]
    xenemy = 0
    yenemy = 0
    for i in range(5):
        for j in range(11):
            enemy_more_rect[i][j] = (enemy.get_rect(topleft = (xenemy,yenemy)))
            xenemy += SIZE_ENEMY_X + 10
        yenemy += 50
        xenemy = 0
    return enemy_more_rect

#------------Стрельба врагов.
def shoot_enemy(bullet_enemy_array,pic_bullet,enemy):
    Random = True
    while Random:        
        value_nubmer_y = random.randint(0,len(enemy)-1)
        value_nubmer_x = random.randint(0,len(enemy[value_nubmer_y])-1)

        if (enemy[value_nubmer_y][value_nubmer_x] is not None):
            if value_nubmer_y == len(enemy) - 1:
                bullet_enemy_array.append(pic_bullet.get_rect(topleft = (enemy[value_nubmer_y][value_nubmer_x].x,enemy[value_nubmer_y][value_nubmer_x].y)))
                return bullet_enemy_array
            elif value_nubmer_y < len(enemy) - 1:
                for i in range(len(enemy)-1,value_nubmer_y-1,-1):        
                    if enemy[i][value_nubmer_x] != None:
                        break
                    if value_nubmer_y+1 == i:
                        Random = False
                if not Random :
                    bullet_enemy_array.append(pic_bullet.get_rect(topleft = (enemy[value_nubmer_y][value_nubmer_x].x,enemy[value_nubmer_y][value_nubmer_x].y)))
                    return bullet_enemy_array
#---


def draw_text(text, font, surface, x, y,color):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def draw_live(value,font,surface,x,y):
    text_live = str(value)
    textobj = font.render(text_live, True, WHITE)  # Рендерим текст
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)  # Устанавливаем позицию текста
    surface.blit(textobj, textrect)  # Отображаем текст на экране


def win():

    clock = pygame.time.Clock()
    pygame.display.set_caption("space invaders")

    pygame.display.flip()
    # Изображения
    im_pause = pygame.image.load('images/pause-button.png').convert_alpha()
    im_pause = pygame.transform.scale(im_pause, (200,200))
    player = pygame.image.load('images/weapon1.png').convert_alpha()
    player = pygame.transform.scale(player, (SIZE_PLAYER_X, SIZE_PLAYER_Y))
    enemy = pygame.image.load('images/enemy.png').convert_alpha()
    enemy = pygame.transform.scale(enemy, (SIZE_ENEMY_X, SIZE_ENEMY_Y))
    bg = pygame.image.load('images/bg1.jpg').convert_alpha()
    bg = pygame.transform.scale(bg,(SIZEX,SIZEY))
    bullet = pygame.image.load('images/bullet3.png').convert_alpha()
    bullet = pygame.transform.scale(bullet, (SIZE_BULLET_X, SIZE_BULLET_Y))
    bullet_enemy = pygame.image.load('images/bullet_enemy_1.png').convert_alpha()
    bullet_enemy =  pygame.transform.scale(bullet_enemy, (SIZE_BULLET_X, SIZE_BULLET_Y))  
    # gameover = pygame.image.load('images/gameover.png').convert_alpha()
    pos_x,pos_y= SIZEX/2,SIZEY-SIZE_PLAYER_Y #player
    im_pause_rect = im_pause.get_rect()
    im_pause_rect.center = (SIZEX // 2, SIZEY // 2)
    runGame = True # флаг выхода из цикла игры
    direction = False
    flag = 1
    k_fire = False
    bullets_rect = []
    bullet_enemy_rect = []
    live = LIVE
    score = SCORE
    start_time = pygame.time.get_ticks()
    b_pause = False


    player_rect = player.get_rect(topleft = (pos_x,pos_y))
    enemy_more_rect = add_enemy(enemy)

    rect_color = (0,255,0)
    #Цикл запуска игры
    while runGame:
        #Обновление дисплея
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                runGame = False
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
            SCREEN.blit(player,(player_rect.x,player_rect.y))

            draw_live(live,FONT_GAME,SCREEN,20,20)
            draw_live(score,FONT_GAME,SCREEN,SIZEX - 100,SIZEY - SIZEY + 20)
            # ----Прорисовка врагов
            for i in range(len(enemy_more_rect)) :
                for j in range(len(enemy_more_rect[i])):
                    if enemy_more_rect[i][j] is not None:
                        SCREEN.blit(enemy,(enemy_more_rect[i][j].x,enemy_more_rect[i][j].y))
            # ----     
        
            # ----Переодичность стрельбы врагов

            if current_time - start_time > TIME_SHOOT_ENEMY:
                bullet_enemy_rect = shoot_enemy(bullet_enemy_rect,bullet_enemy,enemy_more_rect)
                start_time = pygame.time.get_ticks()

            #------Массив передвижение снарядов врагов и проверка на попадание.И так же удаление
            bullet_enemy_pos =[]
            if bullet_enemy_rect is not None: 
                for bullet_en in bullet_enemy_rect.copy():
                    bullet_en.y += SPEED_BULLET_ENEMY
                    SCREEN.blit(bullet_enemy,(bullet_en.x,bullet_en.y))
                    if bullet_en.colliderect(player_rect):
                        if bullet_en in bullet_enemy_rect:
                            bullet_enemy_rect.remove(bullet_en)
                        live-=1
            #------Изменение координат игрока
            player_rect = move_player(direction,player_rect)
            #------Добавление снаряда игрока если переменная равна Пробелу.
            if k_fire == K_SPACE:
                bullets_rect.append(bullet.get_rect(topleft = (player_rect.x + 18,player_rect.y - 15)))

            k_fire = False
            bullets_rect_positive = []
            #-----Отрисовка снаряда игрока и проверка на попадание(Отдельная функция)
            for bullets in bullets_rect.copy():
                SCREEN.blit(bullet,(bullets.x,bullets.y))
                bullets.y -= SPEED_BULLET_PLAYER
                for i in range(len(enemy_more_rect)):
                    for j in range(len(enemy_more_rect[i])):
                        if enemy_more_rect[i][j] is not None:
                            if bullets.colliderect(enemy_more_rect[i][j]):
                                enemy_more_rect[i][j] = None
                                score += 10
                                if bullets in bullets_rect:
                                    bullets_rect.remove(bullets)
                                    i = len(enemy_more_rect)-1
                                    j = len(enemy_more_rect)-1

            #-------Удаление снарядов за экраном
            for i in range(len(bullets_rect)) :
                if bullets_rect[i].y > 0 :
                    bullets_rect_positive.append(bullets_rect[i])

            for i in range(len(bullet_enemy_rect)):
                if bullet_enemy_rect[i].y < SIZEY:
                    bullet_enemy_pos.append(bullet_enemy_rect[i])

            bullet_enemy_rect = bullet_enemy_pos
            bullets_rect = bullets_rect_positive

            if live <= 0:
                main_menu()


            #-----Проверка на нахождение врагов
            for i in range(len(enemy_more_rect)):
                for j in range(len(enemy_more_rect[i])):
                    if enemy_more_rect[i][j] is not None:
                        if enemy_more_rect[i][j].x >= SIZEX - SIZE_ENEMY_X or enemy_more_rect[i][j].x <= 0:
                            if flag == 1 and enemy_more_rect[i][j].x >= SIZEX - SIZE_ENEMY_X:
                                flag = 0
                            if flag == 0 and enemy_more_rect[i][j].x <= 0:
                                flag = 1
                            enemy_more_rect = move_enemy_down(enemy_more_rect)
            # ---- Движение влево или вправо
            enemy_more_rect = move_enemy_L_or_R(enemy_more_rect,flag)
            #---- Ограничение кадров.
            clock.tick(30)
            # ----


def main_menu():
    running = True
    mouse_pos = 0;       
    text_surface_game = FONT_MAIN_MENU.render("Начать игру", True, WHITE)
    text_rect_game = text_surface_game.get_rect(center=(SIZEX / 2, SIZEY / 2))
    text_surface_exit = FONT_MAIN_MENU.render("Выход", True, WHITE)
    text_rect_exit = text_surface_exit.get_rect(center=(SIZEX / 2, SIZEY / 2+200))
    while running:
        
        SCREEN.fill(BLACK)
        SCREEN.blit(text_surface_game, text_rect_game)
        SCREEN.blit(text_surface_exit, text_rect_exit)
        draw_text("Главное меню", FONT_MAIN_MENU, SCREEN, SIZEX/2-120, 100,RED)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Нажатие Enter для начала игры
                    win()
                if event.key == pygame.K_ESCAPE:  # Нажатие Escape для выхода
                    pygame.quit()
                    sys.exit()
            mouse_pos = pygame.mouse.get_pos()
            mouse_buttons = pygame.mouse.get_pressed()

            if text_rect_game.collidepoint(mouse_pos):  # Проверяем, попала ли мышь в текст
                text_surface_game = FONT_MAIN_MENU.render("Начать игру", True, RED)
                if mouse_buttons[0] and text_rect_game.collidepoint(mouse_pos):
                    win()
            else:
                text_surface_game = FONT_MAIN_MENU.render("Начать игру", True, WHITE)

            if text_rect_exit.collidepoint(mouse_pos):  # Проверяем, попала ли мышь в текст
                text_surface_exit = FONT_MAIN_MENU.render("Выход", True, RED)
                if mouse_buttons[0] and text_rect_exit.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
            else:
                text_surface_exit = FONT_MAIN_MENU.render("Выход", True, WHITE)


        pygame.display.flip()

if __name__ == '__main__':
    main_menu()