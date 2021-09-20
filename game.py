import  pygame
import pytmx
import pyscroll
from player import Player

class Game:

    def __init__(self):
        # générer fenetre du jeu
        self.screen = pygame.display.set_mode((1080,810))
        pygame.display.set_caption("The Escape")

        # charger la map
        tmx_data = pytmx.util_pygame.load_pygame('maps/lobby.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 4

        # générer le joueur
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x, player_position.y)


        # stocker les rectangles de collision
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # générer les calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=2)
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

    #/////////////////////////
    # CHANGEMENT DES MAPS :
    #/////////////////////////

    def switch_map(self):

        # charger la map
        tmx_data = pytmx.util_pygame.load_pygame('maps/map1.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # stocker les rectangles de collision
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # générer les calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=2)
        self.group.add(self.player)

        # définir le rect de collision pour sortir du level 1
        enter_level1 = tmx_data.get_object_by_name("exit_level1")
        self.enter_level1_rect = pygame.Rect(enter_level1.x, enter_level1.y, enter_level1.width, enter_level1.height)

        # récupérer le point de spawn dans le level
        spawn = tmx_data.get_object_by_name('spawn_level1')
        self.player.position[0] = spawn.x + 20
        self.player.position[1] = spawn.y



    def switch_lobby(self):

        # charger la map
        tmx_data = pytmx.util_pygame.load_pygame('maps/lobby.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 4

        # stocker les rectangles de collision
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # générer les calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=2)
        self.group.add(self.player)

        # définir le rect de collision pour entrer dans le level 1
        enter_level1 = tmx_data.get_object_by_name('enter_level1')
        self.enter_level1_rect = pygame.Rect(enter_level1.x, enter_level1.y, enter_level1.width, enter_level1.height)

        # récupérer le point de spawn devant le level
        spawn = tmx_data.get_object_by_name('enter_level1_exit')
        self.player.position[0] = spawn.x
        self.player.position[1] = spawn.y + 20


    def update(self):
        self.group.update()

        # vérifier entrée dans le level 1
        if self.player.feet.colliderect(self.enter_level1_rect):
            self.switch_map()

        # vérifier sortie level 1
        if self.player.feet.colliderect(self.enter_level1_rect):
            self.switch_lobby()

        # vérifier la collision
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back()




    def run(self):

        clock = pygame.time.Clock()
        # boucle
        running = True

        while running:

            self.player.save_location()
            self.handle_input()
            self.update()
            self.group.center(self.player.rect)
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)

        pygame.quit()