# Primary game file
import sys, pygame
from pygame.locals import *

display_surf = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hello Pygame World!')

def run():
    """This allows for the running of the game from outside the package"""
    print("Started trying to run")
    # main game loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()