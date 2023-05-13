import pygame #imports the pygame library to the program
from sys import exit #imports the exit function from the system
from levels import * #imports all for the file "levels.py"
from game_elements import * #imports all for the file "game_elements.py"

pygame.font.init()
font = pygame.font.SysFont("freesansbold.ttf", 18)

pygame.init
window_icon = pygame.image.load("blood-cells.png")
pygame.display.set_icon(window_icon)

# establishing a surface for the game to be displayed on
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# naming the surface
pygame.display.set_caption("Grimcell")

# creating a clock to base frame rate off of
FPS = 60
clock = pygame.time.Clock()

class Terrain:
    def __init__(self, x_pos, y_pos, width, height, colour):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.display = True
        self.colour = colour

    def draw(self):
        pygame.draw.rect(screen, self.colour)

        screen.blit(self.x_pos, self.y_pos)

'''
    buttons created
'''
level_select_btn = Button("Level Select", 350, 80, 100, 30, screen)
level_create_btn = Button("Level Create", 350, 130, 100, 30, screen)
endless_btn = Button("Endless", 350, 180, 100, 30, screen)
level_1_btn = Button("Level 1", 350, 130, 100, 50, screen)
# this button will only appear if level_select_btn is clicked
level_1_btn.display = False

'''
    floor and player
    player will collide with the floor
    look at player.update() method in player.py
'''
floor = pygame.Rect(0, SCREEN_HEIGHT*0.66, SCREEN_WIDTH, SCREEN_HEIGHT/2)
player = Player(floor.x, floor.y)
mouse = pygame.mouse.get_pos()

lvl_1_block1 = Terrain(300, 100, 100, 10, "White")

def level_select():
    PLAY_MOUSE_POS = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()


def main_menu():
    screen.fill('grey')

    if level_select_btn.display:
        level_select_btn.draw()
    if level_create_btn.display:
        level_create_btn.draw()
    if endless_btn.display:
        endless_btn.draw()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if level_select_btn.check_click():
                '''
                    all buttons dissapear and the level_1_btn shows
                '''
                level_select_btn.display = False
                level_create_btn.display = False
                endless_btn.display = False
                level_1_btn.display = True

    if level_1_btn.display:
        level_1_btn.draw()

    if level_1_btn.check_click():
        level_1_btn.display = False 
    
    '''
        draw the player and the floor
        update the player
    '''
    if not level_1_btn.display and not level_select_btn.display:
        pygame.draw.rect(screen, 'brown', floor)
        player.update(floor)
        player.draw(screen)
        lvl_1_block1.draw
    pygame.display.update()


# main menu
while True:
    # This is to cap the frame rate of the game and stop any issues that would occur through high frame rates
    clock.tick(FPS)
    main_menu()
    pygame.display.update()