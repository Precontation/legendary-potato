def ScrollRight(bg, enemy, screen, scrollAmount, world_x, projectiles):
    bg.ScrollRight(scrollAmount)
    bg.CheckScroll(screen)
    enemy.ScrollRight(scrollAmount)

    for projectile in projectiles:
            projectile.ScrollRight(scrollAmount)

    return world_x - scrollAmount
    
def ScrollLeft(bg, enemy, screen, scrollAmount, world_x, projectiles):
    bg.ScrollLeft(scrollAmount)
    bg.CheckScroll(screen)
    enemy.ScrollLeft(scrollAmount)

    for projectile in projectiles:
        projectile.ScrollLeft(scrollAmount)

    return world_x + scrollAmount

def ScrollUp(bg, enemy, screen, scrollAmount, world_y, projectiles):
    bg.ScrollUp(scrollAmount)
    bg.CheckScroll(screen)
    enemy.ScrollUp(scrollAmount)

    for projectile in projectiles:
        projectile.ScrollUp(scrollAmount)

    return world_y - scrollAmount

def ScrollDown(bg, enemy, screen, scrollAmount, world_y, projectiles):
    bg.ScrollDown(scrollAmount)
    bg.CheckScroll(screen)
    enemy.ScrollDown(scrollAmount)

    for projectile in projectiles:
        projectile.ScrollDown(scrollAmount)

    return world_y + scrollAmount