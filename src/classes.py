import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Rectangle(pygame.sprite.Sprite):
    def __init__(self, width, height, screen = (800, 640), colour = WHITE):
        self.width = width
        self.height = height
        self.screen = screen

        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, colour, [0, 0, width, height])

        self.rect = self.image.get_rect()

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def get_screen(self, sizes):
        self.screen = sizes

class Paddle(Rectangle):
    def set_pos_p(self, y):
        self.set_pos(self.rect.x, y)
        if y <= 0:
            self.set_pos(self.rect.x, 0)
        elif y >= self.screen[1] - self.height:
            self.set_pos(self.rect.x, self.screen[1] - self.height)
            
class Ball(Rectangle):
    def __init__(self, width):
        super().__init__(width, width)

