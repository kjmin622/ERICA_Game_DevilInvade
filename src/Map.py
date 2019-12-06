from enemy import Mob1
from enemy import Mob2
from enemy import Mob3
from MapList import *
import random
import Crash
from Player import *


class Room:
    door = [False,False, False,False]
    elist = []
    e_list = []
    visited = False

    def __init__(self,in_door):
        self.door = in_door
    
    def get_door(self):
        return self.door

    def visit(self):
        self.visited = True

    def create_enemy(self):
        return not self.visited

    def enter_door(self, player,e_list):
        if(e_list):
            return -1

        d0 = [300,70]
        d2 = [70,200]
        d1 = [300,450]
        d3 = [650,200]

       
        if(Crash.One(player.get_x(), player.get_y(), d0[0], d0[1], player.get_width(), player.get_height(), 50,0)
                and self.door[0]):
            return 0

        if(Crash.One(player.get_x(), player.get_y(), d1[0], d1[1], player.get_width(), player.get_height(), 50,0)
                and self.door[1]):
            return 1
    
        if(Crash.One(player.get_x(), player.get_y(), d2[0], d2[1], player.get_width(), player.get_height(), 0,50)
                and self.door[2]):
            return 2

        if(Crash.One(player.get_x(), player.get_y(), d3[0], d3[1], player.get_width(), player.get_height(), 0,50)
                and self.door[3]):
            return 3
        
        return -1









            
