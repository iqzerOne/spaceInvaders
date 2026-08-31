from constants import *
import pygame,sys
from pygame.locals import *

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

def game_over(score,game_state):
    button_new_game = "Заново"
    button_exit = "Выход"
    list_button = [button_new_game, button_exit] 
    event = display_pygame_event(list_button,game_state,score)
    return event

def win(score,game_state):
    button_new_game = "Заново"
    button_exit = "Выход"
    list_button = [button_new_game, button_exit] 
    event = display_pygame_event(list_button,game_state,score)
    return event

def display_pygame_event(list_button, game_state,score):
    mouse_pos = 0
    text_surface_game = FONT_MAIN_MENU.render(list_button[0], True, WHITE)
    text_surface_exit = FONT_MAIN_MENU.render(list_button[1], True, WHITE)
    text_rect_game = text_surface_game.get_rect(center=(SIZEX / 2, SIZEY / 2))
    text_rect_exit = text_surface_exit.get_rect(center=(SIZEX / 2, SIZEY / 2+200))
    while True:
        SCREEN.fill(BLACK)
        SCREEN.blit(text_surface_game, text_rect_game)
        SCREEN.blit(text_surface_exit, text_rect_exit)

        if game_state == "main_menu":
            draw_text("Главное меню", FONT_MAIN_MENU, SCREEN, SIZEX/2-120, 100,RED)

        if game_state == "win":
            draw_live(score,FONT_GAME,SCREEN,SIZEX - 100, 20)
            draw_text("Вы победили!", FONT_MAIN_MENU, SCREEN, SIZEX/2-120, 100,RED)

        if game_state == "lose":
            draw_live(score,FONT_GAME,SCREEN,SIZEX - 100, 20)
            draw_text("Вы проиграли", FONT_MAIN_MENU, SCREEN, SIZEX/2-120, 100,RED)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Нажатие Enter для начала игры
                    return "play"
                if event.key == pygame.K_ESCAPE:  # Нажатие Escape для выхода
                    pygame.quit()
                    sys.exit()
            mouse_pos = pygame.mouse.get_pos()
            mouse_buttons = pygame.mouse.get_pressed()

            if text_rect_game.collidepoint(mouse_pos):  # Проверяем, попала ли мышь в текст
                text_surface_game = FONT_MAIN_MENU.render(list_button[0], True, RED)
                if mouse_buttons[0] and text_rect_game.collidepoint(mouse_pos):
                    return "play"
            else:
                text_surface_game = FONT_MAIN_MENU.render(list_button[0], True, WHITE)

            if text_rect_exit.collidepoint(mouse_pos):  # Проверяем, попала ли мышь в текст
                text_surface_exit = FONT_MAIN_MENU.render(list_button[1], True, RED)
                if mouse_buttons[0] and text_rect_exit.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
            else:
                text_surface_exit = FONT_MAIN_MENU.render(list_button[1], True, WHITE)
        pygame.display.flip()


def main_menu(game_state):
    button_new_game = "Начать игру"
    button_exit = "Выход"
    list_button = [button_new_game, button_exit] 
    event = display_pygame_event(list_button,game_state,SCORE)
    return event