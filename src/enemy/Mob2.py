from enemy import macro
from Enemy import *
from Player import *
from enemy import Mob3
from Bullet import *
import random

class mob2(Enemy):

    image = "../image/enemy/mob_02.png"
    delay = 150
    
    def __init__(self,x,y):
        super().__init__(x,y,1,0,6,2,40,40)

    def get_image(self):
        return self.image
    
    def shoot(self, player, b_list):
        s_x = self.get_x() + 20
        s_y = self.get_y() + 20
        arr = [[s_x+500,s_y],[s_x-500,s_y],[s_x,s_y+500],[s_x,s_y-500],
                [s_x+500,s_y+500],[s_x-500,s_y+500],[s_x+500,s_y-500],[s_x-500,s_y-500]]
        for i in arr :
            b_list.append(Bullet(s_x+20,s_y+20,i[0],i[1],8,1))

    def create(self, e_list, b_list, player):
        if(self.delay>0):
            self.delay -= 1
        else:
            try_ = random.randrange(0,3)
            
            if(try_ == 0):
                self.shoot(player,b_list)
            else:
                for i in range(random.randrange(1,2)):
                    e_list.append(Mob3.mob3(self.get_x()+20+i*15,self.get_y()+45))
            
            self.delay = random.randrange(90,120)
