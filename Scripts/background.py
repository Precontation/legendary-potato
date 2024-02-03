import pygame

background = pygame.image.load('Images/Decoration/Background/Tiles.png')

def updateStuff(screen, world_x, world_y):
    screen.blit(pygame.transform.scale_by(background, 15), (world_x, world_y))