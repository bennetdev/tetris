import pygame as pg
import colors

class Tetris():

    def __init__(self):
        #init pygame
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((700, 500))
        pg.display.set_caption("Tetris")

    def play(self):
        game_running = True

        while game_running:
            #quit game on quit button
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game_running = False
                elif event.type == pg.KEYDOWN:
                    pass
            #config
            self.screen.fill(colors.BLACK)

            pg.display.flip()

            self.clock.tick(60)
        #clean quit
        pg.quit()


Tetris().play()
