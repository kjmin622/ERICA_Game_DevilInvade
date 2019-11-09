from Move import *
from Player import *

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
        s_x_l = self.get_x()
        s_x_r = self.get_x()+self.width

        s_y_l = self.get_y()
        s_y_r = self.get_y()+self.height
        
        p_x_l = player.get_x()
        p_x_r = player.get_x()+45

        p_y_l = player.get_y()
        p_y_r = player.get_y()+65

        '''
        s_x_r >= p_x_l and s_x_l <= p_x_r and s_y_r >= p_y_l and s_y_l <= p_y_r

        '''
        if(s_x_r >= p_x_l and s_x_l <= p_x_r and s_y_r >= p_y_l and s_y_l <= p_y_r):
            player.add_hp(-self.damage)
            return True
        
        return False
 
