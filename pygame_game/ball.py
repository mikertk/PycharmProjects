import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode([1080, 720])
screen.fill([200, 100, 150])
my_ball = pygame.image.load("beach_ball.png")
x = random.randint(0, 990)
y = random.randint(0, 630)
x_speed = 5
y_speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.time.delay(20)
    pygame.draw.rect(screen, [200, 100, 150], [x, y, 90, 90], 0)
    x += x_speed
    y += y_speed
    if x >= screen.get_width() - 90:
        x_speed = - (x_speed + 5)
    elif x <= 0:
        x_speed = - (x_speed - 5)
    if y >= screen.get_height() - 90:
        y_speed = - (y_speed + 5)
    elif y <= 0:
        y_speed = - (y_speed - 5)
    if x_speed >= 320:
        x_speed = 300
    elif x_speed <= -320:
        x_speed = -300
    if y_speed >= 240:
        y_speed = 200
    elif y_speed <= -240:
        y_speed = -200

    screen.blit(my_ball, [x, y])
    pygame.display.flip()
