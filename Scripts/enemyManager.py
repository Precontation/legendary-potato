import pygame
import enemy
from random import randint

class EnemyManager():
    def __init__(self, screen, maxEnemies) -> None:
        self.sprites = pygame.sprite.Group()
        for sprite in range(randint(1, 4)):
            spriteID = randint(1, maxEnemies)
            self.create(spriteID, screen)

    def create(self, enemyID, screen):
        newEnemy = enemy.create(enemyID, screen)
        self.sprites.add(newEnemy)

    def move(self, player):
        for enemy in self.sprites:
            enemy.move(player)
    def blit(self, screen):
        for enemy in self.sprites:
            screen.blit(enemy.image, enemy.rect)

    def ScrollRight(self, scrollAmount):
        for enemy in self.sprites:
            enemy.ScrollRight(scrollAmount)
    def ScrollLeft(self, scrollAmount):
        for enemy in self.sprites:
            enemy.ScrollLeft(scrollAmount)
    def ScrollUp(self, scrollAmount):
        for enemy in self.sprites:
            enemy.ScrollUp(scrollAmount)
    def ScrollDown(self, scrollAmount):
        for enemy in self.sprites:
            enemy.ScrollDown(scrollAmount)