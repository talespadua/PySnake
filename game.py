__author__ = 'tales.cpadua'
import pygame
from snake import Snake
import time

class Game():
    red = (255, 0, 0)
    black = (0, 0, 0)
    white = (255, 255, 255)

    def __init__(self, screen_width, screen_height):
        # init pygame
        pygame.init()

        self.screen_width = screen_width
        self.screen_height = screen_height

        # set default font
        self.game_font = pygame.font.SysFont(None, 25)
        self.running = True

        # create display
        self.game_display = pygame.display.set_mode((self.screen_width, self.screen_height))

        # set clock for fps control
        self.clock = pygame.time.Clock()
        self.fps = 20

        #instantiate snake
        self.snake = Snake(self.game_display)

        #set window name
        pygame.display.set_caption("Snake")

    def main_loop(self):
        pygame.display.update()
        while self.running:
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
                        self.snake.pause()
                        #self.pause_game()

            #first you draw, then you update to see changes
            self.game_display.fill(self.white)
            self.snake.move()
            #Check collision with boundaries
            if self.check_collision():
                self.put_message("You lose")
                time.sleep(2)
                self.exit_game()

            self.snake.render()
            pygame.display.update()
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
        pygame.display.update()

    def pause_game(self):
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        paused = False
            self.clock.tick(30)


    def exit_game(self):
        pygame.quit()
        quit()