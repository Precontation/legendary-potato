import pygame
import math
from pygame.sprite import Group

class Dagger(pygame.sprite.Sprite):
    def __init__(self, damage, player) -> None:
        super().__init__()

        self.speed = 5

        self.original_image = pygame.transform.scale_by(pygame.image.load("Images/Projectiles/Dagger.png"), 3)
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = player.rect.center

        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        dx = self.mouse_x - self.rect.x
        dy = self.mouse_y - self.rect.y

        self.angle = math.atan2(dx, dy)

        self.mouse_x = math.sin(self.angle)
        self.mouse_y = math.cos(self.angle)
    
        self.image = pygame.transform.rotate(self.original_image, math.degrees(self.angle) - 180)
        
        self.damage = damage

    def move(self, screen, enemies):
        self.rect.x += self.mouse_x * self.speed
        self.rect.y += self.mouse_y * self.speed

        for enemy in enemies.sprites:
            if self.rect.colliderect(enemy.rect):
                enemy.takeDamage(self.damage)
                self.kill()

        if self.rect.colliderect(screen.get_rect()):
            screen.blit(self.image, self.rect)
        else:
            self.kill()

    def ScrollRight(self, scrollAmount):
        self.rect.x -= scrollAmount
    
    def ScrollLeft(self, scrollAmount):
        self.rect.x += scrollAmount

    def ScrollUp(self, scrollAmount):
        self.rect.y -= scrollAmount

    def ScrollDown(self, scrollAmount):
        self.rect.y += scrollAmount