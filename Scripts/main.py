import pygame
import player
import background
import pauseScreen
import enemyManager
from amazing import yes

# setup stuff
pygame.init()
pygame.display.set_caption('Legendary Potato')
pygame.display.set_icon(pygame.image.load('Images/UI/Logo.png'))
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# player stuff
character = player.Player(screen, 10, 3, 100000)

idleAnimationCycle = 1
playerShouldChangeIdleAnim = 1
playerIdleAnimSpeed = 10  #5 or 10

manager = enemyManager.EnemyManager(screen, 5, 100000)

# moving around stuff
world_x = 0
world_y = 0
bg = background.Background(screen)
bg.CheckScroll(screen)
backgroundName = 'Tiles'

# pause screen stuff
font = pygame.font.Font('Fonts/PotatoFont-Regular.otf', 75)

resume = pauseScreen.PauseButton('Running', 'Resume', SCREEN_WIDTH, SCREEN_HEIGHT / 3.5, font)
settings = pauseScreen.PauseButton('Settings', 'Settings', SCREEN_WIDTH, SCREEN_HEIGHT / 2, font)
quit = pauseScreen.PauseButton('Quit', 'Quit', SCREEN_WIDTH, SCREEN_HEIGHT / 1.4, font)
buttons = pauseScreen.Group(resume, settings, quit)

running = True
state = 'Running'

while running:
    keys = pygame.key.get_pressed()
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                if state == 'Running':
                    state = 'Paused'
                elif state == 'Paused':
                    state = 'Running'

    if state == 'Running':
        world_x = character.scrollX(world_x, screen, bg, manager)
        world_y = character.scrollY(world_y, screen, bg, manager)

        bgImage = pygame.transform.scale_by(pygame.image.load('Images/Decoration/Background/' + backgroundName + '.png'), 15)
        bg.ShowBackground(screen)
    
        character.attack(keys, manager)
        character.move(keys, screen, manager)
        manager.move(character)
        manager.blit(screen)
        manager.spawnEnemies(screen)
        character.health -= manager.checkIfHit(character)
        if character.health < 0: character.health = 0
        screen.blit(font.render('Health: ' + str(round(character.health)), 1, 'black', None), (25, SCREEN_HEIGHT / 1.3)) # temporary
        screen.blit(font.render('Kills: ' + str(round(character.kills)), 1, 'black', None), (25, 10)) # temporary
        if character.health <= 0:
            state = 'Quit' # temporary


        screen.blit(character.image, character.rect)
        
    elif state == 'Paused':
        image = pygame.transform.scale(pygame.image.load('Images/UI/Menus/Pause.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(image, (0, 0))
 
        state = buttons.checkForClicks(events, state)
        buttons.blit(screen)

        if keys[pygame.K_SPACE] and keys[pygame.K_r]:
            yes()
    elif state == 'Settings':
        state = 'Paused' # temporary
    elif state == 'Quit':
        running = False
        
    pygame.display.flip()
    pygame.time.Clock().tick(60) / 1000
pygame.quit()