import pygame
import player

SCREEN_WIDTH = 340
SCREEN_HEIGHT = 560
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.init()

character = player.Player()
animationCycle = 1
playerShouldChangeAnim = 1
playerAnimSpeed = 10


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('white')

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d]:
        if playerShouldChangeAnim >= playerAnimSpeed:
            animationCycle += 1
            if animationCycle >= 3:
                animationCycle = 1
            playerShouldChangeAnim = 1
        else: 
            playerShouldChangeAnim += 1
    else:
        animationCycle = 1

    playerDirection = character.playerDirection
    character.move(keys, character.playerDirection, animationCycle)
    screen.blit(character.image, (character.rect.x, character.rect.y))

    pygame.display.flip()
    pygame.time.Clock().tick(60) / 1000
pygame.quit()