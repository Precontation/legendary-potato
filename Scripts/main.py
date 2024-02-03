import pygame

SCREEN_WIDTH = 340
SCREEN_HEIGHT = 560
screen = pygame.display.get_active()

pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.init()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # test
pygame.quit()