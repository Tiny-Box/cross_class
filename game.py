import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((510, 510), 0, 32)
pygame.display.set_caption("Hello, World!")
background = pygame.image.load('bg.jpg').convert()
background2 = pygame.image.load('bg2.jpg').convert()
flag = True

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			flag = not flag
	if flag:
		screen.blit(background, (0,0))
		pygame.display.update()
	else:
		screen.blit(background2, (0,0))
		pygame.display.update()
