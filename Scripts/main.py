import pygame
import player

SCREEN_WIDTH = 340
SCREEN_HEIGHT = 560
screen = pygame.display.get_active()

pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.init()

character = player.Player()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # screen.blit(character.image, (character.rect.x, character.rect.y))
pygame.quit()