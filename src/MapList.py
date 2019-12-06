from enemy import Mob1
from enemy import Mob2
from enemy import Mob3
import random

def map1(x) :
    e_list=[]
    e = [Mob1.mob1, Mob2.mob2, Mob3.mob3]
    #print("init")
    for i in range(13):
        for k in range(18):
            num = random.randrange(0,x)
            if(num < 10):
                #print(i,k)
                e_list.append(Mob1.mob1(70+k*25, 70+i*29))
            elif(num==10):
                e_list.append(Mob2.mob2(70+k*25, 70+i*29))
            elif(num<13):
                e_list.append(Mob3.mob3(70+k*25, 70+i*29))

    return e_list[:]

