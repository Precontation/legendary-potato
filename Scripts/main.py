import pygame
import player
import scroll
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
bg = background.Background(screen)
bg.CheckScroll(screen)
backgroundName = 'Tiles'

running = True
state = 'Running'

while running:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                if state == 'Running':
                    state = 'Paused'
                elif state == 'Paused':
                    state = 'Running'

    if state == 'Running':
        character.scrollX(world_x, screen, bg)
        character.scrollY(world_y, screen, bg)

        bgImage = pygame.transform.scale_by(pygame.image.load('Images/Decoration/Background/' + backgroundName + ".png"), 15)
        bg.ShowBackground(screen)

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

        character.move(keys, character.playerDirection, moveAnimationCycle, idleAnimationCycle)
        screen.blit(character.image, (character.rect.x, character.rect.y))
    elif state == 'Paused':
        screen.blit(pygame.transform.scale(pygame.image.load('Images/UI/Menus/Pause.png'), (SCREEN_WIDTH, SCREEN_HEIGHT)))
        
        if keys[pygame.K_SPACE] and keys[pygame.K_r]:
            yes()
        
    pygame.display.flip()
    pygame.time.Clock().tick(60) / 1000
pygame.quit()