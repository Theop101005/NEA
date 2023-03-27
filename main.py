import pygame
from sys import exit
pygame.font.init()
from levels import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
font = pygame.font.SysFont("freesansbold.ttf", 18)

pygame.init
window_icon = pygame.image.load("blood-cells.png")
pygame.display.set_icon(window_icon)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# establishing a surface for the game to be displayed on

pygame.display.set_caption("Grimcell")
# naming the surface

FPS = 60
clock = pygame.time.Clock()
# creating a clock to base frame rate off of

mouse = pygame.mouse.get_pos()

def level_select():
    PLAY_MOUSE_POS = pygame.mouse.get_pos()

    screen.fill("white")
    level_1_btn()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()

def main_menu():
    level_select_btn = Button("Level Select", 350, 100, 100, 30, screen)
    level_create_btn = Button("Level Create", 350, 150, 100, 30, screen)
    endless_btn = Button("Endless", 350, 200, 100, 30, screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if level_select_btn.check_click():
                level_select()
                break
    
    pygame.display.update()

    



    
#main menu
while True:
    clock.tick(FPS)
    main_menu()
    pygame.display.update()
   
    # This is to cap the frame rate of the game and stop any issues that would occur through high frame rates
