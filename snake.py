__author__ = 'tales.cpadua'
import pygame

class Snake():
    def __init__(self, display, pos_x, pos_y):
        self.color = (0,0,0)
        self.display = display
        self.width = 20
        self.height = 20
        self.x_velocity = 0
        self.y_velocity = (-1)*self.width
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.render()

    def render(self):
        pygame.draw.rect(self.display, self.color, [self.pos_x, self.pos_y, self.width, self.height])

    # To turn, we keep velocity variables for x and y direction, and then we sum it to the position
    # The snake will be always moving, so the event handler will only change the movement direction
    def turn_left(self):
        self.x_velocity = (-1)*self.width
        self.y_velocity = 0

    def turn_right(self):
        self.x_velocity = self.width
        self.y_velocity = 0

    def turn_up(self):
        self.y_velocity = (-1)*self.width
        self.x_velocity = 0

    def turn_down(self):
        self.y_velocity = self.width
        self.x_velocity = 0

    # Here we sum the velocity to the position. Note that negative values will decrease the position value, since
    # sum negative number is the same as subtracting a positive one
    def move(self):
        self.pos_x += self.x_velocity
        self.pos_y += self.y_velocity