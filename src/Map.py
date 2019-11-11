'''
1. rock-secret room
2. 
'''
class Room:
    room = [[]]
    door = [False,False, False,False]

    def __init__(self,in_door,room):
        self.room = room
        self.door = in_door

    def get_room(self):
        return self.room


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

    return room

ro = Room([True,True,True,True],map1())
print(ro.get_room())





            
