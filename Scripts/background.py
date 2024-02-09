import pygame

background = pygame.transform.scale_by(pygame.image.load('Images/Decoration/Background/Tiles.png'), 15)

class Background():

    bgMidRect = [250, 250]
    bgLeftRect = [0, 250]
    bgRightRect = [500, 250]
    bgUpRect = [250, 500]
    bgDownRect = [250, 0]

    def init(self, screen):
        bgMidRect = [screen.get_size()[0] / background.get_size()[0], screen.get_size()[1] / background.get_size()[1]]
        bgLeftRect = [screen.get_size()[0], screen.get_size()[1] / background.get_size()[1]]
        bgRightRect = [-screen.get_size()[0] / background.get_size()[0], screen.get_size()[1] / background.get_size()[1]]
        bgUpRect = [screen.get_size()[0] / background.get_size()[0], screen.get_size()[1]]
        bgDownRect = [screen.get_size()[0], -screen.get_size()[1]]

    def ScrollRight(self):
        self.bgMidRect[0] -= 5
        self.bgLeftRect[0] -= 5
        self.bgRightRect[0] -= 5
        self.bgUpRect[0] -= 5
        self.bgDownRect[0] -= 5
        print('scroll right')
    
    def ScrollLeft(self):
        self.bgMidRect[0] += 5
        self.bgLeftRect[0] += 5
        self.bgRightRect[0] += 5
        self.bgUpRect[0] += 5
        self.bgDownRect[0] += 5
        print('scroll left')
    
    def ScrollUp(self):
        self.bgMidRect[1] -= 5
        self.bgLeftRect[1] -= 5
        self.bgRightRect[1] -= 5
        self.bgUpRect[1] -= 5
        self.bgDownRect[1] -= 5
        print('scroll up')
    
    def ScrollDown(self):
        self.bgMidRect[1] += 5
        self.bgLeftRect[1] += 5
        self.bgRightRect[1] += 5
        self.bgUpRect[1] += 5
        self.bgDownRect[1] += 5
        print('scroll down')