import pygame
from random import randint

def create(enemyID, screen):
    if enemyID == 1:
        enemy = DirectionlessEnemy(screen, "Slime", 2, 10, 0.05, 0.1)
    elif enemyID == 2:
        enemy = DirectionlessEnemy(screen, "Wou", 2, 11, 0.02, 0.3)
    elif enemyID == 3:
        enemy = RotationEnemy(screen, "Clyve", 5, 2, 0.05, 1)
    elif enemyID == 4:
        enemy = DirectionalEnemy(screen, 15, 2, "Ligila", 0.01, 1)
    elif enemyID == 5:
        enemy = DirectionlessEnemy(screen, "Puddle Of Health", 15, 4, 0.00001, -0.1)
    return enemy

class DirectionalEnemy(pygame.sprite.Sprite):
    def __init__(self, screen, animSpeed, animLimit, image, moveSpeed, damage):
        super().__init__()

        self.image = pygame.transform.scale_by(pygame.image.load('Images/Enemies/' + image + '/Down1.png'), 5)
        self.imageName = image

        self.rect = self.image.get_rect()

        self.animSpeed = animSpeed
        self.animLimit = animLimit + 0.1
        self.animationCycle = 1
        self.shouldChangeAnim = 1
        
        self.damage = damage
        self.isMoving = False

        self.rect.x = screen.get_width()
        self.rect.y = screen.get_height()
        
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
    
    def doAnimStuff(self, dirvect):
        # check if which direction it is facing for direction 
        # if pygame.transform.rotate(self.image, dirvect)
        if self.shouldChangeAnim >= self.animSpeed:
            self.animationCycle += 1
            self.shouldChangeAnim = 1
            if self.animationCycle >= self.animLimit:
                self.animationCycle = 1
        else: 
            self.shouldChangeAnim += 1
        self.image = pygame.transform.scale_by(pygame.image.load('Images/Enemies/' + self.imageName + '/' + self.direction + str(self.animationCycle) + '.png'), 5)
    
    def checkIfHitPlayer(self, player):
        if self.rect.colliderect(player.rect):
            return self.damage
        else:
            return 0
        
    def move(self, player):
        dirvect = pygame.math.Vector2((player.rect.centerx - self.rect.centerx) * self.moveSpeed, (player.rect.centery - self.rect.centery) * self.moveSpeed)
        dirvect.normalize()
        self.rect.move_ip(dirvect)
        self.doAnimStuff(dirvect)

class DirectionlessEnemy(pygame.sprite.Sprite):
    def __init__(self, screen, enemyType, animSpeed, animLimit, moveSpeed, damage):
        super().__init__()

        self.enemyType = enemyType
        self.image = pygame.transform.scale_by(pygame.image.load('Images/Enemies/' + enemyType + '/1.png'), 5)

        self.rect = self.image.get_rect()

        self.animSpeed = animSpeed
        self.animLimit = animLimit + 0.1
        self.animationCycle = 1
        self.shouldChangeAnim = 1

        self.damage = damage

        self.rect.x = screen.get_width()
        self.rect.y = screen.get_height()

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
    
    def checkIfHitPlayer(self, player):
        if self.rect.colliderect(player.rect):
            return self.damage
        else:
            return 0
            
    def move(self, player):
        dirvect = pygame.math.Vector2((player.rect.centerx - self.rect.centerx) * self.moveSpeed, (player.rect.centery - self.rect.centery) * self.moveSpeed)
        dirvect.normalize()
        self.rect.move_ip(dirvect)
        self.doAnimStuff()

class RotationEnemy(pygame.sprite.Sprite):
    def __init__(self, screen, enemyType, animSpeed, animLimit, moveSpeed, damage) -> None:
        super().__init__()

        self.enemyType = enemyType
        self.image = pygame.transform.scale_by(pygame.image.load('Images/Enemies/' + enemyType + '/1.png'), 5)

        self.rect = self.image.get_rect()

        self.animSpeed = animSpeed
        self.animLimit = animLimit + 0.1
        self.animationCycle = 1
        self.shouldChangeAnim = 1

        self.damage = damage

        self.rect.x = screen.get_width()
        self.rect.y = screen.get_height()
        
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

    def checkIfHitPlayer(self, player):
        if self.rect.colliderect(player.rect):
            return self.damage
        else:
            return 0
        
    def move(self, player):
        dirvect = pygame.math.Vector2((player.rect.centerx - self.rect.centerx) * self.moveSpeed, (player.rect.centery - self.rect.centery) * self.moveSpeed)
        dirvect.normalize()
        self.doAnimStuff(dirvect.angle_to((player.rect.centerx, player.rect.centery)))
        self.rect.move_ip(dirvect)