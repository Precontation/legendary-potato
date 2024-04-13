from typing import Any
import pygame
import scroll
import projectile

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, animSpeed, animLimit, health) -> None:
        super().__init__()

        self.image = pygame.transform.scale_by(pygame.image.load('Images/Player/Up/Idle1.png'), 5)
        self.rect = self.image.get_rect()

        self.animSpeed = animSpeed
        self.animLimit = animLimit
        self.moveAnimationCycle = 1
        self.idleAnimationCycle = 1
        self.shouldChangeMoveAnim = 1
        self.shouldChangeIdleAnim = 1

        self.projectiles = pygame.sprite.Group()
        self.weaponType = "Old Dagger"
        self.damage = 10
        
        self.screenCenterWidth = (screen.get_width() - self.rect.width) / 2
        self.screenCenterHeight = (screen.get_height() - self.rect.height) / 2

        self.health = health
        self.kills = 0

        self.rect.x = self.screenCenterWidth
        self.rect.y = self.screenCenterHeight
        
        self.direction = 'Down'
        self.moveSpeed = 7
        self.easing = 10 # 10-20 is good (20 smoother, 10 more practical)
        
        self.attacking = ""
        self.attackingCycle = ""
        self.shouldChangeAttackingCycle = 0
        self.hasPressedSpace = False
    
    def throw(self):
        newDagger = projectile.Dagger(self.damage, self)
        self.projectiles.add(newDagger)

    def attack(self, keys, enemyManager):
        if self.attacking == "":
            self.shouldChangeAttackingCycle = 0
            if keys[pygame.K_SPACE]:
                if not self.hasPressedSpace:
                        self.hasPressedSpace = True
                        if self.weaponType == "Sword":
                            # TODO: sword is REALLY bad right now, so at least give a graphic
                            enemyManager.checkAttack(self)
                        elif self.weaponType == "Dagger":
                            self.throw()
                        elif self.weaponType == "Old Dagger":
                            self.throw()
                        self.attackingCycle = 1
                        self.attacking = "Attacking"
            else:
                self.hasPressedSpace = False
        else:
            if self.shouldChangeAttackingCycle >= 5:
                self.shouldChangeAttackingCycle = 0
                self.attackingCycle += 1
                if self.attackingCycle == 3:
                    self.idleAnimationCycle = 2
                    self.moveAnimationCycle = 1
                    self.shouldChangeIdleAnim = 1
                    self.shouldChangeMoveAnim = 1

                    self.attacking = ""
                    self.attackingCycle = 0
                if self.attackingCycle == 0:
                    self.attackingCycle = ""
            else:
                self.shouldChangeAttackingCycle += 1

    def scrollX(self, world_x, screen, bg, enemy):
        newX = world_x
        # right
        if self.rect.x >= self.screenCenterWidth + 100:
            scrollAmount = self.rect.x - (self.screenCenterWidth + 100)
            self.rect.x -= scrollAmount / self.easing + 1
            newX = scroll.ScrollRight(bg, enemy, screen, scrollAmount / self.easing + 1, world_x, self.projectiles)
        
        # left
        elif self.rect.x <= self.screenCenterWidth - 100:
            scrollAmount = self.rect.x - (self.screenCenterWidth - 100)
            self.rect.x -= scrollAmount / self.easing - 1
            newX = scroll.ScrollLeft(bg, enemy, screen, -(scrollAmount / self.easing - 1), world_x, self.projectiles)
        return newX
    def scrollY(self, world_y, screen, bg, enemy):
        newY = world_y
        # up
        if self.rect.y <= self.screenCenterHeight - 100:
            scrollAmount = self.rect.y - (self.screenCenterHeight - 100)
            self.rect.y -= scrollAmount / self.easing - 1
            newY = scroll.ScrollDown(bg, enemy, screen, -(scrollAmount / self.easing - 1), world_y, self.projectiles)
        # down
        elif self.rect.y >= self.screenCenterHeight + 100:
            scrollAmount = self.rect.y - (self.screenCenterHeight + 100)
            self.rect.y -= scrollAmount / self.easing + 1
            newY = scroll.ScrollUp(bg, enemy, screen, scrollAmount / self.easing + 1, world_y, self.projectiles)
        return newY
        
    def move(self, keys, screen, enemyManager):
        oldPlayerDir = self.direction
        hasHeldX = False
        hasHeldY = False
        hasMoved = False

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.direction = 'Up'
            self.rect.y -= self.moveSpeed
            hasMoved = True
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.direction = 'Down'
            self.rect.y += self.moveSpeed
            hasMoved = True
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.direction = 'Left'
            self.rect.x -= self.moveSpeed
            hasMoved = True
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.direction = 'Right'
            self.rect.x += self.moveSpeed
            hasMoved = True

        if ((keys[pygame.K_a] or keys[pygame.K_LEFT]) and (keys[pygame.K_d] or keys[pygame.K_RIGHT])) and (self.direction == 'Right' or self.direction == 'Left'):
            self.direction = oldPlayerDir
            hasHeldX = True
        if ((keys[pygame.K_w] or keys[pygame.K_UP]) and (keys[pygame.K_s] or keys[pygame.K_DOWN])) and (self.direction == 'Up' or self.direction == 'Down'):
            self.direction = oldPlayerDir
            hasHeldY = True

        if (hasHeldX and not hasHeldY) and (keys[pygame.K_LEFT] or keys[pygame.K_a]): self.direction = "Left"
        if (hasHeldX and not hasHeldY) and (keys[pygame.K_RIGHT] or keys[pygame.K_r]): self.direction = "Right"
        if (hasHeldY and not hasHeldX) and (keys[pygame.K_UP] or keys[pygame.K_w]): self.direction = "Up"
        if (hasHeldY and not hasHeldX) and (keys[pygame.K_DOWN] or keys[pygame.K_s]): self.direction = "Down"

        if not keys[pygame.K_w] and not keys[pygame.K_UP] and not keys[pygame.K_a] and not keys [pygame.K_LEFT] and not keys[pygame.K_s] and not keys[pygame.K_DOWN] and not keys[pygame.K_d] and not keys[pygame.K_RIGHT]:
            self.image = pygame.transform.scale_by(pygame.image.load('Images/Player/' + self.direction + '/Idle' + str(self.idleAnimationCycle) + self.attacking + str(self.attackingCycle) + '.png'), 5)
        else:
            if (not hasHeldX and not hasHeldY) and hasMoved:
              self.image = pygame.transform.scale_by(pygame.image.load('Images/Player/' + self.direction + '/Moving' + str(self.moveAnimationCycle) + self.attacking + str(self.attackingCycle) + '.png'), 5)
            else:
                self.image = pygame.transform.scale_by(pygame.image.load('Images/Player/' + self.direction + '/Idle' + str(self.idleAnimationCycle) + self.attacking + str(self.attackingCycle) + '.png'), 5)
        self.doAnimStuff(keys, screen, enemyManager)
        return self.direction
    
    def doAnimStuff(self, keys, screen, enemyManager):
        for projectile in self.projectiles:
            projectile.move(screen, enemyManager, self)

        if self.checkIfMoving(keys):
            self.shouldChangeIdleAnim = 1
            self.idleAnimationCycle = 1
            if self.shouldChangeMoveAnim >= self.animSpeed:
                self.moveAnimationCycle += 1
                if self.moveAnimationCycle >= self.animLimit:
                    self.moveAnimationCycle = 1
                self.shouldChangeMoveAnim = 1
            else: 
                self.shouldChangeMoveAnim += 1
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
    def checkIfMoving(self, keys):
            hasHeldX = False
            hasHeldY = False
            hasMoved = False

            if keys[pygame.K_w] or keys[pygame.K_UP]:
                hasMoved = True
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                hasMoved = True
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                hasMoved = True
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                hasMoved = True

            if ((keys[pygame.K_a] or keys[pygame.K_LEFT]) and (keys[pygame.K_d] or keys[pygame.K_RIGHT])) and (self.direction == 'Right' or self.direction == 'Left'):
                hasHeldX = True
            if ((keys[pygame.K_w] or keys[pygame.K_UP]) and (keys[pygame.K_s] or keys[pygame.K_DOWN])) and (self.direction == 'Up' or self.direction == 'Down'):
                hasHeldY = True
            if not keys[pygame.K_w] and not keys[pygame.K_UP] and not keys[pygame.K_a] and not keys [pygame.K_LEFT] and not keys[pygame.K_s] and not keys[pygame.K_DOWN] and not keys[pygame.K_d] and not keys[pygame.K_RIGHT]:
                return False
            else:
                if not hasHeldX and not hasHeldY and hasMoved:
                    return True
                else:
                    return False