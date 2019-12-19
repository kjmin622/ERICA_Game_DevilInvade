from enemy import Mob1
from enemy import Mob2
from enemy import Mob3

from enemy import Boss_eyes
from enemy import Boss_ghost
from enemy import Boss_slime

import random

def map1(f_level,level) :
    e_list=[]
    x = int(f_level)
    mari = random.randrange(x,x+4)
    for _ in range(mari):
        num = random.randrange(0,101)
        x = random.randrange(120,601)
        y = random.randrange(120,421)
        if(num < 60):
            e_list.append(Mob1.mob1(x,y,level))
        elif(num < 95):
            e_list.append(Mob3.mob3(x,y,level))
        elif(num <= 100):
            e_list.append(Mob2.mob2(x,y,level))

    return e_list[:]

def boss(f_level) :
    e_list = []
    rand = random.randrange(3)
    if(rand == 0) : e_list.append(Boss_eyes.Eyes(0,0,f_level))
    if(rand == 1) : e_list.append(Boss_ghost.ghost(0,0,f_level))
    if(rand == 2) : e_list.append(Boss_slime.Slime(340,250,f_level))
    return e_list[:]

    
