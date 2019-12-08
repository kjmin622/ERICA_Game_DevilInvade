from enemy import Mob1
from enemy import Mob2
from enemy import Mob3
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

