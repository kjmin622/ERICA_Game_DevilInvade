from Move import *
from Player import *
from Crash import *

class Enemy(Move):
    hp = 0
    damage = 0
    width = 0
    height = 0

    def __init__(self,x,y,direction,speed,hp,damage,width,height):
        super().__init__(x,y,direction,speed)
        self.width = width
        self.height = height
        self.damage = damage

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height


    def body_hit(self, player):

        if(One(self.get_x(),self.get_y(),player.get_x(),player.get_y(),
            self.width, self.height, player.get_width(),player.get_height())):
            player.add_hp(-self.damage)
            return True
        
        return False
 
