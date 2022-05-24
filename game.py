from tkinter import W
import pygame as pg
from settings import *


class Game:
    def __init__(self) -> None:
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode(DISPLAY)
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        #Create a new game instance
        self.all_sprites = pg.sprite.Group()
        self.run()

    def run(self):
        #Main game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        #Update
        self.all_sprites.update()

    def events(self):
        # Check for events
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        #Draw sprites and stuff on the screen
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def menu(self):
        #Starting screen
        pass


g = Game()
g.menu()
while g.running:
    g.new()

pg.quit()