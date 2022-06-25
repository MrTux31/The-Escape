#!/Python39/python.exe
# coding:utf-8
#import PYTHONHOME=/Python39/python.exe
#import PYTHONPATH=/Python39/python.exe
import pygame
from pygame import locals
import pytmx
import pyscroll
from player import Player
import math
# from pygame.locals import *
# import time

pygame.init()


class Game:

    def __init__(self):
        # générer la fenêtre du jeu
        self.screen = pygame.display.set_mode((1080, 700), locals.RESIZABLE)
        pygame.display.set_caption("The Escape")
        pygame.display.set_icon(pygame.image.load("Sprites/icon.png"))

        # charger la map
        tmx_data = pytmx.util_pygame.load_pygame('maps/lobby.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        self.map_layer.zoom = 4
        self.map = 'lobby'
        self.tmx_data = tmx_data
        self.is_menu_opened = False
        self.is_pnj1_touched = False

        # générer le bouton de sortie
        self.bouton = pygame.image.load('Sprites/exit_button.png').convert_alpha()
        self.bouton.set_colorkey([179, 0, 100])
        self.bouton.set_colorkey([255, 0, 255])
        self.bouton_rect = self.bouton.get_rect()
        self.bouton_rect.x, self.bouton_rect.y = \
            math.ceil(self.screen.get_width() / 2) - 237, math.ceil(self.screen.get_height() / 2) - 65


        # générer le joueur
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x, player_position.y)

        # stocker les rectangles de collision
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # générer les calques
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=2)
        self.group.add(self.player)

        # définir le rect de collision pour entrer dans le level 1
        enter_level1 = tmx_data.get_object_by_name('enter_level1')
        self.enter_level1_rect = pygame.Rect(enter_level1.x, enter_level1.y, enter_level1.width, enter_level1.height)

        # définir le rect de collision pour entrer dans le level 2
        enter_level2 = tmx_data.get_object_by_name('enter_level2')
        self.enter_level2_rect = pygame.Rect(enter_level2.x, enter_level2.y, enter_level2.width, enter_level2.height)

        # définir le rect de collision pour entrer dans le level 3
        enter_level3 = tmx_data.get_object_by_name('enter_level3')
        self.enter_level3_rect = pygame.Rect(enter_level3.x, enter_level3.y, enter_level3.width, enter_level3.height)

        # définir le rect de collision pour entrer dans le level 4
        enter_level4 = tmx_data.get_object_by_name('enter_level4')
        self.enter_level4_rect = pygame.Rect(enter_level4.x, enter_level4.y, enter_level4.width, enter_level4.height)

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
        self.map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        self.map_layer.zoom = 6.6
        self.map = 'map1'
        self.rep1 = 0

        # stocker les rectangles de collision
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # générer les calques
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=2)

        # définir le rect de collision pour sortir du level 1
        enter_level1 = tmx_data.get_object_by_name("exit_level1")
        self.enter_level1_rect = pygame.Rect(enter_level1.x, enter_level1.y, enter_level1.width, enter_level1.height)
        # définir le rect de collision pour placer la bubble

        # récupérer le point de spawn dans le level
        spawn = tmx_data.get_object_by_name('spawn_level1')
        self.player = Player(spawn.x - 9, spawn.y)
        self.group.add(self.player)

    def switch_map2(self):
        self.group = None
        self.player = None

        # charger la map
        tmx_data = pytmx.util_pygame.load_pygame('maps/map2.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        self.map_layer.zoom = 6.6
        self.map = 'map2'
        self.rep1 = 0

        # stocker les rectangles de collision
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # générer les calques
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=2)

        # définir le rect de collision pour sortir du level 2
        enter_level2 = tmx_data.get_object_by_name("exit_level2")
        self.enter_level2_rect = pygame.Rect(enter_level2.x, enter_level2.y, enter_level2.width, enter_level2.height)

        # récupérer le point de spawn dans le level
        spawn = tmx_data.get_object_by_name('spawn_level2')
        self.player = Player(spawn.x - 9, spawn.y)
        self.group.add(self.player)

    def switch_map3(self):
        self.group = None
        self.player = None
        self.rep1 = 0

        # charger la map
        tmx_data = pytmx.util_pygame.load_pygame('maps/map_3.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        self.map_layer.zoom = 4.5
        self.map = 'map3'

        # stocker les rectangles de collision
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # générer les calques
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=3)

        # définir le rect de collision pour sortir du level 1
        enter_level3 = tmx_data.get_object_by_name("exit_level3")
        self.enter_level3_rect = pygame.Rect(enter_level3.x, enter_level3.y, enter_level3.width, enter_level3.height)

        # récupérer le point de spawn dans le level
        spawn = tmx_data.get_object_by_name('spawn_level3')
        self.player = Player(spawn.x - 9, spawn.y)
        self.group.add(self.player)

    def switch_map4(self):
        self.group = None
        self.player = None
        self.rep1 = 0
        self.rep2 = 0

        # charger la map
        tmx_data = pytmx.util_pygame.load_pygame('maps/map4.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        self.map_layer.zoom = 5.5
        self.map = 'map4'

        # stocker les rectangles de collision
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # générer les calques
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=2)

        # définir le rect de collision pour sortir du level 4
        enter_level4 = tmx_data.get_object_by_name("exit_level4")
        self.enter_level4_rect = pygame.Rect(enter_level4.x, enter_level4.y, enter_level4.width, enter_level4.height)

        # récupérer le point de spawn dans le level
        spawn = tmx_data.get_object_by_name('spawn_level4')
        self.player = Player(spawn.x - 9, spawn.y)
        self.group.add(self.player)







    def switch_lobby(self):

        self.group = None
        self.player = None

        # charger la map
        tmx_data = pytmx.util_pygame.load_pygame('maps/lobby.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        self.map_layer.zoom = 4
        self.map = 'lobby'
        self.rep1 = 0
        self.rep2 = 0

        # stocker les rectangles de collision
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # générer les calques
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=2)

        # définir le rect de collision pour entrer dans le level 1
        enter_level1 = tmx_data.get_object_by_name('enter_level1')
        self.enter_level1_rect = pygame.Rect(enter_level1.x, enter_level1.y, enter_level1.width, enter_level1.height)
        # définir le rect de collision pour entrer dans le level2
        enter_level2 = tmx_data.get_object_by_name("enter_level2")
        self.enter_level2_rect = pygame.Rect(enter_level2.x, enter_level2.y, enter_level2.width, enter_level2.height)
        # définir le rect de collision pour entrer dans le level 3
        enter_level3 = tmx_data.get_object_by_name('enter_level3')
        self.enter_level3_rect = pygame.Rect(enter_level3.x, enter_level3.y, enter_level3.width, enter_level3.height)
        # définir le rect de collision pour entrer dans le level 4
        enter_level4 = tmx_data.get_object_by_name('enter_level4')
        self.enter_level4_rect = pygame.Rect(enter_level4.x, enter_level4.y, enter_level4.width, enter_level4.height)


        # récupérer le point de spawn devant le level
        spawn = tmx_data.get_object_by_name('player')
        self.player = Player(spawn.x, spawn.y)
        self.group.add(self.player)
        self.player.change_animations('up')

    def switch_lobby2(self):

        self.group = None
        self.player = None

        # charger la map
        tmx_data = pytmx.util_pygame.load_pygame('maps/lobby.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        self.map_layer.zoom = 4
        self.map = 'lobby'
        self.rep1 = 0
        self.rep2 = 0

        # stocker les rectangles de collision
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # générer les calques
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=2)

        # définir le rect de collision pour entrer dans le level 1
        enter_level1 = tmx_data.get_object_by_name('enter_level1')
        self.enter_level1_rect = pygame.Rect(enter_level1.x, enter_level1.y, enter_level1.width, enter_level1.height)
        # définir le rect de collision pour entrer dans le level 2
        enter_level2 = tmx_data.get_object_by_name("enter_level2")
        self.enter_level2_rect = pygame.Rect(enter_level2.x, enter_level2.y, enter_level2.width, enter_level2.height)
        # définir le rect de collision pour entrer dans le level 3
        enter_level3 = tmx_data.get_object_by_name('enter_level3')
        self.enter_level3_rect = pygame.Rect(enter_level3.x, enter_level3.y, enter_level3.width, enter_level3.height)
        # définir le rect de collision pour entrer dans le level 4
        enter_level4 = tmx_data.get_object_by_name('enter_level4')
        self.enter_level4_rect = pygame.Rect(enter_level4.x, enter_level4.y, enter_level4.width, enter_level4.height)

        # récupérer le point de spawn devant le level
        spawn = tmx_data.get_object_by_name('player')
        self.player = Player(spawn.x, spawn.y)
        self.group.add(self.player)
        self.player.change_animations('up')

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

        # vérifier entrée dans le level 2
        if self.map == 'lobby' and self.player.feet.colliderect(self.enter_level2_rect):
            self.switch_map2()
            self.map = 'map2'

        # vérifier sortie level 2
        if self.map == 'map2' and self.player.feet.colliderect(self.enter_level2_rect):
            self.switch_lobby2()
            self.map = 'lobby'

        # vérifier entrée dans le level 3
        if self.map == 'lobby' and self.player.feet.colliderect(self.enter_level3_rect):
            self.switch_map3()
            self.map = 'map3'

        # vérifier sortie level 3
        if self.map == 'map3' and self.player.feet.colliderect(self.enter_level3_rect):
            self.switch_lobby()
            self.map = 'lobby'

        # vérifier entrée dans le level 4
        if self.map == 'lobby' and self.player.feet.colliderect(self.enter_level4_rect):
            self.switch_map4()
            self.map = 'map4'

        # vérifier sortie level 4
        if self.map == 'map4' and self.player.feet.colliderect(self.enter_level4_rect):
            self.switch_lobby()
            self.map = 'lobby'







        # vérifier la collision
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back()


    def run(self):
        self.map_layer.set_size(self.screen.get_size())

        clock = pygame.time.Clock()
        # boucle
        running = True

        while running:

            if self.is_menu_opened:
                # image_bouton_rect = image_bouton.get_rect()
                self.screen.blit(self.bouton, self.bouton_rect)
                pygame.display.flip()
            else:
                self.player.save_location()
                self.handle_input()
                self.update()
                self.group.center(self.player.rect)

                self.group.draw(self.screen)


                pygame.display.flip()

            for event in pygame.event.get():
                if self.map != 'lobby' and event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.is_menu_opened:
                            self.is_menu_opened = False
                        else:
                            self.is_menu_opened = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.bouton_rect.collidepoint(event.pos) and self.is_menu_opened:
                        self.is_menu_opened = False
                        self.switch_lobby()
                        self.map = 'lobby'
                elif event.type == locals.VIDEORESIZE:
                    width, height = event.size
                    if width < 800:
                        width = 800
                    if height < 600:
                        height = 600
                    self.screen = pygame.display.set_mode((width, height), locals.RESIZABLE)
                    self.map_layer.set_size(self.screen.get_size())
                    self.bouton_rect.x, self.bouton_rect.y = math.ceil(self.screen.get_width() / 2) - 237, math.ceil(
                        self.screen.get_height() / 2) - 65

                if self.is_menu_opened:
                    if pygame.mouse.get_focused():
                        # Trouve position de la souris
                        x, y = pygame.mouse.get_pos()

                        # S'il y a collision:
                        collide = self.bouton_rect.collidepoint(x, y)

                        if collide:
                            self.bouton = None
                            self.bouton = pygame.image.load('Sprites/exit_button2.png').convert_alpha()
                            self.bouton.set_colorkey([255, 0, 255])
                            pygame.display.flip()

                        else:
                            self.bouton = None
                            self.bouton = pygame.image.load('Sprites/exit_button.png').convert_alpha()
                            self.bouton.set_colorkey([255, 0, 255])
                            pygame.display.flip()
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)

        pygame.quit()
