import random
import sys
import pygame

from FoosDefence_class import *

##import object files here?


# Some constants:
# Snake Constants

       
### SETUP HERE

clock = pygame.time


level_select = int(raw_input("Please select a level skill from 0 - 9, 0 is best, 9 is worst: ")) 

if not level_select in range(0,9):
    print "Not in Range"
    sys.exit()

level_select = int(raw_input("Please select a style from:\n 1) Snake, \n2)Pull\n: "))    

if not level_select in range(1,2):
    print "Not in Range"
    sys.exit()         
    
player_position = position() 
settings = setting()        

while True:
    ### Do the stuff in here
    
    ##Wait random amount of time
    time_value = settings.get_time_variance()
    waiting_time = random.gauss(time_value[0], time_value[1])
    #print waiting_time
    clock.delay(int(round(waiting_time)))
    #print "Move"
    print player_position.weighted_choice(snake_percentages[level_select])
    
    
    
