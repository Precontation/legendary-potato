import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.transform.scale_by(pygame.image.load('Images/Player/Up/Up.png'), 5)
        self.rect = self.image.get_rect()
        self.playerDirection = 'Down'
        self.moveSpeed = 5

    def scrollX(self, world_x, screen):
        if self.rect.x >= ((screen.get_width() - self.rect.width) / 2) + 100:
            self.rect.x -= 5
            return world_x - 5
        elif self.rect.x <= ((screen.get_width() - self.rect.width) / 2) - 100:
            self.rect.x += 5
            return world_x + 5
        else:
            return world_x
    def scrollY(self, world_y, screen):
        if self.rect.y >= ((screen.get_height() - self.rect.height) / 2) + 100:
            self.rect.y -= 5
            return world_y - 5
        elif self.rect.y <= ((screen.get_height() - self.rect.height) / 2) - 100:
            self.rect.y += 5
            return world_y + 5
        else:
            return world_y
        
    def move(self, keys, playerDirection, moveAnimationCycle, idleAnimationCycle):
        oldPlayerDir = playerDirection
        hasSwitched = False

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.playerDirection = 'Up'
            self.rect.y -= self.moveSpeed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.playerDirection = 'Down'
            self.rect.y += self.moveSpeed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.playerDirection = 'Left'
            self.rect.x -= self.moveSpeed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.playerDirection = 'Right'
            self.rect.x += self.moveSpeed
            
        if ((keys[pygame.K_a] or keys[pygame.K_LEFT]) and (keys[pygame.K_d] or keys[pygame.K_RIGHT])) and (self.playerDirection == 'Right' or self.playerDirection == 'Left'):
            self.playerDirection = oldPlayerDir
        if ((keys[pygame.K_w] or keys[pygame.K_UP]) and (keys[pygame.K_s] or keys[pygame.K_DOWN])) and (self.playerDirection == 'Up' or self.playerDirection == 'Down'):
            self.playerDirection = oldPlayerDir

        if not keys[pygame.K_w] and not keys[pygame.K_UP] and not keys[pygame.K_a] and not keys [pygame.K_LEFT] and not keys[pygame.K_s] and not keys[pygame.K_DOWN] and not keys[pygame.K_d] and not keys[pygame.K_RIGHT]:
            if not (keys[pygame.K_a] and keys[pygame.K_d]) or (keys[pygame.w])
            self.image = pygame.transform.scale_by(pygame.image.load('Images/Player/' + playerDirection + '/Idle' + str(idleAnimationCycle) + '.png'), 5)
        else:
            self.image = pygame.transform.scale_by(pygame.image.load('Images/Player/' + playerDirection + '/Moving' + str(moveAnimationCycle) + '.png'), 5)
        return playerDirection