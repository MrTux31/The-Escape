#!/usr/bin/env python3
# coding:utf-8
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
