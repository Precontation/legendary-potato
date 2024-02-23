import pygame
import scroll

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

        self.screenCenterWidth = (screen.get_width() - self.rect.width) / 2
        self.screenCenterHeight = (screen.get_height() - self.rect.height) / 2

        self.rect.x = self.screenCenterWidth
        self.rect.y = self.screenCenterHeight
        
        self.playerDirection = 'Down'
        self.moveSpeed = 7
        self.easing = 10 # 10-20 is good (20 smoother, 10 more practical)

    def scrollX(self, world_x, screen, bg):
        # right
        if self.rect.x >= self.screenCenterWidth + 100:
            scrollAmount = self.rect.x - (self.screenCenterWidth + 100)
            self.rect.x -= scrollAmount / self.easing + 1
            scroll.ScrollRight(bg, screen, scrollAmount / self.easing + 1)
            return scrollAmount
        
        # left
        elif self.rect.x <= self.screenCenterWidth - 100:
            scrollAmount = self.rect.x - (self.screenCenterWidth - 100)
            self.rect.x -= scrollAmount / self.easing - 1
            scroll.ScrollLeft(bg, screen, -(scrollAmount / self.easing - 1))
            return scrollAmount
        else:
            return world_x
    def scrollY(self, world_y, screen, bg):
        # up
        if self.rect.y <= self.screenCenterHeight - 100:
            scrollAmount = self.rect.y - (self.screenCenterHeight - 100)
            self.rect.y -= scrollAmount / self.easing - 1
            scroll.ScrollDown(bg, screen, -(scrollAmount / self.easing - 1))
            return scrollAmount
        # down
        elif self.rect.y >= self.screenCenterHeight + 100:
            scrollAmount = self.rect.y - (self.screenCenterHeight + 100)
            self.rect.y -= scrollAmount / self.easing + 1
            scroll.ScrollUp(bg, screen, scrollAmount / self.easing + 1)
            return scrollAmount
        else:
            return world_y
        
    def move(self, keys, playerDirection, idleAnimationCycle):
        oldPlayerDir = playerDirection
        hasHeldX = False
        hasHeldY = False
        hasMoved = False

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.playerDirection = 'Up'
            self.rect.y -= self.moveSpeed
            hasMoved = True
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.playerDirection = 'Down'
            self.rect.y += self.moveSpeed
            hasMoved = True
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.playerDirection = 'Left'
            self.rect.x -= self.moveSpeed
            hasMoved = True
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.playerDirection = 'Right'
            self.rect.x += self.moveSpeed
            hasMoved = True

        if ((keys[pygame.K_a] or keys[pygame.K_LEFT]) and (keys[pygame.K_d] or keys[pygame.K_RIGHT])) and (self.playerDirection == 'Right' or self.playerDirection == 'Left'):
            self.playerDirection = oldPlayerDir
            hasHeldX = True
        if ((keys[pygame.K_w] or keys[pygame.K_UP]) and (keys[pygame.K_s] or keys[pygame.K_DOWN])) and (self.playerDirection == 'Up' or self.playerDirection == 'Down'):
            self.playerDirection = oldPlayerDir
            hasHeldY = True
        if not keys[pygame.K_w] and not keys[pygame.K_UP] and not keys[pygame.K_a] and not keys [pygame.K_LEFT] and not keys[pygame.K_s] and not keys[pygame.K_DOWN] and not keys[pygame.K_d] and not keys[pygame.K_RIGHT]:
            self.image = pygame.transform.scale_by(pygame.image.load('Images/Player/' + playerDirection + '/Idle' + str(self.idleAnimationCycle) + '.png'), 5)
        else:
            if not hasHeldX and not hasHeldY and hasMoved:
                self.image = pygame.transform.scale_by(pygame.image.load('Images/Player/' + playerDirection + '/Moving' + str(self.moveAnimationCycle) + '.png'), 5)
            else:
                self.image = pygame.transform.scale_by(pygame.image.load('Images/Player/' + playerDirection + '/Idle' + str(self.idleAnimationCycle) + '.png'), 5)
        return playerDirection
    
    def doAnimStuff(self, keys):
        if self.checkIfMoving(keys):
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

            if ((keys[pygame.K_a] or keys[pygame.K_LEFT]) and (keys[pygame.K_d] or keys[pygame.K_RIGHT])) and (self.playerDirection == 'Right' or self.playerDirection == 'Left'):
                hasHeldX = True
            if ((keys[pygame.K_w] or keys[pygame.K_UP]) and (keys[pygame.K_s] or keys[pygame.K_DOWN])) and (self.playerDirection == 'Up' or self.playerDirection == 'Down'):
                hasHeldY = True
            if not keys[pygame.K_w] and not keys[pygame.K_UP] and not keys[pygame.K_a] and not keys [pygame.K_LEFT] and not keys[pygame.K_s] and not keys[pygame.K_DOWN] and not keys[pygame.K_d] and not keys[pygame.K_RIGHT]:
                return False
            else:
                if not hasHeldX and not hasHeldY and hasMoved:
                    return True
                else:
                    return False