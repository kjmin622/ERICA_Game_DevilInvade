from enemy import macro
from Enemy import *
from Player import *
from Bullet import *
import random

class choksu(Enemy):

    image1 = "../image/enemy/ground.png"
    image2 = "../image/enemy/choksu.png"
    image = image1
    delay = 30
    level = 1
    
    def __init__(self,x,y,level):
        super().__init__(x,y,0,0,0.1,0,30,70)
        self.level = level

    def get_image(self):
        return self.image

    def add_hp(self,value):
        if(value == 0) : self.hp = 0
  
    def create(self, e_list, b_list, player):
        if(self.delay>12):
            self.delay -= 1

        elif(self.delay>0):
            self.set_damage(1)
            self.image = self.image2
            self.delay -= 1
            
        else:            
            self.add_hp(0)
