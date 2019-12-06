from enemy import macro
from Enemy import *
from Player import *
from Bullet import *
import random

class mob3(Enemy):

    image = "../image/enemy/mob_02_bullet.png"
    delay = 60
    
    def __init__(self,x,y):
        super().__init__(x,y,1,3,4,1,30,20)

    def get_image(self):
        return self.image

    def moving(self,player):
        self.set_direction(random.randrange(0,4))
        super().move(super().get_width(), super().get_height())

    def shot(self,player,b_list):
        if(self.delay>0):
            self.delay -= 1
        
        else:
            p_x = player.get_x()
            p_y = player.get_y()
            s_x = self.get_x()
            s_y = self.get_y()
            d = 0
            if(p_x < p_y):
                if(p_x - s_x > 0):
                    d = 3
                else:
                    d = 2
            else:
                if(p_y - s_y > 0):
                    d = 1
                else:
                    d = 0
            
            b_list.append(Bullet(s_x,s_y,p_x+22.5,p_y+30,10,1))
            self.delay = 50


    
