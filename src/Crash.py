
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
