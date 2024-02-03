import pygame
import player

SCREEN_WIDTH = 340
SCREEN_HEIGHT = 560
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.init()

character = player.Player()
animationCycle = 0
shouldChangeAnim = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('black')

    character.move(pygame.key.get_pressed(), character.playerDirection, animationCycle, character.keysPressed)
    screen.blit(character.image, (character.rect.x, character.rect.y))
    pygame.display.flip()
pygame.quit()