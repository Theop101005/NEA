import pygame
from sys import exit

pygame.init()

window_icon = pygame.image.load("blood-cells.png")
pygame.display.set_icon(window_icon)

screen = pygame.display.set_mode((800, 400))
# establishing a surface for the game to be displayed on

pygame.display.set_caption("Grimcell")
# naming the surface

clock = pygame.time.Clock()
# creating a clock to base frame rate off of

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)
    # This is to cap the frame rate of the game and stop any issues that would occur through high frame rates
