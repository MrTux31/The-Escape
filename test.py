# -*- coding: cp1252 -*-
import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()  ## NE PAS OUBLIEZ

# Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((1600, 900))





# Chargement du bouton (LES 3)
bouton = pygame.image.load("Sprites/exit_button.png").convert_alpha()
bouton_rect = bouton.get_rect()  ## CONNAITRE LE RECTANGLE


screen.fill((0, 0, 0))
screen.blit(exit_bouton, (50, 50))




# Rafraichissement
pygame.display.flip()

pygame.quit()