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
    
    def get_door(self):
        return self.door

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


            
