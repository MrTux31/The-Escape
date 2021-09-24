#!/usr/bin/env python3
# coding:utf-8
import pygame
import pytmx
import pyscroll
from player import Player
# from pygame.locals import *
# import time
pygame.init()


class Game:

    def __init__(self):
        # générer la fenêtre du jeu
        self.screen = pygame.display.set_mode((1080, 810), pygame.RESIZABLE)
        pygame.display.set_caption("The Escape")

        # charger la map
        tmx_data = pytmx.util_pygame.load_pygame('maps/lobby.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 4
        self.map = 'lobby'
        self.tmx_data = tmx_data
        self.is_menu_opened = False

        # générer le joueur
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x, player_position.y)

        # stocker les rectangles de collision
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # générer les calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=10)
        self.group.add(self.player)

        # définir le rect de collision pour entrer dans le level 1
        enter_level1 = tmx_data.get_object_by_name('enter_level1')
        self.enter_level1_rect = pygame.Rect(enter_level1.x, enter_level1.y, enter_level1.width, enter_level1.height)

    # détecter les entrées clavier
    def handle_input(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.player.move_up()
            self.player.change_animations('up')
        elif pressed[pygame.K_DOWN]:
            self.player.change_animations('down')
            self.player.move_down()
        elif pressed[pygame.K_LEFT]:
            self.player.change_animations('left')
            self.player.move_left()
        elif pressed[pygame.K_RIGHT]:
            self.player.change_animations('right')
            self.player.move_right()

    # /////////////////////////
    # CHANGEMENT DES MAPS :
    # /////////////////////////

    def switch_map(self):
        self.group = None
        self.player = None

        # charger la map
        tmx_data = pytmx.util_pygame.load_pygame('maps/map1.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 6.6
        self.map = 'map1'

        # stocker les rectangles de collision
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # générer les calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=10)

        # définir le rect de collision pour sortir du level 1
        enter_level1 = tmx_data.get_object_by_name("exit_level1")
        self.enter_level1_rect = pygame.Rect(enter_level1.x, enter_level1.y, enter_level1.width, enter_level1.height)

        # récupérer le point de spawn dans le level
        spawn = tmx_data.get_object_by_name('spawn_level1')
        self.player = Player(spawn.x - 9, spawn.y)
        self.group.add(self.player)

    def switch_lobby(self):

        self.group = None
        self.player = None

        # charger la map
        tmx_data = pytmx.util_pygame.load_pygame('maps/lobby.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 4
        self.map = 'lobby'

        # stocker les rectangles de collision
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # générer les calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=10)

        # définir le rect de collision pour entrer dans le level 1
        enter_level1 = tmx_data.get_object_by_name('enter_level1')
        self.enter_level1_rect = pygame.Rect(enter_level1.x, enter_level1.y, enter_level1.width, enter_level1.height)

        # récupérer le point de spawn devant le level
        spawn = tmx_data.get_object_by_name('enter_level1_exit')
        self.player = Player(spawn.x, spawn.y)
        self.group.add(self.player)
        self.player.change_animations('down')

    def update(self):
        self.group.update()

        # vérifier entrée dans le level 1
        if self.map == 'lobby' and self.player.feet.colliderect(self.enter_level1_rect):
            self.switch_map()
            self.map = 'map1'

        # vérifier sortie level 1
        if self.map == 'map1' and self.player.feet.colliderect(self.enter_level1_rect):
            self.switch_lobby()
            self.map = 'lobby'

        # vérifier la collision
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back()

    def run(self):

        clock = pygame.time.Clock()
        # boucle
        running = True

        while running:

            if self.is_menu_opened:
                # générer le bouton de sortie
                image_bouton = pygame.image.load('Sprites/exit_button.png').convert_alpha()
                image_bouton.set_colorkey([255, 0, 255])
                image_bouton.set_colorkey([179, 0, 100])

                # image_bouton_rect = image_bouton.get_rect()
                self.screen.blit(image_bouton, (300, 300))
                pygame.display.flip()
            else:
                self.player.save_location()
                self.handle_input()
                self.update()
                self.group.center(self.player.rect)
                self.group.draw(self.screen)
                pygame.display.flip()

            for event in pygame.event.get():
                if self.map == 'map1' and event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.is_menu_opened:
                            self.is_menu_opened = False
                        else:
                            self.is_menu_opened = True

                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)

        pygame.quit()
