
from enemy import macro
from Enemy import *
from Player import *
from math import *

class mob1(Enemy):
    
    image = "../image/enemy/mob_01.png"
    delay = 5
    move_check = False
     
    def __init__(self,x,y):
        super().__init__(x,y,1,2,3,1,10,10)
    
    def get_image(self):
        return self.image

    def moving(self,player):
        
        if(self.move_check == False and self.delay>0):
            self.delay -= 1

        if(self.move_check == True and self.delay<=8):
            self.delay += 1

        if(self.move_check == True and self.delay>=8):
            super().set_speed(3)
            self.move_check = False

        if(self.move_check == False and self.delay<=0):
            super().set_speed(6)
            self.move_check = True
       
        super().set_direction(macro.MtoP(player.get_x(), player.get_y(), super().get_x(), super().get_y(), 
            player.get_width(), player.get_height(), super().get_width(), super().get_height()))
            
        super().move(super().get_width(), super().get_height())
