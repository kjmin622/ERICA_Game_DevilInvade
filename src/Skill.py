from Player import *
from Enemy import *
from enemy import Mob1
import Crash
class Skill:
    cooltime = 0 # 0이면 사용 가능, 나머지는 쿨타임

    def __init__(self):
        pass
   
    def get_cooltime(self):
        return self.cooltime

    def position(self, player, value):
        if(player.get_direction()==0):
            return [player.get_x(), player.get_y()-value]

        if(player.get_direction()==1):
            return [player.get_x(), player.get_y()+player.get_height()]

        if(player.get_direction()==2):
            return [player.get_x()-value, player.get_y()]

        if(player.get_direction()==3):
            return [player.get_x()+player.get_width(), player.get_y()]


    def attack(self,player,enemy,ww,hh):
        box = self.position(player, 200)
        sx = box[0]
        sy = box[1]
        sw = ww
        sh = hh
            
        ex = enemy.get_x()
        ey = enemy.get_y()
        ew = enemy.get_width()
        eh = enemy.get_height()

        if(Crash.One(sx,sy,ex,ey,sw,sh,ew,eh)):
            return True
        else:
            return False
    
    def cool_1 (self):
        if(self.cooltime>0):
            self.cooltime -= 1
    
    def make_cool_1(self, player):
        self.cooltime = 16 * player.get_as()

    def skill_1 (self, player, enemy):
        
        if(self.cooltime==0):
            if(player.get_direction() == 0 or player.get_direction() == 1):
                if(self.attack(player,enemy,45,200)):
                    enemy.add_hp(-(player.get_power()))
                    return True

            else:
                if(self.attack(player,enemy,200,45)):
                    enemy.add_hp(-(player.get_power()))
                    return True
        return False

