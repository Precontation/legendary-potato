import pygame
from pygame.sprite import Group

class PauseButton(pygame.sprite.Sprite):
    def __init__(self, button, text, SCREEN_WIDTH, yPosition, font) -> None:
        super().__init__()

        self.buttonPath = 'Images/UI/Buttons/Pause Button/'
        self.button = button
        self.buttonText = text
        self.image = pygame.transform.scale(pygame.image.load(self.buttonPath + 'Unclicked.png'), (190, 100))
        self.rect = self.image.get_rect()
        self.clicked = False
        self.rect.x = (SCREEN_WIDTH - self.rect.width) / 2
        self.rect.y = yPosition

        self.text = font.render(self.buttonText, True, 'black', None)

    def blit(self, screen):
        if self.clicked:
            self.image = pygame.transform.scale(pygame.image.load(self.buttonPath + 'Clicked.png'), (190, 100))
        else:
            self.image = pygame.transform.scale(pygame.image.load(self.buttonPath + 'Unclicked.png'), (190, 100))
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.rect)
    
    def checkForClick(self, event, state):
        self.buttonPressed = False
        newState = state
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.clicked = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.clicked = False
            if self.rect.collidepoint(event.pos):
                newState = self.button
        return newState

class Group(pygame.sprite.Group):
    def blit(self, screen):
        # Do something to all the sprites in the group
        for sprite in self.sprites():
            sprite.blit(screen)
        
    def checkForClicks(self, events, state):
        # Do something to all the sprites in the group
        newState = state
        for sprite in self.sprites():
            for event in events:
                newState = sprite.checkForClick(event, newState)
        return newState