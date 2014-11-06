import random

POSITIONS = 9  #  9 postitions if using half spaces. 5 is middle

PREVIOUS = [0.1, 0.15, 0.2, 0.25]



class position:
    two_row = 6
    goalie_row = 4   
    two_row_previous = []
    goalie_row_previous = []
    
    def check_crossing(self):
        if self.two_row_previous[-1]:
            two_big_prev = (self.two_row_previous[-1] > self.goalie_row_previous[-1])  
            one_big_prev = (self.two_row_previous[-1] < self.goalie_row_previous[-1])
            two_big = self.two_row > self.goalie_row
            one_big = self.goalie_row < self.two_row
            
            if (two_big_prev and not two_big):
                return true
            elif (not two_big_prev and two_big):
                return true
            else:
                return false
        else:
            return false
            
    def select_postition(self):
        pass
    
    def weighted_choice(self,snake_percentages):
        values = range(1,10) 
        choices = zip(values, snake_percentages)
        total = sum(w for c, w in choices)
        r = random.uniform(0, total)
        upto = 0
        for c, w in choices:
          if upto + w > r:
             return c
          upto += w
        assert False, "Shouldn't get here"
     
    
class setting:
    defence_type = ""
    speedSelectChance = .80
    speed = [250, 500]  #speed in MS between steps. Median
    speed_variance = [50, 100]
    cover_previous = PREVIOUS  # Likelyhood to cover previously covered spot (x steps ago)
    cross_over_chance = 0.15  # Percentage chance to cross
    
    def get_time_variance(self):
        change_time = []
        if (random.random() < self.speedSelectChance):
            change_time.append(self.speed[0])
            change_time.append(self.speed_variance[0])
        else:
            change_time.append(self.speed[1])
            change_time.append(self.speed_variance[1])
            
        return change_time
    
    
    

class snake(setting):
    
    snake_percentages =  [[0.11, 0.11, 0.11,  0.11,  0.11, 0.11,  0.11, 0.11,  0.11],
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
    
    median = (POSITIONS)/2
    stddev = ""
    
    
    
    
    
    
    




