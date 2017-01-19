# coding=utf-8


import pygame
import sys
import random


# 定义MyBallClass对象

class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):

        # 初始化pygame.sprite.Sprite对象
        pygame.sprite.Sprite.__init__(self)

        # 初始化各参数
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        # 定义全局变量
        global points, score_text

        self.rect = self.rect.move(self.speed)

        # Ball位于左右边界时反弹
        if self.rect.left <= 0 or self.rect.right >= screen.get_width():
            # 加入反弹随机速度
            self.speed[0] = -self.speed[0] + random.randint(-3, 3)

        # Ball位于顶部边界时反弹，并计分
        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1] + random.randint(-3, 3)
            points += 1
            score_text = font.render(str(points), 1, (0, 0, 0))


# 定义MyPaddleClass对象

class MyPaddleClass(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)

        # Paddle的长和宽
        image_surface = pygame.surface.Surface([100, 20])
        # 黑色填充Paddle
        image_surface.fill([0, 0, 0])
        # 将矩形转换成image
        self.image = image_surface.convert()

        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


pygame.init()
screen = pygame.display.set_mode([640, 480])
clock = pygame.time.Clock()
ball_speed = [10, 5]
myBall = MyBallClass("wackyball.bmp", ball_speed, [50, 50])
ballGroup = pygame.sprite.Group(myBall)
paddle = MyPaddleClass([270, 400])
points = 0
lives = 3

# 创建font实例
font = pygame.font.Font(None, 50)
score_text = font.render(str(points), 1, (50, 50, 50))
textpos = [10, 10]
done = False

while True:
    # 设置帧率
    clock.tick(30)
    # 屏幕颜色
    screen.fill([100, 100, 100])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            # 鼠标移动X坐标事件，paddle移动
            paddle.rect.centerx = event.pos[0]
    # 碰撞检测，Y坐标反向
    if pygame.sprite.spritecollide(paddle, ballGroup, False):
        myBall.speed[1] = -myBall.speed[1] + random.randint(-3, 3)

    # 控制球速
    if 0 < myBall.speed[0] < 3: myBall.speed[0] = 3
    if -3 < myBall.speed[0] <= 0: myBall.speed[0] = -3
    if myBall.speed[0] > 15:  myBall.speed[0] = 15
    if 0 < myBall.speed[1] < 3: myBall.speed[1] = 3
    if -3 < myBall.speed[1] <= 0: myBall.speed[1] = -3
    if myBall.speed[1] > 15:  myBall.speed[1] = 15

    # 移动球
    myBall.move()

    # 完全重绘myBall、paddle、lives
    if not done:
        screen.blit(myBall.image, myBall.rect)
        screen.blit(paddle.image, paddle.rect)
        screen.blit(score_text, textpos)
        # lives以循环的方式依次排列显示在[width - 40 * i, 20]这个位置上
        for i in range(lives):
            width = screen.get_width()
            screen.blit(myBall.image, [width - 40 * i, 20])
        pygame.display.flip()

    # 球掉出页面底部，则减命1条
    if myBall.rect.top >= screen.get_rect().bottom:
        lives -= 1

        # lives为0时，屏幕展示结果，并结束循环，done = True。
        if lives == 0:
            final_text1 = "GAME OVER!"
            final_text2 = "Your final score is: " + str(points)
            ft1_font = pygame.font.Font(None, 70)
            ft1_surf = font.render(final_text1, 1, (50, 50, 50))
            ft2_font = pygame.font.Font(None, 50)
            ft2_surf = font.render(final_text2, 1, (50, 50, 50))
            screen.blit(ft1_surf, [screen.get_width() / 2 - ft1_surf.get_width() / 2, 100])
            screen.blit(ft2_surf, [screen.get_width() / 2 - ft2_surf.get_width() / 2, 200])
            pygame.display.flip()
            done = True
        else:
            pygame.time.delay(2000)
            myBall.rect.topleft = [50, 50]
