import pygame

SCREEN_WIDTH = 340
SCREEN_HEIGHT = 560
screen = pygame.display.get_active()

pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.init()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #TODO: add stuff
pygame.quit()




"""import pgzrun
WIDTH=600
HEIGHT=600
gamestate="start"
Character=Actor(("player_down"),(WIDTH/2, HEIGHT/2))
Character.xspeed=5
Character.yspeed=5

def draw():
    global gamestate
    global gamestate
    if gamestate=="start":
        screen.draw.text("Press Enter to start",center=(WIDTH/2,HEIGHT/2),fontsize=50)
    if gamestate=="play":
        screen.clear()
        Character.draw()
    if gamestate=="end":
        screen.clear()
        screen.draw.text("Press Enter to play again",center=(WIDTH/2,HEIGHT/2+100),fontsize=25)
        screen.draw.text("Press escape to exit",center=(WIDTH/2,HEIGHT/2+125),fontsize=25)
    if gamestate=="menu":
        screen.clear()
        screen.draw.text("Press Enter to resume", center=(WIDTH / 2, HEIGHT / 2), fontsize=50)



def update():
    global gamestate
    if gamestate == "end":
        if keyboard.RETURN:
            gamestate = "play"
        if keyboard.escape:
            quit()
    if gamestate == "play":
        if keyboard.LEFT:
            Character.x-=Character.xspeed
            Character.image="player_left"
        if keyboard.RIGHT:
            Character.x += Character.xspeed
            Character.image = "player_right"
        if keyboard.UP:
            Character.y -= Character.yspeed
            Character.image = "player_up"
        if keyboard.DOWN:
            Character.y += Character.yspeed
            Character.image = "player_down"a
        if keyboard.escape:
            gamestate="menu"
    if gamestate == "menu":
        if keyboard.RETURN:
            gamestate = "play"




def on_key_down(key):
    global gamestate
    if key==keys.RETURN and gamestate=="start":
        gamestate="play"



pgzrun.go()"""