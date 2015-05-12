__author__ = 'tales.cpadua'
from gamelogic.game import Game

def main():
    game = Game(800, 600, 20)
    game.main_loop()

if __name__ == "__main__":
    main()