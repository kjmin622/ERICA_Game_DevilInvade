from enemy import Mob1
from MapList import *
import random


class Room:
    room = [[]]
    door = [False,False, False,False]
    e_list = []
    map_list = [map1()]

    def __init__(self,in_door):
        self.room, self.e_list = random.choice(self.map_list)
        self.door = in_door

    def get_room(self):
        return self.room
    
    def get_door(self):
        return self.door

    def get_e_list(self):
        return self.e_list



            
