import random


PREVIOUS = [0.1, 0.15, 0.2, 0.25]



class position:
    def __init__(self):
        self.two_row = 6
        self.goalie_row = 4   
        self.two_row_previous = [6]
        self.goalie_row_previous = [4]
        self.percentage = [0.11, 0.11, 0.11,  0.11,  0.11, 0.11,  0.11, 0.11,  0.11]
        self.cross_over_chance = 0.15  # Percentage chance to cross    
        
    def check_crossing(self, two_new, one_new):
        if self.two_row_previous[-1]:
            two_big_prev = (self.two_row_previous[-1] > self.goalie_row_previous[-1])  
            two_big = two_new > one_new    
            
            if (two_big_prev and not two_big):
                return True
            elif (not two_big_prev and two_big):
                return True
            else:
                return False
        else:
            return False
            
    def select_postition(self):
        pass
        
   
    def weighted_choice(self):
        values = range(1,10) 
        choices = zip(values, self.percentage)
        total = sum(w for c, w in choices)
        r = random.uniform(0, total)
        upto = 0
        for c, w in choices:
          if upto + w > r:
             return c
          upto += w
        assert False, "Shouldn't get here"
        
    
        
        
        
     
    
class setting:
    speedSelectChance = .80
    speed = [250, 500]  #speed in MS between steps. Median
    speed_variance = [50, 100]
    cover_previous = PREVIOUS  # Likelyhood to cover previously covered spot (x steps ago)

    
    def get_time_variance(self):
        change_time = []
        if (random.random() < self.speedSelectChance):
            change_time.append(self.speed[0])
            change_time.append(self.speed_variance[0])
        else:
            change_time.append(self.speed[1])
            change_time.append(self.speed_variance[1])
            
        return change_time
    
    
    

class snake(position):
    
    def __init__(self, level):
        position.__init__(self)
        self.level = level
        self.percentages =  [[0.11, 0.11, 0.11,  0.11,  0.11, 0.11,  0.11, 0.11,  0.11],
                        [0.09, 0.11, 0.11,  0.12,  0.13, 0.12,  0.11, 0.11,  0.09],
                        [0.07, 0.11, 0.11,  0.13,  0.15, 0.13,  0.11, 0.11,  0.07],
                        [0.05, 0.11, 0.12,  0.14,  0.15, 0.14,  0.12, 0.11,  0.05],
                        [0.05, 0.08, 0.145, 0.15,  0.15, 0.15,  0.145, 0.08, 0.05],
                        [0.04, 0.06, 0.15,  0.16,  0.17, 0.16,  0.15, 0.06,  0.04],
                        [0.03, 0.03, 0.17,  0.175, 0.18, 0.175, 0.17, 0.03,  0.03],
                        [0.02, 0.02, 0.18,  0.18,  0.19, 0.18,  0.18, 0.02,  0.02],
                        [0.01, 0.01, 0.185, 0.19,  0.2,  0.19,  0.185, 0.01, 0.01],
                        [0,       0, 0.2,   0.2,   0.2,  0.2,   0.2,   0,    0   ]
                        ]
        self.percentage = self.percentages[self.level]
    
    def new_postitions(self):
        position1 = self.weighted_choice()
        position2 = self.weighted_choice()
        #print "Currently: " + str(position1) + " and " + str(position2) 
        if self.check_crossing(position1, position2):
            if random.random() < self.cross_over_chance:
                #print "\nFirst if:"
                #print str(position1) + " and " + str(position2)
                return (position1, position2)
            else:
                #print "\nIn Else clause:" 
                return self.new_postitions()
        else:
            return (position1, position2)
            #print "\nLast ELSE:"
            #print str(position1) + " and " + str(position2)

    def two_space_chance(self):
        if self.level >= 8:
            return False
        else:
            if random.random() < ((10 - self.level)/10):
                return True
            else:
                return False
    

                         
class pull(position):
    
    def __init__(self, level):
        position.__init__(self)
        self.level = level

        self.percentages = [[0, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125],
                            [0.125, 0.14, 0.125, 0.125, 0.125, 0.125, 0.125, 0.11, 0],
                            [0.125, 0.15, 0.145, 0.14, 0.14, 0.125, 0.125, 0.05, 0],
                            [0.1, 0.2, 0.17, 0.17, 0.16, 0.125, 0.05, 0.025, 0],
                            [0.12, 0.2, 0.2, 0.2, 0.145, 0.1, 0.025, 0.01, 0],
                            [0.175, 0.2, 0.2, 0.2, 0.13, 0.07, 0.02, 0.005, 0],
                            [0.2, 0.21, 0.21, 0.21, 0.11, 0.05, 0.01, 0, 0],
                            [0.2, 0.25, 0.21, 0.215, 0.1, 0.025, 0, 0, 0],
                            [0.21, 0.25, 0.25, 0.23, 0.05, 0.0125, 0, 0, 0],
                            [0.19, 0.3, 0.2, 0.3, 0.01, 0, 0, 0, 0]
                           ]
        self.percentage = self.percentages[self.level]
    
    def new_postitions(self):
        position1 = self.weighted_choice()
        position2 = self.weighted_choice()
        
        ### Check to make sure not same (and greater the half space):
        if abs(position1 - position2) <= self.two_space_chance():
            return self.new_postitions()
        
        
        #print "Currently: " + str(position1) + " and " + str(position2) 
        if self.check_crossing(position1, position2):
            if random.random() < self.cross_over_chance:
                #print "\nFirst if:"
                #print str(position1) + " and " + str(position2)
                return (position1, position2)
            else:
                #print "\nIn Else clause:" 
                return self.new_postitions()
        else:
            return (position1, position2)
            #print "\nLast ELSE:"
            #print str(position1) + " and " + str(position2)    
            
            
    def two_space_chance(self):
        if self.level >= 8:
            return 1
        else:
            if random.random() < ((10 - self.level)/10):
                return 2
            else:
                return 1

    
    
    
    
    
    
    




