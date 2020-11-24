import pygame
from pygame.locals import *
import sys

##########################
# Importing files to main
##########################



##########################
# Global Variables
##########################

pygame.init()
pygame.font.init()
CLOCK = pygame.time.Clock()
SCREENWIDTH, SCREENHEIGHT = 1650, 1000
WIN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

##########################
# Helper Functions
##########################

def redrawGameWindow():
    WIN.fill((255, 255, 255))
    pygame.display.update()

##########################
# Main Function
##########################

def main():
    pygame.display.set_caption("Sorting Algorithm Visualizer")
    while True:
        CLOCK.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        redrawGameWindow()

main()