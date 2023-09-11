#imports
import pygame, sys
from pygame.locals import*
import time
import random

pygame.init()

#set the game screen
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
screen.fill((110, 110, 5))
pygame.display.set_caption('Snake Game')
pygame.display.update()

#Create the snake



#set the events
while True:
    for event in pygame.event.get():
        #set the Quit event
        if event.type == QUIT:
            quit()
