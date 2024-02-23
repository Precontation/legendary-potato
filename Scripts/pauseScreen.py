import pygame
from pygame.sprite import Group

class PauseButton(pygame.sprite.Sprite):
    def __init__(self, button, SCREEN_WIDTH, yPosition, font) -> None:
        super().__init__()

        self.buttonPath = 'Images/UI/Buttons/Pause Button/'
        self.button = button
        self.image = pygame.transform.scale(pygame.image.load(self.buttonPath + 'Unclicked.png'), (190, 100))
        self.rect = self.image.get_rect()
        self.clicked = False
        self.rect.x = (SCREEN_WIDTH - self.rect.width) / 2
        self.rect.y = yPosition
        
        self.buttonPressed = False

        if button == 'Resume':
            self.text = font.render('Resume', True, 'black', None)
        elif button == 'Settings':
            self.text = font.render('Settings', True, 'black', None)
        elif button == 'Quit':
            self.text = font.render('Quit', True, 'black', None)

    def blit(self, screen):
        if self.clicked:
            self.image = pygame.transform.scale(pygame.image.load(self.buttonPath + 'Clicked.png'), (190, 100))
        else:
            self.image = pygame.transform.scale(pygame.image.load(self.buttonPath + 'Unclicked.png'), (190, 100))
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.rect)
    
    def checkForClick(self, events):
        self.buttonPressed = False
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    print('Clicked')
                    self.clicked = True
                    self.buttonPressed = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.clicked = False
                if self.buttonPressed:
                    print(self.button)

class Group(pygame.sprite.Group):
    def blit(self, screen):
        # Do something to all the sprites in the group
        for sprite in self.sprites():
            sprite.blit(screen)
    def checkForClick(self, events):
        # Do something to all the sprites in the group
        for sprite in self.sprites():
            sprite.checkForClick(events)