import pygame
import math

def create(enemyID, screen):
    if enemyID == 1:
        enemy = DirectionlessEnemy(screen, "Slime", 2, 10, 0.05, 0.1, 10)
    elif enemyID == 2:
        enemy = DirectionlessEnemy(screen, "Wou", 2, 11, 0.02, 0.3, 15)
    elif enemyID == 3:
        enemy = RotationEnemy(screen, "Clyve", 5, 2, 0.05, 1, 25)
    elif enemyID == 4:
        enemy = DirectionalEnemy(screen, 15, 2, "Ligila", 0.01, 1, 100)
    elif enemyID == 5:
        enemy = DirectionlessEnemy(screen, "Puddle Of Health", 15, 4, 0.00001, -0.1, 1)
    return enemy

class DirectionalEnemy(pygame.sprite.Sprite):
    def __init__(self, screen, animSpeed, animLimit, image, moveSpeed, damage, health):
        super().__init__()

        self.health = health

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
        if dirvect.y < 0:
            self.direction = "Up"
        elif dirvect.y > 0:
            self.direction = "Down"
        if dirvect.x > 0 and dirvect.x > dirvect.y:
            self.direction = "Right"
        elif dirvect.x < 0:
            self.direction = "Left"

        if self.shouldChangeAnim >= self.animSpeed:
            self.animationCycle += 1
            self.shouldChangeAnim = 1
            if self.animationCycle >= self.animLimit:
                self.animationCycle = 1
        else: 
            self.shouldChangeAnim += 1
        self.image = pygame.transform.scale_by(pygame.image.load('Images/Enemies/' + self.imageName + '/' + self.direction + str(self.animationCycle) + '.png'), 5)
    
    def takeDamage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()

    def checkAttack(self, player):
        if self.rect.colliderect(player.rect):
            self.takeDamage(player.damage)

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
    def __init__(self, screen, enemyType, animSpeed, animLimit, moveSpeed, damage, health):
        super().__init__()

        self.health = health

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
    
    def takeDamage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()

    def checkAttack(self, player):
        if self.rect.colliderect(player.rect):
            self.takeDamage(player.damage)

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
    def __init__(self, screen, enemyType, animSpeed, animLimit, moveSpeed, damage, health) -> None:
        super().__init__()
        
        self.health = health

        self.enemyType = enemyType
        self.original_image = pygame.transform.scale_by(pygame.image.load('Images/Enemies/' + enemyType + '/1.png'), 5)
        self.image = self.original_image
        
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
    
    def doAnimStuff(self, player):
        if self.shouldChangeAnim >= self.animSpeed:
            self.animationCycle += 1
            if self.animationCycle >= self.animLimit:
                self.animationCycle = 1
            self.shouldChangeAnim = 1
        else: 
            self.shouldChangeAnim += 1
        self.image = pygame.transform.scale_by(pygame.image.load('Images/Enemies/' + self.enemyType + "/" + str(self.animationCycle) + '.png'), 5)
        
        playerX, playerY = player.rect.center
        angle = math.degrees(-math.atan2(playerY - self.rect.y, playerX - self.rect.x)) - 90
        
        self.image = pygame.transform.rotate(self.original_image, angle)

    def takeDamage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()
            
    def checkAttack(self, player):
        if self.rect.colliderect(player.rect):
            self.takeDamage(player.damage)
    
    def checkIfHitPlayer(self, player):
        if self.rect.colliderect(player.rect):
            return self.damage
        else:
            return 0
        
    def move(self, player):
        dirvect = pygame.math.Vector2((player.rect.centerx - self.rect.centerx) * self.moveSpeed, (player.rect.centery - self.rect.centery) * self.moveSpeed)
        dirvect.normalize()
        self.doAnimStuff(player)
        self.rect.move_ip(dirvect)