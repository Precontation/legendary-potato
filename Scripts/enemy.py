import pygame
from random import randint


def create(enemyID, screen):
    if enemyID == 1:
        enemy = DirectionlessEnemy(screen, "Slime", 2, 9, 0.05)
    elif enemyID == 2:
        enemy = DirectionlessEnemy(screen, "Wou", 2, 10, 0.02)
    elif enemyID == 3:
        enemy = RotationEnemy(screen, "Clyve", 5, 2, 0.1)
    return enemy

class DirectionalEnemy(pygame.sprite.Sprite):
    def __init__(self, screen, animSpeed, animLimit, image, moveSpeed) -> None:
        super().__init__()

        self.image = pygame.transform.scale_by(pygame.image.load('Images/Enemies/' + image + '/' + image + '.png'), 5)
        self.imageName = image

        self.rect = self.image.get_rect()

        self.animSpeed = animSpeed
        self.animLimit = animLimit + 0.1
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

class DirectionlessEnemy(pygame.sprite.Sprite):
    def __init__(self, screen, enemyType, animSpeed, animLimit, moveSpeed) -> None:
        super().__init__()

        self.enemyType = enemyType
        self.image = pygame.transform.scale_by(pygame.image.load('Images/Enemies/' + enemyType + '/0.png'), 5)

        self.rect = self.image.get_rect()

        self.animSpeed = animSpeed
        self.animLimit = animLimit + 0.1
        self.animationCycle = 1
        self.shouldChangeAnim = 1

        self.screenCenterWidth = randint(0, screen.get_width() - self.rect.width)
        self.screenCenterHeight = randint(0, screen.get_height() - self.rect.height)

        self.rect.x = self.screenCenterWidth
        self.rect.y = self.screenCenterHeight

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
        if self.shouldChangeAnim >= self.animSpeed:
            self.animationCycle += 1
            if self.animationCycle >= self.animLimit:
                self.animationCycle = 1
            self.shouldChangeAnim = 1
        else: 
            self.shouldChangeAnim += 1
        self.image = pygame.transform.scale_by(pygame.image.load('Images/Enemies/' + self.enemyType + "/" + str(self.animationCycle) + '.png'), 5)
    
    def move(self, player):
        dirvect = pygame.math.Vector2((player.rect.centerx - self.rect.centerx) * self.moveSpeed, (player.rect.centery - self.rect.centery) * self.moveSpeed)
        dirvect.normalize()
        self.rect.move_ip(dirvect)
        self.doAnimStuff()

class RotationEnemy(pygame.sprite.Sprite):
    def __init__(self, screen, enemyType, animSpeed, animLimit, moveSpeed) -> None:
        super().__init__()

        self.enemyType = enemyType
        self.image = pygame.transform.scale_by(pygame.image.load('Images/Enemies/' + enemyType + '/0.png'), 5)

        self.rect = self.image.get_rect()

        self.animSpeed = animSpeed
        self.animLimit = animLimit + 0.1
        self.animationCycle = 1
        self.shouldChangeAnim = 1

        self.screenCenterWidth = randint(0, screen.get_width() - self.rect.width)
        self.screenCenterHeight = randint(0, screen.get_height() - self.rect.height)

        self.rect.x = self.screenCenterWidth
        self.rect.y = self.screenCenterHeight

        self.moveSpeed = moveSpeed

    def ScrollRight(self, scrollAmount):
        self.rect.x -= scrollAmount
    
    def ScrollLeft(self, scrollAmount):
        self.rect.x += scrollAmount

    def ScrollUp(self, scrollAmount):
        self.rect.y -= scrollAmount

    def ScrollDown(self, scrollAmount):
        self.rect.y += scrollAmount
    
    def doAnimStuff(self, dirvect):
        if self.shouldChangeAnim >= self.animSpeed:
            self.animationCycle += 1
            if self.animationCycle >= self.animLimit:
                self.animationCycle = 1
            self.shouldChangeAnim = 1
        else: 
            self.shouldChangeAnim += 1
        self.image = pygame.transform.scale_by(pygame.image.load('Images/Enemies/' + self.enemyType + "/" + str(self.animationCycle) + '.png'), 5)
        
        self.image = pygame.transform.rotate(self.image, dirvect)
    
    def move(self, player):
        dirvect = pygame.math.Vector2((player.rect.centerx - self.rect.centerx) * self.moveSpeed, (player.rect.centery - self.rect.centery) * self.moveSpeed)
        dirvect.normalize()
        self.rect.move_ip(dirvect)
        self.doAnimStuff(dirvect.angle_to((player.rect.x, player.rect.y)))