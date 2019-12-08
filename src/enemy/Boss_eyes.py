from enemy import macro
from Enemy import *
from Player import *
from Bullet import *
import random

class Eyes(Enemy):
    image = "../image/enemy/Boss_eyes.png"
    delay = 20
    change_delay = 150
    speeds = 7
    p_x = 360
    p_y = 70
    o_x = 360
    o_y = 470
    s_x = 360
    s_y = 270

    x_check = True
    y_check = True
    ox_check = False
    oy_check = False

    def __init__(self,x,y,level):
        super().__init__(310,220,1,0,20+level*5,1,100,100)

    def get_image(self):
        return self.image
    
    def eyes_change(self):
        x = self.p_x
        y = self.p_y

        if(x<=160):
            x = 160
            self.x_check = True
        if(x>=560):
            x = 560
            self.x_check = False

        if(self.x_check):
            x += self.speeds
        else:
            x -= self.speeds
        
        if(y<=70):
            y = 70
            self.y_check = True
        if(y>=470):
            y = 470
            self.y_check = False

        if(self.y_check):
            y+= self.speeds
        else:
            y -= self.speeds

        self.p_x = x
        self.p_y = y

        x = self.o_x
        y = self.o_y

        if(x<=160):
            x = 160
            self.ox_check = True
        if(x>=560):
            x = 560
            self.ox_check = False

        if(self.ox_check):
            x += self.speeds
        else:
            x -= self.speeds
        
        if(y<=70):
            y = 70
            self.oy_check = True
        if(y>=470):
            y = 470
            self.oy_check = False

        if(self.oy_check):
            y+= self.speeds
        else:
            y -= self.speeds

        self.o_x = x
        self.o_y = y

    
        

        

    def shot(self,player,b_list):
        self.change_delay -= 1
        if(self.delay>0):
            self.delay -= 1

        else:
            b_list.append(Bullet(self.s_x,self.s_y,self.p_x,self.p_y,4,1))
            b_list.append(Bullet(self.s_x,self.s_y,self.o_x,self.o_y,3,1))
            
            self.eyes_change()

            if(self.change_delay <= 0):
                self.change_delay = random.randrange(101,151)
                self.speeds = random.randrange(5,8)
                



