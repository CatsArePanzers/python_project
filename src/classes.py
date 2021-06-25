import pygame
import math
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Rectangle(pygame.sprite.Sprite):
    def __init__(self, width, height, screen = (800, 640), colour = WHITE):
        self.width = width
        self.height = height
        self.screen = screen
        self.colour = colour

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

    def scale(self):
        self.height = self.rect.height * self.screen[1] / 600
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLACK)

        pygame.draw.rect(self.image, self.colour, [0, 0, self.width, self.height])

    def are_colliding(self, other):
        if other.rect.x <= self.rect.x + self.width:
            if self.rect.x <= other.rect.x + other.width:
                if other.rect.y <= self.rect.y + self.width:
                    if self.rect.y <= other.rect.y + other.height:
                        return True
                        

class Paddle(Rectangle):
    def set_pos_p(self, y):
        self.set_pos(self.rect.x, y)
        if y <= 0:
            self.set_pos(self.rect.x, 0)
        elif y >= self.screen[1] - self.height:
            self.set_pos(self.rect.x, self.screen[1] - self.height)

    def ai(self, other, speed):
        self.rect.y += (other.rect.y - self.rect.y) * self.screen[1] / 640
        if self.rect.y >= self.screen[1] - self.height:
            self.set_pos(self.rect.x, self.screen[1] - self.height)
            
class Ball(Rectangle):
    def __init__(self, width):
        self.direction_x = 1
        self.direction_y = 1
        self.angle = 100
        super().__init__(width, width)

    def scale(self): 
        self.width = self.height = self.rect.height * float(self.screen[1] / 640)
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLACK)

        pygame.draw.rect(self.image, self.colour, [0, 0, self.width, self.height])

    def bounce(self, other, speed):
        if self.are_colliding(other):
            self.angle = math.fabs(round((other.rect.y + other.width / 2 - 
                                         self.rect.y + self.height / 2) / 15))
            if self.direction_x > 0:
                self.rect.x = other.rect.x - self.width
                self.angle = round(random.random() * 4)
            else:
                self.rect.x = other.rect.x + other.width + 1
                self.angle = round(random.random() * 4)
            self.direction_x *= -1
            self.direction_y *= -1
        elif self.rect.y + self.width >= self.screen[1]:
            self.direction_y = -1
            self.rect.y -= 20
            self.angle = random.random() * 4
        elif self.rect.y <= 0:
            self.rect.y = 0
            self.direction_y = 1
            self.angle = random.random() * 4

    def move_ball(self, other, speed):
        self.bounce(other[0], speed)
        self.bounce(other[1], speed)
        self.set_pos(self.rect.x + (speed) * self.direction_x,
                     self.rect.y + (speed - self.angle) * self.direction_y)
        if self.rect.x <= 0:
            self.set_pos(self.screen[0] / 2, self.screen[1] / 2)
            self.direction_x *= -1
        elif self.rect.x >= self.screen[0] - self.width:
            self.set_pos(self.screen[0] / 2, self.screen[1] / 2)
            self.direction_x *= -1

        
