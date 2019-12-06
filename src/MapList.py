from enemy import Mob1
from enemy import Mob2
from enemy import Mob3
import random

def map1(x) :
    e_list=[]
    mari = random.randrange(x,x+4)
    for _ in range(mari):
        num = random.randrange(0,101)
        x = random.randrange(120,601)
        y = random.randrange(120,421)
        if(num < 60):
            e_list.append(Mob1.mob1(x,y))
        elif(num < 95):
            e_list.append(Mob3.mob3(x,y))
        elif(num <= 100):
            e_list.append(Mob2.mob2(x,y))

    return e_list[:]

