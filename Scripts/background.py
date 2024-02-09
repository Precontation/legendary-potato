import pygame

background = pygame.transform.scale_by(pygame.image.load('../Images/Decoration/Background/Tiles.png'), 15)

def updateStuff(screen, world_x, world_y):
    screen.blit(background, (world_x, world_y))
    screen.blit(background, (world_x + background.get_size()[0], world_y))
    screen.blit(background, (world_x - background.get_size()[0], world_y))
    screen.blit(background, (world_x, world_y + background.get_size()[1]))
    screen.blit(background, (world_x, world_y - background.get_size()[1]))
    return