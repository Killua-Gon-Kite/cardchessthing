import pygame as pg
from settings import *

pg.init()
clock = pg.time.Clock()

#Initialize screen
screen = pg.display.set_mode(DISPLAY)
pg.display.set_caption(TITLE)

running = True

while running:
    # Set FPS
    clock.tick(FPS)

    #Check for events
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            running = False
            pg.quit()

    screen.fill(BLACK)
    pg.draw.rect(screen, RED, pg.Rect(WIDTH/2, HEIGHT/2, 64, 64))
    pg.display.flip()
