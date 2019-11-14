from Player import *
import Crash
import math

class Bullet():
    x = 0
    y = 0
    speed = 0
    damage = 0
    x_v = 0
    y_v = 0

    
    def __init__(self,x,y,t_x,t_y,speed,damage):
        self.x = x
        self.y = y
        self.speed = speed
        self.damage = damage
        
        a_x = t_x
        a_y = y
        
        if(t_x==x):
            if(y > t_y):
                self.y_v = -speed
            else:
                self.y_v = speed
        else:
            if(t_x<x):
                speed = -speed
            angle = math.atan((t_y-y)/(t_x-x))
            self.x_v = speed*math.cos(angle) 
            self.y_v = speed*math.sin(angle)
                
    
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def hit_del(self, player):

        s_x = self.get_x()
        s_y = self.get_y()
        p_x = player.get_x() # +45
        p_y = player.get_y() # +65

        if(Crash.One(s_x,s_y,p_x,p_y,10,10,player.get_width(),player.get_height())):
            player.add_hp(-self.damage)
            return True
        
        if(s_x<40 or s_x>680 or s_y<40 or s_y>500):
            return True
        
        self.x += self.x_v
        self.y += self.y_v
        return False

        
