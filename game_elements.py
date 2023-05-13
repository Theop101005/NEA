import pygame


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

'''
    Various game elements will be placed here
    Below is the player class
'''

class Player(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.image = pygame.image.load('Idle.png')  #player image
        self.image = self.image.subsurface(pygame.Rect(50, 60, 50, 40)) #use subsurface of the player image
        self.rect = self.image.get_rect(topleft=(x, y)) #create a rect for the player based on image
        self.flip = False   #controls when to flip player image 
        self.in_air = False #contrils player jumping
        #some variables for player movement. direction is for x and y directions
        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.gravity = 1
        self.jump_height = -16
        self.on_ground = True

    def movement(self):
        keys = pygame.key.get_pressed() #get the key pressed

        #jump
        if keys[pygame.K_SPACE] and not self.in_air:
            self.direction.y = self.jump_height
            self.in_air = True
            self.on_ground = False
        #move left
        if keys[pygame.K_a] and self.rect.x > 0:
            self.direction.x = -1
        #move right
        elif keys[pygame.K_d] and self.rect.x < SCREEN_WIDTH - self.image.get_width():
            self.direction.x = 1
        else:
            self.direction.x = 0

    #gravity on player acts on it' y direction
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

        if self.on_ground:
            self.in_air = False

    '''
        moving horizontally
        added functionality for if the player jumps onto higher platform
        or runs into wall present in vertical_movement and horizontal_movement
    '''
    def vertical_movement(self, floor: pygame.Rect):
        self.apply_gravity()
        if floor.colliderect(self.rect):
            if self.direction.y < 0:
                self.rect.top = floor.bottom
                self.direction.y = 0
            if self.direction.y > 0:
                self.rect.bottom = floor.top
                self.direction.y = 0
                self.on_ground = True

    def horizontal_movement(self, floor: pygame.Rect):
        self.rect.x += self.speed * self.direction.x
        if floor.colliderect(self.rect):
            if self.direction.x < 0:
                self.rect.left = floor.right
            if self.direction.x > 0:
                self.rect.right = floor.left

    def draw(self, screen: pygame.Surface):
        #draw and flip the player
        screen.blit(pygame.transform.flip(
            self.image, self.flip, False), self.rect)

    def update(self, floor: pygame.Rect):
        #flip the image based on direction
        if self.direction.x < 0:
            self.flip = True
        elif self.direction.x > 0:
            self.flip = False

        #movement methods
        self.vertical_movement(floor)
        self.horizontal_movement(floor)
        self.movement()
