# coding = utf-8
import pygame
import sys
from math import pi
from pygame.color import THECOLORS
import random

reload(sys)
sys.setdefaultencoding("utf-8")

pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
color = THECOLORS[random.choice(THECOLORS.keys())]

pygame.draw.ellipse(screen, color, [225, 10, 50, 20], 2)
pygame.draw.ellipse(screen, color, [300, 10, 50, 20])
pygame.draw.polygon(screen, color, [[100, 100], [0, 200], [200, 200]], 5)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
