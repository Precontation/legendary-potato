def ScrollRight(bg, enemy, screen, scrollAmount):
    bg.ScrollRight(scrollAmount)
    bg.CheckScroll(screen)
    enemy.ScrollRight(scrollAmount)
    # this is where you put other enemmies, items, blocks, etc
    
def ScrollLeft(bg, enemy, screen, scrollAmount):
    bg.ScrollLeft(scrollAmount)
    bg.CheckScroll(screen)
    enemy.ScrollLeft(scrollAmount)
    # this is where you put other enemmies, items, blocks, etc

def ScrollUp(bg, enemy, screen, scrollAmount):
    bg.ScrollUp(scrollAmount)
    bg.CheckScroll(screen)
    enemy.ScrollUp(scrollAmount)
    # this is where you put other enemmies, items, blocks, etc

def ScrollDown(bg, enemy, screen, scrollAmount):
    bg.ScrollDown(scrollAmount)
    bg.CheckScroll(screen)
    enemy.ScrollDown(scrollAmount)
    # this is where you put other enemmies, items, blocks, etc