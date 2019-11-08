from Move as *
from Player as *

class Enemy(Move):
    hp = 0
    damage = 0
    width = 0
    height = 0

    def __init__(self,x,y,direction,speed,hp,damage):
        super().__init__(x,y,direction,speed)
        self.width = width
        self.height = height
        self.damage = damage

    def body_hit(self, Player):
        s_x = self.get_x() # + self.width
        s_y = self.get_y() # + self.height
        p_x = player.get_x() # +45
        p_y = player.get_y() # +65
        
        #s_x+width>=p_x && s_x<=p_x+45 && s_y<=
        if(s_x>=p_x and s_x+self.width<=p_x+45 and s_y>=p_y and s_y<=p_y+65):
            player.add_hp(-self.damage)
            return True
        
        return False
 
