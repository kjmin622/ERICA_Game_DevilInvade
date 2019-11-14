from enemy import macro
from Enemy import *
from Player import *
from enemy import Mob3
import random

class mob2(Enemy):

    image = "../image/enemy/mob_02.png"
    delay = 150
    
    def __init__(self,x,y):
        super().__init__(x,y,1,0,15,2,40,40)

    def get_image(self):
        return self.image

    def create(self, e_list):
        if(self.delay>0):
            self.delay -= 1
        else:
            for i in range(random.randrange(1,2)):
                e_list.append(Mob3.mob3(self.get_x()+20+i*15,self.get_y()+45))
            self.delay = random.randrange(90,120)
