__author__ = 'tales.cpadua'
import pygame

class Snake():
    def __init__(self, display, pos_x, pos_y):
        self.color = (0,0,0)
        self.display = display
        self.width = 20
        self.height = 20
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.render()

    def render(self):
        pygame.draw.rect(self.display, self.color, [self.pos_x, self.pos_y, self.width, self.height])

    def move_left(self):
          self.pos_x -= self.width

    def move_right(self):
        self.pos_x += self.width

    def move_up(self):
        self.pos_y -= self.width

    def move_down(self):
        self.pos_y += self.width