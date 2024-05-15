import pygame
from menu import *


scene = "menu"
pygame.display.set_caption(scene)

w = 800
h = 600

screen = pygame.display.set_mode((w, h))

pb = Button(400, 300, 100, 50, "Play")
lb = Button(400, 400, 100, 50, "License")
while True:
    if scene == "menu":
        screen.fill("BLACK")
        pb.draw(screen)
        lb.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.update()