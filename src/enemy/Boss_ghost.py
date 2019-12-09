from enemy import macro
from Enemy import *
from Bullet import *
import random

class ghost(Enemy):
    image = "../image/enemy/Boss_ghost.png"
    delay = 40
    check = False
    
    def __init__(self,x,y,level):
        super().__init__(random.randrange(70,500),random.randrange(70,450),3,30,20+level*5,1,60,25)

    def get_image(self):
        return self.image

    def moving(self,player):
        if(self.get_x() >= 720):
            self.set_x(-60)
            self.set_y(random.randrange(80,450))
            
            if(not self.check and random.randrange(0,5)==4):
                self.check = True
            else:
                self.check = False

        self.set_x(self.get_x()+self.get_speed())

    def shot(self,player,b_list):
        if(self.delay>0):
            self.delay -= 1

        elif(self.check) :
            x = self.get_x()
            y = self.get_y()
            b_list.append(Bullet(x,y,x,y+200,5,1))
            b_list.append(Bullet(x,y,x,y-200,5,1))
            self.delay = 3


