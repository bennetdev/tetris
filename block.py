import pygame as pg
import colors
from random import choice


class Block(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #list for where the large block should have little blocks (see tetris blocks)
        self.little_blocks = [[False, False, False], [False, False, False], [False, False, False]]
        self.generate_little_blocks()

    #method to generate where little blocks should be generated (modify boolean list)
    def generate_little_blocks(self):
        for little_index, littles in enumerate(self.little_blocks):
            for block_index, block in enumerate(littles):
                #random select True or False
                is_block = choice([True, False])
                #replace initial boolean in list
                self.little_blocks[little_index][block_index] = is_block
        print(self.little_blocks)


Block()
