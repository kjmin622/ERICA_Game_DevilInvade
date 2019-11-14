from enemy import Mob1
from enemy import Mob2
from enemy import Mob3

def map1() :
    f = False
    t = True
    room = [
            [f,f,f,f,f,f,f,f,f,f,f,f,f],
            [f,f,f,f,f,f,f,f,f,f,f,f,f],
            [f,f,f,f,f,f,f,f,f,f,f,f,f],
            [f,f,f,f,f,f,f,f,f,f,f,f,f],
            [f,f,f,f,f,f,f,f,f,f,f,f,f],
            [f,f,f,f,f,f,f,f,f,f,f,f,f],
            [f,f,f,f,f,f,f,f,f,f,f,f,f],
            [f,f,f,f,f,f,f,f,f,f,f,f,f],
            [f,f,f,f,f,f,f,f,f,f,f,f,f]
            ]

    e_list = []
    e_list.append(Mob3.mob3(300,300))
    e_list.append(Mob2.mob2(200,200))
    e_list.append(Mob1.mob1(250,200))
    return room, e_list

