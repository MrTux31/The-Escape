#!/Python39/python.exe
# coding:utf-8
#import PYTHONHOME=/Python39/python.exe
#import PYTHONPATH=/Python39/python.exe
import pygame
from game import Game
from pygame import mixer

if __name__ == '__main__':
    pygame.init()
    # jouer la musique en boucle
    mixer.music.load('Songs/The Escape Official Theme Song.ogg ')
    mixer.music.play(-1)
    game = Game()
    game.run()
