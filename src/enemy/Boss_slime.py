from enemy import macro
from Enemy import *
from Player import *
import Crash
import random

class Slime(Enemy):

    image1 = "../image/enemy/Boss_slime1.png"
    image2 = "../image/enemy/Boss_slime2.png"
    image3 = "../image/enemy/Boss_slime3.png"
    image = ""
    delay = 150
    level = 1
    size = 0
    direction = 1 # 1:우상 2:좌상 3:좌하 4:우하
    
    def __init__(self,x,y,level,size=0, direction=1):
        if(size==0):
            super().__init__(x,y,1,8,10+level*3,1,64,64)
            self.image = self.image1
            self.level = level
            self.size = size
        elif(size==1):
            super().__init__(x,y,1,8,2.3+level*0.5,1,32,32)
            self.image = self.image2
            self.level = level
            self.size = size
            self.direction = direction
        else:
            super().__init__(x,y,1,9,1,1,16,16)
            self.image = self.image3
            self.level = level
            self.size = size
            self.direction = direction

    def moving(self,player):
        x = self.get_x()
        y = self.get_y()
        x_w = self.get_width()
        x_h = self.get_height()

        if(Crash.One(x,y,0,0,x_w,x_h,720,70) or
                Crash.One(x,y,0,470,x_w,x_h,720,70)):
            if(self.direction == 1):self.direction=4
            elif(self.direction == 2):self.direction=3
            elif(self.direction == 3):self.direction=2
            elif(self.direction == 4):self.direction=1
        
        elif(Crash.One(x,y,0,0,x_w,x_h,70,540) or
                Crash.One(x,y,650,0,x_w,x_h,70,540)):

            if(self.direction == 1):self.direction=2
            elif(self.direction == 2):self.direction=1
            elif(self.direction == 3):self.direction=4
            elif(self.direction == 4):self.direction=3


        if(self.direction == 1):
            self.set_x(x+self.get_speed())
            self.set_y(y-self.get_speed())

        if(self.direction == 2):
            self.set_x(x-self.get_speed())
            self.set_y(y-self.get_speed())

        if(self.direction == 3):
            self.set_x(x-self.get_speed())
            self.set_y(y+self.get_speed())

        if(self.direction == 4):
            self.set_x(x+self.get_speed())
            self.set_y(y+self.get_speed())

    
    def get_image(self):
        return self.image

    def create(self, e_list, b_list, player):
        
        if(self.get_hp() <= 0):
            x = self.get_x()
            y = self.get_y()
            if(self.size==0):
                e_list.append(Slime(x+32,y,self.level,1,1)) 
                e_list.append(Slime(x,y+32,self.level,1,3))
                e_list.append(Slime(x+32,y+32,self.level,1,4)) 
                e_list.append(Slime(x,y,self.level,1,2))
                
            if(self.size==1):
                e_list.append(Slime(x+16,y,self.level,2,1))
                e_list.append(Slime(x,y,self.level,2,2))
                e_list.append(Slime(x,y+16,self.level,2,3))
                e_list.append(Slime(x+16,y+16,self.level,2,4))

