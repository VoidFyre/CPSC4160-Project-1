import pygame
from random import randint


p1Color = (255,255,255)
p1Size = p1W, p1H = 10, 150
p1Pos = p1X, p1Y = 10, 0

player1 = pygame.Rect(p1X, p1Y, p1W, p1H)

p2Color = (255,255,255)
p2Size = p2W, p2H = 10, 150
p2Pos = p2X, p2Y = 780, 0

player2 = pygame.Rect(p2X, p2Y, p2W, p2H)




class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.image.set_colorkey(color)

        self.ballVelocity = [randint(4,8), randint(-8,8)]

        self.rect = self.image.get_rect()

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        def updateBall(self):
            self.rect.x += self.ballVelocity[0]
            self.rect.y += self.ballVelocity[1]
        def bounceBall(self):
            self.rect.x += -self.ballVelocity[0]
            self.rect.y += randint(-8,8)