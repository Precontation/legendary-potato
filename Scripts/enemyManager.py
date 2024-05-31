import pygame
import enemy
from random import randint

class EnemyManager():
    def __init__(self, screen, maxEnemyTypes, spawnTime) -> None:
        self.sprites = pygame.sprite.Group()
        self.spawnTime = spawnTime
        self.maxEnemyTypes = maxEnemyTypes
        self.amountOfEnemies = 0
        self.spawnTime = spawnTime
        self.shouldSpawn = spawnTime
        self.spawnEnemies(screen)
         
    def spawnEnemies(self, screen):
        if self.shouldSpawn >= self.spawnTime:
            print('Spawning an enemy!')
            spriteID = randint(1, self.maxEnemyTypes)
            self.create(spriteID, screen)
            self.amountOfEnemies += 1
            self.shouldSpawn = 1
        else:
            self.shouldSpawn += 1

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
    def checkIfHit(self, player):
        amountHit = 0
        for enemy in self.sprites:
            amountHit += enemy.checkIfHitPlayer(player)
        return amountHit
    
    def checkAttack(self, player):
        for enemy in self.sprites:
            enemy.checkAttack(player)

    def checkCursorTouches(self):
        for enemy in self.sprites:
            enemy.checkCursorTouch()