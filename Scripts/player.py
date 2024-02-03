import pygame

animationCycle = 1

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.transform.scale_by(pygame.image.load('Images/Player/Up/Up.png'), 10)
        self.rect = self.image.get_rect()
        self.playerDirection = 'Down'
        self.moveSpeed = 5
    def update(self, speed) -> None:
        if animationCycle >= 2:
            animationCycle = 1
        else: 
            animationCycle += 1
        pygame.time.Clock().tick(speed) / 1000  
    def move(self, keys, playerDirection, animationCycle):
        if keys[pygame.K_w or pygame.K_UP]:
            self.playerDirection = 'Up'
            self.rect.y -= self.moveSpeed
        if keys[pygame.K_s or pygame.K_DOWN]:
            self.playerDirection = 'Down'
            self.rect.y += self.moveSpeed
        if keys[pygame.K_a or pygame.K_LEFT]:
            self.playerDirection = 'Left'
            self.rect.x -= self.moveSpeed
        if keys[pygame.K_d or pygame.K_RIGHT]:
            self.playerDirection = 'Right'
            self.rect.x += self.moveSpeed
        if not keys[pygame.K_w] and not keys[pygame.K_a] and not keys[pygame.K_s] and not keys[pygame.K_d]:
            self.image = pygame.transform.scale_by(pygame.image.load('Images/Player/' + playerDirection + '/' + playerDirection + '.png'), 10)
        else:
            self.image = pygame.transform.scale_by(pygame.image.load('Images/Player/' + playerDirection + '/' + playerDirection + str(animationCycle) + '.png'), 10)
        return playerDirection