import math
import pygame
from pygame.locals import *
from src.classes import *

speed = 3
speed_ball = speed
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen_size = (800, 640)
ai = 1

pygame.init()
screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
pygame.display.set_caption("Pong")

ball = Ball(20)
ball.set_pos((screen_size[0] - ball.width) / 2, 
    (screen_size[1] - ball.width) / 2)

player_paddle = Paddle(20, 100, screen_size)
player_paddle.set_pos(60, (screen_size[1] - player_paddle.height) / 2)

enemy_paddle = Paddle(20, 100, screen_size)
enemy_paddle.set_pos(screen_size[0] - 80, player_paddle.rect.y)

sprites = pygame.sprite.Group()
sprites.add(player_paddle)
sprites.add(enemy_paddle)
sprites.add(ball)

rectangles = [player_paddle, enemy_paddle, ball]

is_running = True
clock = pygame.time.Clock()

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_paddle.set_pos_p(player_paddle.rect.y - speed)
    elif keys[pygame.K_s]:
        player_paddle.set_pos_p(player_paddle.rect.y + speed)

    if keys[pygame.K_m]:
        ai *= -1

    if ai > 0:
        enemy_paddle.ai(ball, speed)
    else:
        if keys[pygame.K_UP]:
            enemy_paddle.set_pos_p(enemy_paddle.rect.y - speed)
        elif keys[pygame.K_DOWN]:
            enemy_paddle.set_pos_p(enemy_paddle.rect.y + speed)


    ball.move_ball(rectangles, speed - 1)

    if screen_size != screen.get_size():
        screen_size = screen.get_size()
        for i in sprites:
            i.get_screen(screen_size)
            i.scale()
            speed = round(2 + screen_size[0] / 640)
            if speed <= 0:
                speed = 5
        enemy_paddle.set_pos(screen_size[0] - 80, enemy_paddle.rect.y)

    sprites.update()

    screen.fill(BLACK)

    sprites.draw(screen)

    pygame.display.flip()

    clock.tick(350)
 
pygame.quit()
