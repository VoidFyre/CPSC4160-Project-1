import pygame
import random

class Ball(pygame.sprite.Sprite):
	def __init__(self, color=(255,255,255), width=20, height=20):
		super().__init__()

		self.image = pygame.image.load("./resources/pumpkin.png").convert_alpha()

		# resize the image
		self.image = pygame.transform.scale(self.image, (width, height))

		self.rect = self.image.get_rect()

		self.velocity = [random.randint(4, 8), random.randint(-8, 8)]

		# set initial position randomly within a range of values for x and y
		self.rect.x = 50
		self.rect.y = 200

	def reset_(self, x=50, y=200):
		# set initial position randomly within a range of values for x and y
		self.rect.x = x
		self.rect.y = y
		self.velocity = [random.randint(4, 8), random.randint(-8, 8)]

	def update(self):
		self.rect.x += self.velocity[0]
		self.rect.y += self.velocity[1]

	def bounce(self):
		self.velocity[0] = -self.velocity[0]
		self.velocity[1] = random.randint(-8, 8)