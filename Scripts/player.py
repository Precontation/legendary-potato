import pygame

playerDirection = 'Up'
moveSpeed = 5

keysPressed = []

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.transform.scale_by(pygame.image.load('Images/Player/Up/Up.png'), 10)
        self.rect = self.image.get_rect()
    def move(self, keys, playerDirection, animationCycle, keysPressed):
        if keys[pygame.K_w]:
            if not keysPressed.__contains__('Up'):
                playerDirection = 'Up'
                keysPressed += "Up"
            self.rect.y -= moveSpeed
        # else: keysPressed -= 'Up'
        if keys[pygame.K_s]:
            if not keysPressed.__contains__('Down'):
                playerDirection = 'Down'
                keysPressed += 'Down'
            self.rect.y += moveSpeed
        # else: keysPressed -= 'Down'
        if keys[pygame.K_a]:
            if not keysPressed.__contains__('Left'):
                playerDirection = 'Left'
                keysPressed += 'Left'
            self.rect.x -= moveSpeed
        # else: keysPressed -= 'Left'
        if keys[pygame.K_d]:
            if not keysPressed.__contains__('Right'):
                playerDirection = 'Right'
                keysPressed += 'Right'
            self.rect.x += moveSpeed
        # else: keysPressed -= 'd'
        if not keys[pygame.K_w] and not keys[pygame.K_a] and not keys[pygame.K_s] and not keys[pygame.K_d]:
            self.image = pygame.transform.scale_by(pygame.image.load('Images/Player/' + playerDirection + '/' + playerDirection + '.png'), 10)
        else:
            self.image = pygame.transform.scale_by(pygame.image.load('Images/Player/' + playerDirection + '/' + playerDirection + str(animationCycle) + '.png'), 10)
        return playerDirection
    def slash(self):
        if playerDirection == 'Up':
            return self.rect.x, self.rect.y + 10
        elif playerDirection == 'Down':
            return self.rect.x, self.rect.y - 10
        elif playerDirection == 'Right':
            return self.rect.x + 10, self.rect.y
        elif playerDirection == 'Left':
            return self.rect.x + 10, self.rect.y