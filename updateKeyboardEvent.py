import pygame
import sys

pygame.init()
screen = pygame.display.set_mode([640, 480])
print screen.get_size()
background = pygame.Surface(screen.get_size())
background.fill([200, 200, 240])
clock = pygame.time.Clock()


class Ball(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        if self.rect.left <= screen.get_rect().left or \
                self.rect.right >= screen.get_rect().right:
            self.speed[0] = -self.speed[0]
        newPos = self.rect.move(self.speed)
        self.rect = newPos


my_ball = Ball('beach_ball.png', [10, 0], [20, 20])
pygame.time.set_timer(pygame.USEREVENT, 10)
direction = 1
print my_ball.rect.centery
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.USEREVENT:
            my_ball.rect.centery += 30 * direction
            if my_ball.rect.top <= 0 or my_ball.rect.bottom >= screen.get_rect().bottom:
                direction = -direction

    clock.tick(30)
    screen.blit(background, (0, 0))
    my_ball.move()
    screen.blit(my_ball.image, my_ball.rect)
    pygame.display.flip()
