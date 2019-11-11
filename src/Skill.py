from Player as *

class Skill:
    skill_lv = [1,0,0,0] #일반공격, 힐, 투사체 , 마치 제라스 궁
    cooltime = [0,0,0,0] # 0이면 사용 가능, 나머지는 쿨타임

    def __init__(self):
        pass

    def skill_up(self,n):
        skill_lv[n] += 1

    def skill_1 (self, player):
        direction = player.get_direction()
        x = player.get_x()
        y = player.get_y()
