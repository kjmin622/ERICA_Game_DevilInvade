import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Enemy import *
from Player import *
from math import *

class mob1(Enemy):
    
    image = "../image/enemy/mob_01.png"
     
    def __init__(self,x,y):
        super().__init__(x,y,1,4,10,1,10,10)
    
    def get_image(self):
        return self.image

    def moving(self,player):
        px = player.get_x()+player.get_width()//2
        py = player.get_y()+player.get_height()//2
        mx = super().get_x()+super().get_width()//2
        my = super().get_y()+super().get_height()//2
        
        if(abs(px-mx)>abs(py-my)):
            if(abs(px-mx) > abs(px-(mx+1))):
                super().set_direction(3)
            if(abs(px-mx) > abs(px-(mx-1))):
                super().set_direction(2)
        else:
            if(abs(py-my) > abs(py-(my+1))):
                super().set_direction(1)
            if(abs(py-my) > abs(py-(my-1))):
                super().set_direction(0)

        super().move(super().get_width(), super().get_height())

        

