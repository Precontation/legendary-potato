import pygame
import player
import background
import pauseScreen
import enemyManager
from amazing import yes

# setup stuff
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Legendary Potato')
pygame.init()

# player stuff
character = player.Player(screen, 10, 3, 100)

idleAnimationCycle = 1
playerShouldChangeIdleAnim = 1
playerIdleAnimSpeed = 10  #5 or 10

manager = enemyManager.EnemyManager(screen, 4)

# moving around stuff
world_x = 0
world_y = 0
bg = background.Background(screen)
bg.CheckScroll(screen)
backgroundName = 'Tiles'

# pause screen stuff
font = pygame.font.Font('Fonts/PotatoFont-Regular.otf', 75)

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
        character.scrollX(world_x, screen, bg, manager)
        character.scrollY(world_y, screen, bg, manager)

        bgImage = pygame.transform.scale_by(pygame.image.load('Images/Decoration/Background/' + backgroundName + ".png"), 15)
        bg.ShowBackground(screen)

        character.move(keys)
        manager.move(character)
        manager.blit(screen)
        character.health -= manager.checkIfHit(character)
        screen.blit(font.render("Health: " + str(round(character.health)), 1, 'black', None), (25, SCREEN_HEIGHT / 1.3)) # temporary
        if character.health <= 0:
            state = "QUIT" # temporary


        screen.blit(character.image, character.rect)
        
    elif state == 'Paused':
        image = pygame.image.load('Images/UI/Buttons/Pause Button/Unclicked.png')
        screen.blit(pygame.transform.scale(pygame.image.load('Images/UI/Menus/Pause.png'), (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))
        
        for event in pygame.event.get(pygame.MOUSEBUTTONDOWN):
            if event.type == pygame.MOUSEBUTTONDOWN:
                buttons.checkForClicks(event, state)
        
        buttons.blit(screen)

        if keys[pygame.K_SPACE] and keys[pygame.K_r]:
            yes()
    elif state == 'QUIT':
        running = False
    
    pygame.display.flip()
    pygame.time.Clock().tick(60) / 1000
pygame.quit()