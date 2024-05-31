import pygame
import math
from random import randint

import pygame.imageext

def create(enemyID, screen):
    if enemyID == 1:
        enemy = DirectionlessEnemy(screen, 'Slime', 2, 10, 5, 0.1, 10)
    elif enemyID == 2:
        enemy = DirectionlessEnemy(screen, 'Wou', 2, 11, 2, 0.3, 15)
    elif enemyID == 3:
        enemy = RotationEnemy(screen, 'Clyve', 5, 2, 5, 1, 25)
    elif enemyID == 4:
        enemy = DirectionalEnemy(screen, 'Ligila', 15, 2, 5, 1, 100)
        print('lig')
    elif enemyID == 5:
        enemy = DirectionlessEnemy(screen, 'Puddle Of Health', 15, 4, 0.00001, -0.1, 1)
    elif enemyID == 6:
        enemy = DirectionlessEnemy(screen, 'Bob', 10, 2, -5, -5, 100)
    return enemy

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, image, animSpeed, animLimit, moveSpeed, damage, health):
        super().__init__()

        self.moveSpeed = moveSpeed
        self.health = health

        self.enemyType = image

        self.imageName = image

        self.image = pygame.image.load('Images/Player/Down/Idle1.png')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image, 0)

        self.animSpeed = animSpeed
        self.animLimit = animLimit + 0.1
        self.animationCycle = 1
        self.shouldChangeAnim = 1
        
        self.damage = damage

        pos = randint(0, 4)
        if pos == 0: # right
            self.rect.x = screen.get_width() + 10
            self.rect.y = randint(0, screen.get_height())
        elif pos == 2: # left
            self.rect.x = -10
            self.rect.y = randint(0, screen.get_height())
        elif pos == 3: # up
            self.rect.y = -10
            self.rect.x = randint(0, screen.get_width())
        else: # down
            self.rect.y = screen.get_height() + 10
            self.rect.x = randint(0, screen.get_width())

    def ScrollRight(self, scrollAmount):
        self.rect.x -= scrollAmount
    
    def ScrollLeft(self, scrollAmount):
        self.rect.x += scrollAmount

    def ScrollUp(self, scrollAmount):
        self.rect.y -= scrollAmount

    def ScrollDown(self, scrollAmount):
        self.rect.y += scrollAmount

    def takeDamage(self, amount, player, velocity):
        self.health -= amount
        self.rect.x += velocity[0] * 3
        self.rect.y += velocity[1] * 3
        if self.health <= 0:
            player.kills += 1
            self.kill()

    def checkAttack(self, player):
        if pygame.sprite.collide_mask(self, player):
            self.takeDamage(player.damage, player, 0)

    def checkIfHitPlayer(self, player):
        if pygame.sprite.collide_mask(self, player):
            return self.damage
        else:
            return 0
        
    def move(self, player):
        dirvect = pygame.math.Vector2(0, 0)

        try:
            distance = math.sqrt((player.rect.x - self.rect.x)**2 + (player.rect.y - self.rect.y)**2)
            dirvect = pygame.math.Vector2(((player.rect.x - self.rect.x) * self.moveSpeed) / distance, ((player.rect.y - self.rect.y) * self.moveSpeed) / distance)
            dirvect.normalize()
            self.rect.move_ip(dirvect)
        except:
            pass

        self.doAnimStuff(dirvect, player)

    def checkCursorTouch(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)

class DirectionalEnemy(Enemy, pygame.sprite.Sprite):
    def __init__(self, screen, image, animSpeed, animLimit, moveSpeed, damage, health):
        super().__init__(screen, image, animSpeed, animLimit, moveSpeed, damage, health)

        self.image = pygame.transform.scale_by(pygame.image.load('Images/Enemies/' + self.enemyType + '/Down1.png'), 5)
        self.direction = 'Down'
    
    def doAnimStuff(self, dirvect, player):
        if dirvect.y < 0:
            self.direction = 'Up'
        elif dirvect.y >= 0:
            self.direction = 'Down'
        if abs(dirvect.x) > abs(dirvect.y):
            if dirvect.x > 0:
                self.direction = 'Right'
            elif dirvect.x <= 0:
                self.direction = 'Left'

        if self.shouldChangeAnim >= self.animSpeed:
            self.animationCycle += 1
            self.shouldChangeAnim = 1
            if self.animationCycle >= self.animLimit:
                self.animationCycle = 1
        else: 
            self.shouldChangeAnim += 1

        self.image = pygame.transform.scale_by(pygame.image.load('Images/Enemies/' + self.imageName + '/' + self.direction + str(self.animationCycle) + '.png'), 5)
        self.mask = pygame.mask.from_surface(self.image, 0)
    
class DirectionlessEnemy(Enemy, pygame.sprite.Sprite):
    def __init__(self, screen, image, animSpeed, animLimit, moveSpeed, damage, health):
        super().__init__(screen, image, animSpeed, animLimit, moveSpeed, damage, health)

        self.image = pygame.transform.scale_by(pygame.image.load('Images/Enemies/' + self.enemyType + '/' + str(self.animationCycle) + '.png'), 5)

    def doAnimStuff(self, dirvect, player):
        if self.shouldChangeAnim >= self.animSpeed:
            self.animationCycle += 1
            if self.animationCycle >= self.animLimit:
                self.animationCycle = 1
            self.shouldChangeAnim = 1
        else: 
            self.shouldChangeAnim += 1
        self.image = pygame.transform.scale_by(pygame.image.load('Images/Enemies/' + self.enemyType + '/' + str(self.animationCycle) + '.png'), 5)
        self.mask = pygame.mask.from_surface(self.image, 0)

class RotationEnemy(Enemy, pygame.sprite.Sprite):
    def __init__(self, screen, image, animSpeed, animLimit, moveSpeed, damage, health) -> None:
        super().__init__(screen, image, animSpeed, animLimit, moveSpeed, damage, health)

        self.original_image = pygame.transform.scale_by(pygame.image.load('Images/Enemies/' + self.enemyType + '/1.png'), 5)
        self.image = self.original_image

    def doAnimStuff(self, dirvect, player):
        if self.shouldChangeAnim >= self.animSpeed:
            self.animationCycle += 1
            if self.animationCycle >= self.animLimit:
                self.animationCycle = 1
            self.shouldChangeAnim = 1
        else: 
            self.shouldChangeAnim += 1
        self.image = pygame.transform.scale_by(pygame.image.load('Images/Enemies/' + self.enemyType + '/' + str(self.animationCycle) + '.png'), 5)
        
        playerX, playerY = player.rect.center
        angle = math.degrees(-math.atan2(playerY - self.rect.y, playerX - self.rect.x)) - 90
        
        self.image = pygame.transform.rotate(self.original_image, angle)
        
        self.mask = pygame.mask.from_surface(self.image, 0)