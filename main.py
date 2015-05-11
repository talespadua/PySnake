__author__ = 'tales.cpadua'
import pygame
from snake import Snake

def main():
    running = True

    #init pygame
    pygame.init()

    #preset color to be used in game
    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)

    #set screen size variables
    screen_width = 800
    screen_height = 600

    #Creating the display
    game_display = pygame.display.set_mode((screen_width, screen_height))
    #set screen name
    pygame.display.set_caption("Snake")
    pygame.display.update()

    #call snake object
    snake = Snake(game_display, 100, 100)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.move_left()
                if event.key == pygame.K_RIGHT:
                    snake.move_right()
                if event.key == pygame.K_UP:
                    snake.move_up()
                if event.key == pygame.K_DOWN:
                    snake.move_down()

        #first you draw, then you update to see changes
        game_display.fill(white)
        snake.render()
        pygame.display.update()
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()