__author__ = 'tales.cpadua'
import pygame
from snake import Snake

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
        self.fps = 15

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

            #first you draw, then you update to see changes
            self.game_display.fill(self.white)
            if not self.snake.move(self.screen_width, self.screen_height):
                self.running = False
            self.snake.render()
            pygame.display.update()

            #set fps
            self.clock.tick(self.fps)

    def put_pause_message(self):
        pause_text = self.game_font.render("Game Paused", True, self.red)
        self.game_display.blit()


    def exit_game(self):
        pygame.quit()
        quit()