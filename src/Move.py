
class Move:
    speed = 1 #이동속도 초기값
    direction = 0 #방향, 위:0  아래:1  좌:2 오른쪽:3
    x = 0 #x축 위치
    y = 0 #y축 위치

    def __init__(self, x,y,direction,speed):
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = speed

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_direction(self):
        return self.direction

    def get_speed(self):
        return self.speed

    def move(self):
        if(self.direction == 0):
            self.y-=self.speed
        if(self.direction == 1):
            self.y+=self.speed
        if(self.direction == 2):
            self.x-=self.speed
        if(self.direction == 3):
            self.x+=self.speed

        if(self.y > 410): #추후 인터페이스 조정할 때 같이 조정해야 함  
            self.y=410
        if(self.y < 10):
            self.y=10
        if(self.x<70):
            self.x=70
        if(self.x>620):
            self.x=620

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_direction(self, d):
        self.direction = d

    def set_speed(self, s):
        self.speed = s
