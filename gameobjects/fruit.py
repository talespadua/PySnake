__author__ = 'tales.cpadua'

import random

class Fruit:
    def __init__(self, screen_width, screen_height, block_size):
        self.block_size = block_size
        self.pos_x = random.randrange(0, screen_width, self.block_size)
        self.pos_y = random.randrange(0, screen_height, self.block_size)

    def reposition(self, screen_width, screen_height):
        self.pos_x = random.randrange(0, screen_width, self.block_size)
        self.pos_y = random.randrange(0, screen_height, self.block_size)