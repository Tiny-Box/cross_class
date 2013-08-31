#-*- coding:utf-8
import pygame
from sys import exit
import random

pygame.init()
screen = pygame.display.set_mode((800, 500), 0, 32)
pygame.display.set_caption("Hello, World!")
background = pygame.image.load('backg.jpg').convert()
#要是处理带透明部分 就要用到convert_alpha 而不是convert
plane = pygame.image.load('dude2.png').convert_alpha()

class Bullet():
	def __init__(self):
		self.x = -1
		self.y = 0
		self.image = pygame.image.load('bullet.png').convert_alpha()

	def move(self):
		if self.x > 800:
			mouseX, mouseY = pygame.mouse.get_pos()
			self.x = mouseX - self.image.get_width() / 2
			self.y = mouseY + 10
		else:
			self.x += 5
bullet = Bullet()

class Enemy:
	def __init__(self):
		self.x = 850
		self.y = random.randint(0, 500)
		self.speed = random.randint(1, 2) + 0.1
		self.image = pygame.image.load('badguy.png').convert_alpha()

	def move(self):
		if self.x > 0:
			self.x -= self.speed
		else:
			self.x = 850
enemy = Enemy()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	screen.blit(background, (0, 0))

	x, y = pygame.mouse.get_pos()

	bullet.move()
	screen.blit(bullet.image, (bullet.x, bullet.y))

	enemy.move()
	screen.blit(enemy.image, (enemy.x, enemy,y))

	x -= plane.get_width() / 2
	y -= plane.get_height() / 2

	screen.blit(plane, (x, y))

	pygame.display.update()
