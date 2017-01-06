import pygame
import sys

pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([200, 100, 150])
my_ball = pygame.image.load("beach_ball.png")
x = 50
y = 50
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
    if x >= screen.get_width() - 90 or x <= 0:
        x_speed = -x_speed
    if y >= screen.get_height() - 90 or y <= 0:
        y_speed = -y_speed
    screen.blit(my_ball, [x, y])
    pygame.display.flip()
