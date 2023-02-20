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


class Paddle:
    def __init__(self, x, y):
        super().__init__()

class Ball(pygame.Rect):
    def __init__(self):
        self.x, self.y = 300, 400
        self.color = (255,255,255)
        self.width, self.height = 10, 10
        self.ballVelocity = [randint(4,8), randint(-8,8)]

    def drawBall(self, surface):
            pygame.draw.rect(surface, self.color, [0, 0, self.width, self.height])

    def updateBall(self):
            self.x += self.ballVelocity[0]
            self.y += self.ballVelocity[1]
    def bounceBall(self):
            self.x += -self.ballVelocity[0]
            self.y += randint(-8,8)