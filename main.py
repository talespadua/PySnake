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

    # create clock object to control game speed (FPS), and set fps to 15
    # the fps variable can be changed to control game difficulty
    clock = pygame.time.Clock()
    fps = 15

    #call snake object
    snake = Snake(game_display, 300, 300)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    snake.turn_left()
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    snake.turn_right()
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    snake.turn_up()
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    snake.turn_down()

                #handle pause game
                if event.key == pygame.K_ESCAPE:
                    snake.pause()

        #first you draw, then you update to see changes
        game_display.fill(white)
        snake.move()
        snake.render()
        pygame.display.update()

        #set fps
        clock.tick(fps)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()