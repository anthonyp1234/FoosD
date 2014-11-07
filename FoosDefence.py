import random
import sys
import pygame

from FoosDefence_class import *

##import object files here?


# Some constants:
# Snake Constants

       
### SETUP HERE

clock = pygame.time


level_select = int(raw_input("\n\nPlease select a level skill from 0 - 9, 0 is best, 9 is worst: ")) 

if not level_select in range(0,9):
    print "Not in Range"
    sys.exit()

type_select = int(raw_input("\nPlease select a style from:\n1) Snake, \n2) Pull\nCHOICE: "))    

if not type_select in range(1,3):
    print "Not in Range"
    sys.exit()         

if type_select == 1:    
    player_position = snake(level_select) 
else:
    player_position = pull(level_select)
    
settings = setting()        

while True:
    ### Do the stuff in here
    #import pdb; pdb.set_trace()
    ##Wait random amount of time
    #print "\n\n############################New Round"
    time_value = settings.get_time_variance()
    waiting_time = random.gauss(time_value[0], time_value[1])
    #print waiting_time
    clock.delay(int(round(waiting_time)))
    #print "Move"
    value = player_position.new_postitions()
    print "{0}:{1}".format(value[0], value[1])
    
    
    
