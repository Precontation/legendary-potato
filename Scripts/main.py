import pygame
import player
import background
from amazing import yes

# setup stuff
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Legendary Potato')
pygame.init()

# player stuff
character = player.Player()
moveAnimationCycle = 1
playerShouldChangeMoveAnim = 1
playerMoveAnimSpeed = 10

idleAnimationCycle = 1
playerShouldChangeIdleAnim = 1
playerIdleAnimSpeed = 10  #5 or 10

# moving around stuff
world_x = 0
world_y = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    world_x = character.scrollX(world_x, screen)
    world_y = character.scrollY(world_y, screen)

    background.updateStuff(screen, world_x, world_y)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and keys[pygame.K_r]:
        yes()

    if character.checkIfMoving(keys):
        playerShouldChangeIdleAnim = 1
        idleAnimationCycle = 1
        if playerShouldChangeMoveAnim >= playerMoveAnimSpeed:
            moveAnimationCycle += 1
            if moveAnimationCycle >= 3:
                moveAnimationCycle = 1
            playerShouldChangeMoveAnim = 1
        else: 
            playerShouldChangeMoveAnim += 1
    else:
        playerShouldChangeMoveAnim = 1
        moveAnimationCycle = 1

        if playerShouldChangeIdleAnim >= playerIdleAnimSpeed:
            idleAnimationCycle += 1
            if idleAnimationCycle >= 3:
                idleAnimationCycle = 1
            playerShouldChangeIdleAnim = 1
        else: 
            playerShouldChangeIdleAnim += 1

    playerDirection = character.playerDirection
    character.move(keys, character.playerDirection, moveAnimationCycle, idleAnimationCycle)
    screen.blit(character.image, (character.rect.x, character.rect.y))

    pygame.display.flip()
    pygame.time.Clock().tick(60) / 1000
pygame.quit()