import pygame
import player

SCREEN_WIDTH = 340
SCREEN_HEIGHT = 560
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.init()

character = player.Player()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('white')

    playerDirection = character.playerDirection
    character.move(pygame.key.get_pressed(), character.playerDirection)
    character.update(6, character.shouldChangeAnim, character.animationCycle)
    screen.blit(character.image, (character.rect.x, character.rect.y))

    pygame.display.flip()
    pygame.time.Clock().tick(60) / 1000
pygame.quit()