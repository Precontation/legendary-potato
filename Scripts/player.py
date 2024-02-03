import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.transform.scale_by(pygame.image.load('Images/Player/Up/Up.png'), 5)
        self.rect = self.image.get_rect()
        self.playerDirection = 'Down'
        self.moveSpeed = 5
    def move(self, keys, playerDirection, animationCycle):
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
        if not keys[pygame.K_w] and not keys[pygame.K_UP] and not keys[pygame.K_a] and not keys [pygame.K_LEFT] and not keys[pygame.K_s] and not keys[pygame.K_DOWN] and not keys[pygame.K_d] and not keys[pygame.K_RIGHT]:
            self.image = pygame.transform.scale_by(pygame.image.load('Images/Player/' + playerDirection + '/' + playerDirection + '.png'), 5)
        else:
            self.image = pygame.transform.scale_by(pygame.image.load('Images/Player/' + playerDirection + '/' + playerDirection + str(animationCycle) + '.png'), 5)
        return playerDirection