import pygame
from sys import exit
pygame.font.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
font = pygame.font.SysFont("freesansbold.ttf", 18)

pygame.init
window_icon = pygame.image.load("blood-cells.png")
pygame.display.set_icon(window_icon)

mainMenu = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# establishing a surface for the game to be displayed on

pygame.display.set_caption("Grimcell")
# naming the surface

FPS = 60
clock = pygame.time.Clock()
# creating a clock to base frame rate off of

mouse = pygame.mouse.get_pos()

class Button:
    def __init__(self, text, x_pos, y_pos, width, height, screen):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.screen = screen
        self.draw()

    def draw(self):
        button_text = font.render(self.text, True, "black")
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos),(self.width ,self.height))
        pygame.draw.rect(self.screen, "gray", button_rect, 0, 5)
        pygame.draw.rect(self.screen, "black", button_rect, 2, 5)
        mainMenu.blit(button_text, (self.x_pos + 10, self.y_pos + 10))

while True:
    mainMenu.fill("white")
    clock.tick(FPS)
    level_select_btn = Button("Level Select", 350, 100, 100, 30, mainMenu)
    level_create_btn = Button("Level Create", 350, 150, 100, 30, mainMenu)
    endless_btn = Button("Endless", 350, 200, 100, 30, mainMenu)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.flip()
    pygame.display.update()
   
    # This is to cap the frame rate of the game and stop any issues that would occur through high frame rates
