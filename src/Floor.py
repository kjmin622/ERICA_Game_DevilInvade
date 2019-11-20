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

                if(random.choice([True,True,False])):
                    continue
                
                queue.append([i,j])
                arr[i][j] = True
                count += 1
            if(count>10):
                break
            del queue[0]

        return arr, count

class Floor:
    floor_init=[[],[],[],[],[]] # 각 리스트의 최대 길이는 6, 방 있으면 True
    floor_room=[[],[],[],[],[]] # 각 리스트의 최대 길이는 6, foor_init에서 True의 자리에 room객체 생성 
    
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
        for i in range(5):
            for k in range(6):
                arr[i].append(False)

        arr, count = FloorInit(arr)

        while(count<6):
            arr, count = FloorInit(arr)

        for i in range(5):
            for k in range(6):
                if(arr[i][k]):
                    print('@',end="")
                else:
                    print(' ',end="")
            print('')

    
                

floor = Floor()



