import pygame
import sys


pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode([640, 480])
# pygame.time.delay(1000)

splat = pygame.mixer.Sound("splat.wav")
splat.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
