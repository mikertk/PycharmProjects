# coding=utf-8
import pygame
import sys


pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode([640, 480])
# 给出mixer加载音乐时间。
pygame.time.delay(1000)

splat = pygame.mixer.Sound("splat.wav")
splat.play()

pygame.mixer.music.load("周杰伦 - 床边故事.flac")
pygame.mixer.music.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
