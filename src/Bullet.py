from Move import *
from Player import *

class Bullet(Move):
    damage = 0
    radius = 8

    
    def __init__(self,x,y,direction,speed,damage):
        super().__init__(x,y,direction,speed)
        self.damage = damage


    def hit_del(self,player): #player 45 * 65
        s_x = self.get_x()
        s_y = self.get_y()
        p_x = player.get_x() # +45
        p_y = player.get_y() # +65

        if(s_x>=p_x and s_x<=p_x+45 and s_y>=p_y and s_y<=p_y+65):
            player.add_hp(-self.damage)
            print("hit",self.damage)
            return True

        if(s_x<0 and s_x>720 and s_y<0 and s_y>540):
            return True
        return False
        


        
