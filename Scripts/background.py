import pygame

class Background():
    def __init__(self, screen) -> None:
        self.backgroundName = 'Bubbles'

        self.scale = [screen.get_width(), screen.get_height()]
        self.image = pygame.image.load('Images/Decoration/Background/' + self.backgroundName + '.png')
        self.background = pygame.transform.scale(self.image, self.scale)
        
        self.bgMidRect = [screen.get_width() / 2, screen.get_height() / 2]
        self.bgLeftRect = [0, screen.get_height() / 2]
        self.bgRightRect = [screen.get_width(), screen.get_height() / 2]
        self.bgUpRect = [screen.get_width() / 2, 0]
        self.bgDownRect = [screen.get_width() / 2, screen.get_height()]
        self.bgTopRightRect = [screen.get_width(), 0]
        self.bgTopLeftRect = [0, 0]
        self.bgBottomRightRect = [screen.get_width(), screen.get_height()]
        self.bgbottomLeftRect = [0, screen.get_height()]
        self.rects = [self.bgMidRect, self.bgLeftRect, self.bgRightRect, self.bgUpRect, self.bgDownRect, self.bgTopRightRect, self.bgTopLeftRect, self.bgBottomRightRect, self.bgbottomLeftRect]

    def CheckScroll(self, screen):
        for rect in self.rects:
            if rect[0] < ((-screen.get_width())):
                rect[0] += screen.get_width() * 2
            elif rect[0] > ((screen.get_width())):
                rect[0] -= screen.get_width() * 2
            if rect[1] < ((-screen.get_height())):
                rect[1] += screen.get_height() * 2
            elif rect[1] > ((screen.get_height())):
                rect[1] -= screen.get_height() * 2

    def ScrollRight(self, scrollAmount):
        for rect in self.rects:
            rect[0] -= scrollAmount
    
    def ScrollLeft(self, scrollAmount):
        for rect in self.rects:
            rect[0] += scrollAmount

    def ScrollUp(self, scrollAmount):
        for rect in self.rects:
            rect[1] -= scrollAmount

    def ScrollDown(self, scrollAmount):
        for rect in self.rects:
            rect[1] += scrollAmount

    def ShowBackground(self, screen):
        for rect in self.rects:
            screen.blit(self.background, rect)