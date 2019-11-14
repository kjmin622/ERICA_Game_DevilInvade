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
        self.hp = hp
        self.width = width
        self.height = height
        self.damage = damage

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height
    
    def add_hp(self, value):
        self.hp += value
    
    def get_hp(self):
        return self.hp

    def death(self):
        if(self.hp<=0) :
            return True
        else :
            return False

    def body_hit(self, player):

        if(One(self.get_x(),self.get_y(),player.get_x(),player.get_y(),
            self.width, self.height, player.get_width(),player.get_height())):
            player.add_hp(-self.damage)
            return True
        
        return False

    def moving(self, player):
        pass

    def create(self, e_list, b_list, player):
        pass

    def shot(self,player,b_list):
        pass
    


    
 
