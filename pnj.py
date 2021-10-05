#!/usr/bin/env python3
# coding:utf-8
import pygame



# Define player class
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        image = read_image('gnome.png', w=32, h=)
        self.image = pg.Surface(image.get_size(), pg.SRCALPHA)
        self.image.blit(image, (0, 0))
        self.rect = self.image.get_rect(topleft=(50, screen.get_height() - TILE_SIZE))
