import pygame
import sys

pygame.init()

screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
my_ball = pygame.image.load("beach_ball.png")
x = 50
y = 50
x_speed = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.time.delay(20)
    pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0)
    x += x_speed
    if x > screen.get_width() - 90:
        x_speed = - (x_speed + 10)
    elif x <= 0:
        x_speed = - (x_speed - 10)
    screen.blit(my_ball, [x, y])
    pygame.display.flip()
