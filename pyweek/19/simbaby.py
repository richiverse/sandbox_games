"""Baby simulator for pyweek #19: 'One Room'."""
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 768))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.ket == pygame.K_ESCAPE:
            running = False
