__author__ = 'tales.cpadua'
import pygame

class Snake():
    def __init__(self, display, block_size, pos_x=300, pos_y=300):
        self.color = (0,0,0)
        self.display = display
        self.block_size = block_size
        self.x_velocity = 0
        self.y_velocity = (-1)*self.block_size
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.render()
        self.paused = False
        self.prev_x_vel = 0
        self.prev_y_vel = 0

    def render(self):
        pygame.draw.rect(self.display, self.color, [self.pos_x, self.pos_y, self.block_size, self.block_size])

    # To turn, we keep velocity variables for x and y direction, and then we sum it to the position
    # The snake will be always moving, so the event handler will only change the movement direction
    # The snake cannot go directly to the opposite direction. The first if of these methods assure this
    def turn_left(self):
        if self.paused:
            return
        elif self.x_velocity > 0:
            return
        self.x_velocity = (-1)*self.block_size
        self.y_velocity = 0

    def turn_right(self):
        if self.paused:
            return
        elif self.x_velocity < 0:
            return
        self.x_velocity = self.block_size
        self.y_velocity = 0

    def turn_up(self):
        if self.paused:
            return
        elif self.y_velocity > 0:
            return
        self.y_velocity = (-1)*self.block_size
        self.x_velocity = 0

    def turn_down(self):
        if self.paused:
            return
        elif self.y_velocity < 0:
            return
        self.y_velocity = self.block_size
        self.x_velocity = 0

    # Here we sum the velocity to the position. Note that negative values will decrease the position value, since
    # sum negative number is the same as subtracting a positive one
    def move(self):
        self.pos_x += self.x_velocity
        self.pos_y += self.y_velocity