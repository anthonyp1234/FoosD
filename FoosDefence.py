import random
import sys
import pygame

from FoosDefence_class import *
import glob #for listing all the files in a directory

DISPLAY_SIZE = (320,240)


picture_dir = 'images'


## put files into array
picture_files = [["","","","","","","","",""],
                 ["","","","","","","","",""],
                 ["","","","","","","","",""],
                 ["","","","","","","","",""],
                 ["","","","","","","","",""],
                 ["","","","","","","","",""],
                 ["","","","","","","","",""],
                 ["","","","","","","","",""],
                 ["","","","","","","","",""]
                 ]

for i in range(0,9):
    for j in range(0,9):
       filename = picture_dir + r"\{0}_{1}.jpg".format(i, j)
       picture_files[i][j] = glob.glob(filename) 

pygame.init()
screen = pygame.display.set_mode(DISPLAY_SIZE)


def draw_pic(i,j):
    surface_image = pygame.image.load(picture_files[i][j][0])
    surface_image = pygame.transform.scale(surface_image, DISPLAY_SIZE)
    screen.blit(surface_image,(0,0))    ##surface_image.convert(screen)
    pygame.display.flip()
    return True
### SETUP HERE

#for i in range(0,9):
#    for j in range(0,9):
#        print "For {0} - {1}, file is {2}".format(i,j,picture_files[i][j])






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
    player_position.goalie_row_previous.append(value[0])
    player_position.two_row_previous.append(value[1])
    print "{0}:{1}".format(value[0], value[1])
    draw_pic(value[0]-1, value[1]-1)
    
    
    
    
