import pygame
from pygame.locals import *
from src.classes import *

SPEED = 1
SPEED_BALL = SPEED
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen_size = (800, 640)

pygame.init()
screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
pygame.display.set_caption("Pong")

ball = Ball(20)
ball.set_pos((screen_size[0] - ball.width) / 2, 
    (screen_size[1] - ball.width) / 2)

player_paddle = Paddle(20, 100, screen_size)
player_paddle.set_pos(ball.width, (screen_size[1] - player_paddle.height) / 2)

enemy_paddle = Paddle(20, 100, screen_size)
enemy_paddle.set_pos(screen_size[0] - ball.width * 2, player_paddle.rect.y)

sprites = pygame.sprite.Group()
sprites.add(player_paddle)
sprites.add(enemy_paddle)
sprites.add(ball)

list = []
list.append(player_paddle)
list.append(enemy_paddle)
list.append(ball)

#dneska ke se pravim na jasho

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
 
    # --- Game logic should go here
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_paddle.set_pos_p(player_paddle.rect.y - SPEED)
    elif keys[pygame.K_s]:
        player_paddle.set_pos_p(player_paddle.rect.y + SPEED)

    # --- Drawing code should go here
    sprites.update()

    # First, clear the screen to black.
    if screen_size != screen.get_size():
        screen_size = screen.get_size()
        for i in list:
            i.get_screen(screen_size)
        enemy_paddle.set_pos(screen_size[0] - ball.width * 2, screen_size[1] - enemy_paddle.rect.y)


    screen.fill(BLACK)

    sprites.draw(screen)

    pygame.display.flip()
 
pygame.quit()
