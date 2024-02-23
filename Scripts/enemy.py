import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, animSpeed, animLimit) -> None:
        super().__init__()

        self.image = pygame.transform.scale_by(pygame.image.load('Images/Player/Up/Up.png'), 5)
        self.rect = self.image.get_rect()

        self.animSpeed = animSpeed
        self.animLimit = animLimit
        self.moveAnimationCycle = 1
        self.idleAnimationCycle = 1
        self.shouldChangeMoveAnim = 1
        self.shouldChangeIdleAnim = 1
        
        self.isMoving = False

        self.screenCenterWidth = (screen.get_width() - self.rect.width) / 2
        self.screenCenterHeight = (screen.get_height() - self.rect.height) / 2

        self.rect.x = self.screenCenterWidth
        self.rect.y = self.screenCenterHeight
        
        self.direction = 'Down'
        self.moveSpeed = 7

    def ScrollRight(self, scrollAmount):
        self.rect.x -= scrollAmount
    
    def ScrollLeft(self, scrollAmount):
        self.rect.x += scrollAmount

    def ScrollUp(self, scrollAmount):
        self.rect.y -= scrollAmount

    def ScrollDown(self, scrollAmount):
        self.rect.y += scrollAmount
    
    def doAnimStuff(self, keys):
        if self.isMoving:
            self.shouldChangeIdleAnim = 1
            self.idleAnimationCycle = 1
            if self.shouldChangeMoveAnim >= self.animSpeed:
                self.moveAnimationCycle += 1
                if self.moveAnimationCycle >= 3:
                    self.moveAnimationCycle = 1
                self.shouldChangeMoveAnim = 1
            else: 
                self.shouldChangeMoveAnim += 1
        else:
            self.shouldChangeMoveAnim = 1
            self.moveAnimationCycle = 1

            if self.shouldChangeIdleAnim >= self.animSpeed:
                self.idleAnimationCycle += 1
                if self.idleAnimationCycle >= 3:
                    self.idleAnimationCycle = 1
                self.shouldChangeIdleAnim = 1
            else: 
                self.shouldChangeIdleAnim += 1