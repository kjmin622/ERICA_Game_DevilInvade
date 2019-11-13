from enemy import Mob1

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
    e_list.append(Mob1.mob1(200,200))
    e_list.append(Mob1.mob1(230,230))

    return room, e_list

