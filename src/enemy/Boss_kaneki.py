from enemy import macro
from Enemy import *
from Player import *
from enemy import Mob3
from Bullet import *
import random
class kaneki(enemy){
    image = "../image/enemy/Boss_kaneki.png" #45,90
    delay = 60
    level = 1
    
    def __init__(self,x,y,level):
        super().__init__(x,y,1,0,6+level*1.40,2,45,90)
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

            else:
                for i in range(random.randrange(8)):
                    for j in range(random.randrange(20)):
                        e_list.append(choksu.choksu(70+j*30,70+i*70))

            self.delay = random.randrange(30,60)

