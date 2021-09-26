# -*- coding: cp1252 -*-
import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()  ## NE PAS OUBLIEZ

# Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((1600, 900))

## Chargement du SysFont
font = pygame.font.SysFont('helvetic', 70)

# Nommer la page
pygame.display.set_caption("Menu jeu")



# Chargement du bouton (LES 3)
bouton = pygame.image.load("Sprites/exit_button.png").convert_alpha()
bouton_rect = bouton.get_rect()  ## CONNAITRE LE RECTANGLE

continuer = 1
TEXT = 'Rien..'


def gerer_event():
    global continuer, TEXT
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0

    ## Si le focus est sur la fenêtre.
    if pygame.mouse.get_focused():
        ## Trouve position de la souris
        x, y = pygame.mouse.get_pos()

        ## S'il y a collision:
        collide = bouton_rect.collidepoint(x, y)

        if collide:
            bouton = pygame.image.load('Sprites/exit_button2.png').convert_alpha()
            bouton.set_colorkey([255, 0, 255])
            pygame.display.flip()
            print('dessus')

        else:
            bouton = pygame.image.load('Sprites/exit_button.png').convert_alpha()
            bouton.set_colorkey([255, 0, 255])
            pygame.display.flip()
            print("a coté")


        ## Détecte les clique de souris.
        pressed = pygame.mouse.get_pressed()
        if pressed[0]:  # 0=gauche, 1=milieu, 2=droite
            continuer = 0


while continuer:
    fenetre.fill((0, 0, 0))
    fenetre.blit(bouton, (50, 50))

    text = font.render(TEXT, 1, (255, 255, 255))
    fenetre.blit(text, (50, 500))

    ## Gérer les événements.
    gerer_event()

    # Rafraichissement
    pygame.display.flip()

pygame.quit()