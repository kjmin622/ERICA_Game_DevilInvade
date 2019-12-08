from Map import *
import random

def FloorInit(arr):
        queue = []
        arr[2][2] = True
        count = 1
        check = arr
        queue.append([2,2]) 
        direction = [[1,0],[-1,0],[0,1],[0,-1]]

        while(queue):
            for d in direction:
                i = queue[0][0] + d[0]
                j = queue[0][1] + d[1]
                if(i<0 or i>=5 or j<0 or j>=6):
                    continue

                if(check[i][j]==True):
                    continue
                check[i][j] == True

                if(random.randrange(0,100001)>20000):
                    continue
                
                queue.append([i,j])
                arr[i][j] = True
            if(counter(arr) >= 10):
                break
            del queue[0]

        return arr

def counter(arr):
    count = 0
    for i in range(5):
        for k in range(6):
            if arr[i][k] :
                count+=1
    return count

def painter(arr,x):
    check = False
    if(not arr[0]):
        check = True

    for i in range(5):
        for k in range(6):
            if check:
                arr[i].append(x)
            arr[i][k] = x
            

def boxcheck(arr):
    for i in range(4):
        for k in range(5):
            if(arr[i][k] and arr[i][k+1] and arr[i+1][k] and arr[i+1][k+1]):
                return True
    return False

def bosscheck(arr):
    bossroom=[]
    for i in range(5):
        for k in range(6):
            count =0
            if([i,k]!=[2,2] and arr[i][k]):
                direction = [[1,0],[-1,0],[0,1],[0,-1]]
                for d in direction:
                    a = i + d[0]
                    b = k + d[1]
                    if(a<0 or a>=5 or b<0 or b>=6):
                        continue
                    
                    if(arr[a][b]):
                        count += 1
                if(count==1):
                    bossroom.append([i,k])                
    return bossroom


def doorcheck(arr, i, j):
    door = [False, False, False, False]
    if(i-1>=0 and arr[i-1][j] == True):door[0]=True
    if(i+1<5 and arr[i+1][j] == True):door[1]=True
    if(j-1>=0 and arr[i][j-1] == True):door[2]=True
    if(j+1<6 and arr[i][j+1] == True):door[3]=True
    return door



############################################
class Floor:
    floor_init=[[],[],[],[],[]] # 각 리스트의 최대 길이는 6, 방 있으면 True
    floor_room=[[],[],[],[],[]] # 각 리스트의 최대 길이는 6, foor_init에서 True의 자리에 room객체 생성 
    
    player_position = [2,2]
    
    boss_position = []
    '''
    random.choice([1,2...])  : [] 리스트에 있는 것중 하나 선택

    arr = [[],[]]  만약에 0번째 배열에 3이란 숫자를 넣고 싶다!  카면은 arr[0].append(3)
    다만, 이걸 쓰면 안되는게 우리가 하려 했던게, 한 점을 찍고 상하좌우로 가야하니까, 애초에 위에서 그걸 해줘야하는데 그게 뭐냐면 
    0 빈방
    1 시작 
    2 몹
    3 보스
    4 이벤트!!
    '''
    def __init__(self):
        arr = [[],[],[],[],[]]

        count = 0
        painter(arr,False) # 모든 방 False 로 

        done_map = True
        while(done_map):
            while(count<8 or boxcheck(arr)): 
                painter(arr,False) 
                arr = FloorInit(arr) # 방 가져오기
                count = counter(arr) # True 개수
            self.floor_init = arr # 방 가져오기
            bosscheck_arr = bosscheck(self.floor_init) #보스방 후보들
            if(bosscheck_arr):
                bossroom_position = random.choice(bosscheck_arr) #보스방 뽑기
                done_map = False

        arr2 = [[],[],[],[],[]]



# 방을 표현해보아요

        painter(arr2,0) #모든 방 0으로 표현
        for i in range(5):
            for k in range(6):
                if self.floor_init[i][k] :
                    arr2[i][k] = Room(doorcheck(self.floor_init,i,k)) #
        
        self.boss_position = [bossroom_position[0],bossroom_position[1]] #보스방 설정
        self.floor_room = arr2

    def get_map(self):
        return self.floor_init

    def get_where(self):
        return self.player_position

    def get_bossRoom(self):
        return self.boss_position

    def get_room(self):
        return self.floor_room[self.player_position[0]][self.player_position[1]]

    def get_room_position(self,i,k):
        return self.floor_room[i][k]

    def map_move(self, where, player):
        i = self.player_position[0]
        j = self.player_position[1]
        
        if(where == 0):
            i-=1
            player.set_y(395)

        elif(where == 1):
            i+=1
            player.set_y(80)

        elif(where == 2):
            j-=1
            player.set_x(555)

        elif(where == 3):
            j+=1
            player.set_x(80)

        else:pass

        self.player_position = [i,j]

        return self.get_room()
    
    def bossRoom(self):
        return self.player_position == self.boss_position

