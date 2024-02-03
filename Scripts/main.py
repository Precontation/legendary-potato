import pygame
import player
import background
from amazing import yes

# setup stuff
SCREEN_WIDTH = 340
SCREEN_HEIGHT = 560
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.init()

# player stuff
character = player.Player()
animationCycle = 1
playerShouldChangeAnim = 1
playerAnimSpeed = 10

# moving around stuff
world_x = 1
world_y = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    background.updateStuff(screen, world_x, world_y)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE and pygame.K_r]:
        yes()
    if keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_a] or keys[pygame.K_LEFT] or keys[pygame.K_s] or keys[pygame.K_DOWN] or keys[pygame.K_d] or keys[pygame.K_RIGHT]:
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