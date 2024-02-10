import pygame

scale = [500, 500]
backgroundName = 'Tiles'

image = pygame.image.load('Images/Decoration/Background/' + backgroundName + '.png')
background = pygame.transform.scale(image, scale)

class Background():

    def __init__(self, screen) -> None:
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
                rect[0] = screen.get_width()
            elif rect[0] > ((screen.get_width())):
                rect[0] = -screen.get_width()
            if rect[1] < ((-screen.get_height())):
                rect[1] = screen.get_height()
            elif rect[1] > ((screen.get_height())):
                rect[1] = -screen.get_height()

    def ScrollRight(self):
        for rect in self.rects:
            rect[0] -= 5
    
    def ScrollLeft(self):
        for rect in self.rects:
            rect[0] += 5

    def ScrollUp(self):
        for rect in self.rects:
            rect[1] -= 5

    def ScrollDown(self):
        for rect in self.rects:
            rect[1] += 5

    def ShowBackground(self, screen):
        for rect in self.rects:
            screen.blit(background, rect)