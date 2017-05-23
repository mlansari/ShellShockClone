import pygame
import logging

print("Finished with imports within init")

# important creations go here

pygame.init()       # initialize all of pygame
logging.basicConfig(filename='errors.log', level=logging.DEBUG) # initialize the log; consider loading logging info from a file?

print("Initialized pygame and set up the logger")

# pull things to the package level
from ShellShockClone import game

print("Got to importing game to the module level")

###########################
### GENERAL NOTES TO ME ###
###########################
# work pythonic, start in one file, and spread outwards as needs grow
# perform some form of run or run setup here

# important to note that, for the sake of segmentation, python has a ConfigParser module that can be used