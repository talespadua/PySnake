__author__ = 'tales.cpadua'
import pygame
from snake import Snake
from fruit import Fruit

class Game():
    red = (255, 0, 0)
    black = (0, 0, 0)
    white = (255, 255, 255)

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

        #instantiate snake
        self.snake = Snake(self.game_display, self.block_size)

        #instantiate fruit
        self.fruit = Fruit(self.screen_width, self.screen_height, self.block_size)

        #set window name
        pygame.display.set_caption("Snake")

    def main_loop(self):
        while self.running:

            #Handle game over situation
            if self.game_over:
                self.game_over_dialog()

            for event in pygame.event.get():
                #Handle exit through x corner button
                if event.type == pygame.QUIT:
                    self.running = False
                # Handle KeyDown events. Note that it will works with arrows and WASD
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.snake.turn_left()
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.snake.turn_right()
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.snake.turn_up()
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.snake.turn_down()

                    #handle pause game
                    if event.key == pygame.K_ESCAPE:
                        self.pause_game()

            #execute snake logic
            self.snake.move()
            #Check collision with boundaries
            if self.check_collision():
                self.game_over = True

            #first you draw, then you update to see changes
            self.game_display.fill(self.white)
            self.draw_fruit(self.fruit)
            self.draw_snake(self.snake)
            pygame.display.flip()
            #set fps
            self.clock.tick(self.fps)

    def check_collision(self):
        if self.snake.pos_x < 0 or self.snake.pos_x > self.screen_width - self.snake.block_size:
            return True
        if self.snake.pos_y < 0 or self.snake.pos_y > self.screen_height - self.snake.block_size:
            return True
        return False

    def put_message(self, message):
        pause_text = self.game_font.render(message, True, self.red)
        self.game_display.blit(pause_text, [self.screen_width/2, self.screen_height/2])

    #separate method so we can display slightly left from previous method
    def game_over_message(self):
        message = "Game over, press ENTER to continue or ESC to quit"
        pause_text = self.game_font.render(message, True, self.red)
        self.game_display.blit(pause_text, [self.screen_width/4, self.screen_height/2])

    #handle pause situation
    def pause_game(self):
        paused = True
        self.put_message("Game is Paused")
        pygame.display.update()
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        paused = False
            self.clock.tick(30)

    #Handle game over situation
    def game_over_dialog(self):
        while self.game_over:
            self.game_display.fill(self.white)
            self.game_over_message()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.reset_game()
                        return
                    if event.key == pygame.K_ESCAPE:
                        self.exit_game()

    #Reset variables to a new game in case of playing again
    def reset_game(self):
        self.snake.pos_x = 300
        self.snake.pos_y = 300
        self.game_over = False

        self.fruit.reposition(self.screen_width, self.screen_height)
        pygame.display.flip()

    def draw_snake(self, snake):
        #pygame.draw.rect(self.game_display, self.black, [snake.pos_x, snake.pos_y, snake.block_size, snake.block_size])
        self.game_display.fill(self.black, rect=[snake.pos_x, snake.pos_y, snake.block_size, snake.block_size])

    def draw_fruit(self, fruit):
        self.game_display.fill(self.red, rect=[fruit.pos_x, fruit.pos_y, fruit.block_size, fruit.block_size])

    def exit_game(self):
        pygame.quit()
        quit()