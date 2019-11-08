from Move import *

class Player(Move) :
    max_hp = 10     #최대 체력, 초기값 10
    hp = 10         #체력, 초기값 10
    power = 1       # 공격력, 초기값 1
    at_speed = 1    # 공격속도, 초기값 1
    
    def __init__(self,x,y,direction,speed):
        print("player_init")
        super().__init__(x,y,direction,speed)

    # get_x, get_y, get_direction, get_speed, move, set_x, set_y, set_direction, set_speed
    

    #값 데려오기
    def get_max_hp(self):
        return self.max_hp

    def get_hp(self):
        return self.hp

    def get_power(self):
        return self.power

    def get_as(self):
        return self.at_speed
    
    #값 추가
    def add_hp(self, value):
        self.hp += value
        if(self.hp > self.max_hp) :
            self.hp = self.max_hp
        if(self.hp < 0) :
            self.hp = 0

    def add_max_hp(self, value):
        self.max_hp += value

        if(self.max_hp <= 0):
            self.max_hp = 1

        if(value >= 0):
            self.add_hp(value)

        else:
            self.add_hp(0)

    def add_power(self,value):
        self.power += value

        if(self.power <= 0):
            self.power = 1

    def add_as(self,value):
        self.at_speed += value

        if(self.at_speed <= 0):
            self.at_speed = 1

    def death(self):
        if(self.hp == 0):
            return True
        else:
            return False





