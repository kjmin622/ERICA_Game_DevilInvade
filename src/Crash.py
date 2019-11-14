
def One(ax,ay, bx, by, a_width, a_height, b_width, b_height): #1차원, 2차원 충돌
    s_x_l = ax
    s_x_r = ax+a_width

    s_y_l = ay
    s_y_r = ay +a_height
        
    p_x_l = bx
    p_x_r = bx+b_width

    p_y_l = by
    p_y_r = by+b_height

    return s_x_r >= p_x_l and s_x_l <= p_x_r and s_y_r >= p_y_l and s_y_l <= p_y_r

def Where(enemy1, enemy2): #enemy1에 대한 enemy2의 위치
    if(enemy1.get_direction() == 0 or enemy1.get_direction() == 1):
        if(enemy1.get_y()<enemy2.get_y()):
            return 1
        else:
            return 0
    else:
        if(enemy1.get_x()<enemy2.get_x()):
            return 3
        else:
            return 2

def E_bump(enemy1,enemy2):
    if(One(enemy1.get_x(),enemy1.get_y(),enemy2.get_x(),enemy2.get_y(),
        enemy1.get_width(),enemy1.get_height(), enemy2.get_width(), enemy2.get_height())):
            
            d = Where(enemy1,enemy2)
            if d==0 :
                enemy1.set_y(enemy2.get_y()+enemy2.get_height())
            if d==1 :
                enemy1.set_y(enemy2.get_y()-enemy1.get_height())
            if d==2 :
                enemy1.set_x(enemy2.get_x()-enemy1.get_width())
            if d==3 :
                enemy1.set_x(enemy2.get_x()+enemy2.get_width())


def E_bump_list(enemy1,e_list):
    for enemy2 in e_list :
        if(enemy1 == enemy2):
            break
        E_bump(enemy1,enemy2)
