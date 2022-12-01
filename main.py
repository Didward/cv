# Square That Can Be Controlled By Arrow Keys on Keyboard

import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Square That Can Be Controlled By Arrow Keys on Keyboard")

square = pygame.Rect(300, 200, 50, 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                square.x -= 10
            if event.key == pygame.K_RIGHT:
                square.x += 10
            if event.key == pygame.K_UP:
                square.y -= 10
            if event.key == pygame.K_DOWN:
                square.y += 10

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), square)
    pygame.display.update()
    