
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

    def move(self, width, height):
        if(self.direction == 0):
            self.y-=self.speed
        if(self.direction == 1):
            self.y+=self.speed
        if(self.direction == 2):
            self.x-=self.speed
        if(self.direction == 3):
            self.x+=self.speed

        if(self.y > 470-height):
            self.y=470-height
        if(self.y < 85-height):
            self.y=85-height
        if(self.x<70):
            self.x=70
        if(self.x>650-width):
            self.x=650-width
    
    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_direction(self, d):
        self.direction = d

    def set_speed(self, s):
        self.speed = s
