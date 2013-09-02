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
		self.active = False

	def move(self):
		if self.active:
			self.x += 5
		if self.x > 800:
			self.active = False

	def restart(self):
		mouseX, mouseY = pygame.mouse.get_pos()
		self.x = mouseX - self.image.get_width() / 2
		self.y = mouseY - 10

		self.active = True
		

class Enemy:
	def __init__(self):
		self.x = 850
		self.y = random.randint(0, 500)
		self.speed = random.randint(1, 2) + 0.1
		self.image = pygame.image.load('badguy.png').convert_alpha()
		self.restart()

	def move(self):
		if self.x > 0:
			self.x -= self.speed
		else:
			self.x = 850
			self.restart()

	def restart(self):
		self.x = 850
		self.y = random.randint(0, 500)

#添加多个子弹
bullets = []
for i in range(5):
	bullets.append(Bullet())

#统计子弹总数
count_b = len(bullets)
#激活的子弹序号
index_b = 0
#发射间隔
interval_b = 0

enemy = Enemy()

while True:
	interval_b -= 1

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	screen.blit(background, (0, 0))

	x, y = pygame.mouse.get_pos()

	if interval_b < 0:
		bullets[index_b].restart()
		#重置间隔时间
		interval_b = 100
		#子弹序号周期性递增
		index_b = (index_b + 1) % count_b

		for b in bullets:
			if b.active:
				b.move()
				screen.blit(b.image, (b.x, b.y))

	enemy.move()
	screen.blit(enemy.image, (enemy.x, enemy.y))

	x -= plane.get_width() / 2
	y -= plane.get_height() / 2

	screen.blit(plane, (x, y))

	pygame.display.update()
