#-*- coding:utf-8
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 500), 0, 32)
pygame.display.set_caption("Hello, World!")
background = pygame.image.load('backg.jpg').convert()
#要是处理带透明部分 就要用到convert_alpha 而不是convert
plane = pygame.image.load('dude2.png').convert_alpha()
arrow = pygame.image.load('bullet.png').convert_alpha()

arrow_x = -1
arrow_y = 0

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	screen.blit(background, (0, 0))

	x, y = pygame.mouse.get_pos()

	if arrow_x > 800:
		arrow_x = x + arrow.get_width() / 2
		arrow_y = y + arrow.get_height() / 2
	else:
		arrow_x += 5

	screen.blit(arrow, (arrow_x, arrow_y))

	x -= plane.get_width() / 2
	y -= plane.get_height() / 2

	screen.blit(plane, (x, y))

	pygame.display.update()
