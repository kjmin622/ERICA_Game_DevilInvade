from enemy import macro
from Enemy import *
from Player import *
from enemy import Mob3
from Bullet import *
import random
from enemy import Choksu

class kaneki(Enemy):
    image = "../image/enemy/Boss_kaneki.png" #45,90
    delay = 60
    level = 1
    
    def __init__(self,x,y,level):
        super().__init__(x,y,1,0,20+level*5,2,45,90)
        self.level = level

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
            try_ = random.randrange(0,2)
            
            if(try_ == 0):
                self.shoot(player,b_list)

            for i in range(8):
                for j in range(20):
                    rand = random.randrange(0,6)
                    if(rand == 0):
                        e_list.append(Choksu.choksu(70+j*30,i*70,self.level))

            self.delay = random.randrange(40,60)

