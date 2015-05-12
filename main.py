__author__ = 'tales.cpadua'
import pygame
from snake import Snake
from game import Game

def main():
    game = Game(800, 600, 20)
    game.main_loop()

if __name__ == "__main__":
    main()