import pygame
import player
import background
import pauseScreen
import enemy
from amazing import yes

# setup stuff
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Legendary Potato')
pygame.init()

# player stuff
character = player.Player(screen, 10, 3)

idleAnimationCycle = 1
playerShouldChangeIdleAnim = 1
playerIdleAnimSpeed = 10  #5 or 10

testEnemy = enemy.Slime(screen, 2, 9, 0.05)

# moving around stuff
world_x = 0
world_y = 0
bg = background.Background(screen)
bg.CheckScroll(screen)
backgroundName = 'Tiles'

# pause screen stuff
font = pygame.font.Font('Fonts/PotatoFont-Regular.ttf', 75)

resume = pauseScreen.PauseButton('Resume', SCREEN_WIDTH, SCREEN_HEIGHT / 3.5, font)
settings = pauseScreen.PauseButton('Settings', SCREEN_WIDTH, SCREEN_HEIGHT / 2, font)
quit = pauseScreen.PauseButton('Quit', SCREEN_WIDTH, SCREEN_HEIGHT / 1.4, font)
buttons = pauseScreen.Group(resume, settings, quit)
buttons.add(resume, settings, quit)

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
        character.scrollX(world_x, screen, bg, testEnemy)
        character.scrollY(world_y, screen, bg, testEnemy)

        bgImage = pygame.transform.scale_by(pygame.image.load('Images/Decoration/Background/' + backgroundName + ".png"), 15)
        bg.ShowBackground(screen)

        testEnemy.move(character)
        screen.blit(testEnemy.image, testEnemy.rect)

        character.move(keys)
        screen.blit(character.image, character.rect)
        
    elif state == 'Paused':
        image = pygame.image.load('Images/UI/Buttons/Pause Button/Unclicked.png')
        screen.blit(pygame.transform.scale(pygame.image.load('Images/UI/Menus/Pause.png'), (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))
        
        buttons.blit(screen)
        buttons.checkForClick(pygame.event.get())

        if keys[pygame.K_SPACE] and keys[pygame.K_r]:
            yes()
    pygame.display.flip()
    pygame.time.Clock().tick(60) / 1000
pygame.quit()