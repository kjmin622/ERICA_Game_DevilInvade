import Crash
import Player

class Heart():
    x=0
    y=0
    width=30
    height=30

    def __init__(self,x,y):
        self.x=x
        self.y=y
   
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def heart_crash(self,player):
        if(Crash.One(self.x,self.y,player.get_x(), player.get_y(), 
            self.width, self.height, player.get_width(), player.get_height())):

            player.add_hp(1)
            return True
        return False
