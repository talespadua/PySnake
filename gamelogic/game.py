__author__ = 'tales.cpadua'
import pygame

from gameobjects.snake import Snake
from gameobjects.fruit import Fruit


class Game():
    red = (255, 0, 0)
    black = (0, 0, 0)
    white = (255, 255, 255)
    green = (0, 255, 0)

    def __init__(self, screen_width, screen_height, block_size):
        # init pygame
        pygame.init()

        self.game_over = False

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.block_size = block_size

        # set default font
        self.game_font = pygame.font.SysFont(None, 25)
        self.running = True

        # create display
        self.game_display = pygame.display.set_mode((self.screen_width, self.screen_height))

        # set clock for fps control
        self.clock = pygame.time.Clock()
        self.fps = 15

        # instantiate snake
        self.snake = Snake(self.game_display, self.block_size)

        # instantiate fruit
        self.fruit = Fruit(self.screen_width, self.screen_height, self.block_size)

        # set window name
        pygame.display.set_caption("Snake")

    def main_loop(self):
        while self.running:

            # Handle game over situation
            if self.game_over:
                self.game_over_dialog()

            for event in pygame.event.get():
                # Handle exit through x corner button
                if event.type == pygame.QUIT:
                    self.running = False
                # Handle KeyDown events. Note that it will works with arrows and WASD
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.snake.turn_left()
                        break
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.snake.turn_right()
                        break
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.snake.turn_up()
                        break
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.snake.turn_down()
                        break

                    # handle pause game
                    if event.key == pygame.K_ESCAPE:
                        self.pause_game()

            # execute snake logic
            self.snake.move()
            # Check collision with boundaries
            if self.check_collision():
                self.game_over = True

            #check if eated fruit
            if self.check_fruit_collision():
                self.snake.add_segment()
                self.fruit.respawn(self.screen_width, self.screen_height, self.snake)

            #first you draw, then you update to see changes
            self.game_display.fill(self.white)
            self.draw_fruit(self.fruit)
            self.draw_snake(self.snake)
            pygame.display.flip()
            #set fps
            self.clock.tick(self.fps)

    #this method checks collisions that result in game over
    def check_collision(self):
        if self.snake.segments[0].pos_x < 0 or \
                self.snake.segments[0].pos_x > self.screen_width - self.snake.block_size:
            return True
        if self.snake.segments[0].pos_y < 0 or \
                self.snake.segments[0].pos_y > self.screen_height - self.snake.block_size:
            return True

        #check collision of the snake with itself
        head_pos_x = self.snake.segments[0].pos_x
        head_pos_y = self.snake.segments[0].pos_y
        for s in self.snake.segments[1:]:
            if head_pos_x == s.pos_x and head_pos_y == s.pos_y:
                return True
        return False

    #Check if snake eats fruit
    def check_fruit_collision(self):
        if self.fruit.pos_y == self.snake.segments[0].pos_y and self.fruit.pos_x == self.snake.segments[0].pos_x:
            return True
        return False

    #method for input general messages
    def put_message(self, message):
        pause_text = self.game_font.render(message, True, self.red)
        self.game_display.blit(pause_text, [self.screen_width / 2, self.screen_height / 2])

    # separate method so we can display slightly left from previous method
    def game_over_message(self):
        message = "Game over, press ENTER/SPACE to continue or ESC to quit"
        pause_text = self.game_font.render(message, True, self.red)
        self.game_display.blit(pause_text, [self.screen_width / 5, self.screen_height / 2])

    # handle pause situation
    def pause_game(self):
        paused = True
        self.put_message("Game is Paused")
        pygame.display.update()
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        paused = False
            self.clock.tick(30)

    # Handle game over situation
    def game_over_dialog(self):
        while self.game_over:
            self.game_display.fill(self.white)
            self.game_over_message()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        self.reset_game()
                        return
                    if event.key == pygame.K_ESCAPE:
                        self.exit_game()

    #Reset variables to a new game in case of playing again
    def reset_game(self):
        self.snake.reset_snake()
        self.game_over = False
        self.fruit.respawn(self.screen_width, self.screen_height, self.snake)
        pygame.display.flip()

    #draw snake segments
    def draw_snake(self, snake):
        for s in self.snake.segments:
            self.game_display.fill(self.snake.color, rect=[s.pos_x, s.pos_y, snake.block_size, snake.block_size])

    def draw_fruit(self, fruit):
        self.game_display.fill(self.red, rect=[fruit.pos_x, fruit.pos_y, fruit.block_size, fruit.block_size])

    def exit_game(self):
        pygame.quit()
        quit()