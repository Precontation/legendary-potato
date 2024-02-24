import pygame
from random import randint


def create(enemyID, screen):
    if enemyID == 1:
        slime = Slime(screen)
        return slime

class EnemyTemplate(pygame.sprite.Sprite):
    def __init__(self, screen, animSpeed, animLimit, image, moveSpeed) -> None:
        super().__init__()

        self.image = pygame.transform.scale_by(pygame.image.load('Images/Enemies/' + image + '/' + image + '.png'), 5)
        self.imageName = image

        self.rect = self.image.get_rect()

        self.animSpeed = animSpeed
        self.animLimit = animLimit
        self.moveAnimationCycle = 1
        self.idleAnimationCycle = 1
        self.shouldChangeMoveAnim = 1
        self.shouldChangeIdleAnim = 1
        
        self.isMoving = False

        self.screenCenterWidth = randint(0, screen.get_width() - self.rect.width)
        self.screenCenterHeight = randint(0, screen.get_height() - self.rect.height)

        self.rect.x = self.screenCenterWidth
        self.rect.y = self.screenCenterHeight
        
        self.direction = 'Down'
        self.moveSpeed = moveSpeed

    def ScrollRight(self, scrollAmount):
        self.rect.x -= scrollAmount
    
    def ScrollLeft(self, scrollAmount):
        self.rect.x += scrollAmount

    def ScrollUp(self, scrollAmount):
        self.rect.y -= scrollAmount

    def ScrollDown(self, scrollAmount):
        self.rect.y += scrollAmount
    
    def doAnimStuff(self):
        if self.isMoving:
            self.shouldChangeIdleAnim = 1
            self.idleAnimationCycle = 1
            if self.shouldChangeMoveAnim >= self.animSpeed:
                self.moveAnimationCycle += 1
                if self.moveAnimationCycle >= self.animLimit:
                    self.moveAnimationCycle = 1
                self.shouldChangeMoveAnim = 1
            else: 
                self.shouldChangeMoveAnim += 1
            self.image = pygame.transform.scale_by(pygame.image.load('Images/Enemies/' + self.imageName + '/Moving' + str(self.moveAnimationCycle) + '.png'), 5)
        else:
            self.shouldChangeMoveAnim = 1
            self.moveAnimationCycle = 1

            if self.shouldChangeIdleAnim >= self.animSpeed:
                self.idleAnimationCycle += 1
                if self.idleAnimationCycle >= self.animLimit:
                    self.idleAnimationCycle = 1
                self.shouldChangeIdleAnim = 1
            else: 
                self.shouldChangeIdleAnim += 1
            self.image = pygame.transform.scale_by(pygame.image.load('Images/Enemies/' + self.imageName + '/Idle' + str(self.idleAnimationCycle) + '.png'), 5)

class Slime(pygame.sprite.Sprite):
    def __init__(self, screen) -> None:
        super().__init__()

        self.image = pygame.transform.scale_by(pygame.image.load('Images/Enemies/Slime/Slime.png'), 5)

        self.rect = self.image.get_rect()

        self.animSpeed = 2
        self.animLimit = 9
        self.animationCycle = 1
        self.shouldChangeAnim = 1

        self.screenCenterWidth = randint(0, screen.get_width() - self.rect.width)
        self.screenCenterHeight = randint(0, screen.get_height() - self.rect.height)

        self.rect.x = self.screenCenterWidth
        self.rect.y = self.screenCenterHeight

        self.moveSpeed = 0.05

    def ScrollRight(self, scrollAmount):
        self.rect.x -= scrollAmount
    
    def ScrollLeft(self, scrollAmount):
        self.rect.x += scrollAmount

    def ScrollUp(self, scrollAmount):
        self.rect.y -= scrollAmount

    def ScrollDown(self, scrollAmount):
        self.rect.y += scrollAmount
    
    def doAnimStuff(self):
        if self.shouldChangeAnim >= self.animSpeed:
            self.animationCycle += 1
            if self.animationCycle >= self.animLimit:
                self.animationCycle = 1
            self.shouldChangeAnim = 1
        else: 
            self.shouldChangeAnim += 1
        self.image = pygame.transform.scale_by(pygame.image.load('Images/Enemies/Slime/'+ str(self.animationCycle) + '.png'), 5)
    
    def move(self, player):
        dirvect = pygame.math.Vector2((player.rect.centerx - self.rect.x) * self.moveSpeed, (player.rect.centery - self.rect.y) * self.moveSpeed)
        dirvect.normalize()
        self.rect.move_ip(dirvect)
        self.doAnimStuff()