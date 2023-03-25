import pygame
from sys import exit

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

pygame.init
window_icon = pygame.image.load("blood-cells.png")
pygame.display.set_icon(window_icon)

mainMenu = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# establishing a surface for the game to be displayed on

pygame.display.set_caption("Grimcell")
# naming the surface

clock = pygame.time.Clock()
# creating a clock to base frame rate off of

test_surface = pygame.Surface((100,200))
test_surface.fill("gold4")

mouse = pygame.mouse.get_pos()

pygame.draw.rect(mainMenu, "black", [590, 315, 80 , 30])

selectImg = pygame.load()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    mainMenu.blit(test_surface,(0,0))

    pygame.display.update()
    clock.tick(60)
    # This is to cap the frame rate of the game and stop any issues that would occur through high frame rates
