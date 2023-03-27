import pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.SysFont("freesansbold.ttf", 18)

#(self, text, x_pos, y_pos, width, height, screen):

class Button:
    def __init__(self, text, x_pos, y_pos, width, height, screen):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.screen = screen
        self.draw()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos),(self.width ,self.height))
        if left_click and button_rect.collidepoint(mouse_pos):
            return True
        else:
            return False


    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        button_text = font.render(self.text, True, "black")
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos),(self.width ,self.height))
        pygame.draw.rect(screen, "gray", button_rect, 0, 5)
        pygame.draw.rect(screen, "black", button_rect, 2, 5)
        if mouse_pos and button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, "gray", button_rect, 0, 5)

        screen.blit(button_text, (self.x_pos + 10, self.y_pos + 10))

def level_1_btn():
	level_1_btn = Button("Level 1", 30, 30, 100, 50, screen)