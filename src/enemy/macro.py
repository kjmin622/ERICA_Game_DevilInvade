
def MtoP(px,py,mx,my,pw,ph,mw,mh):
    px += pw//2
    py += ph//2
    mx += mw//2
    my += mh//2
        
    if(abs(px-mx)>abs(py-my)):
        if(abs(px-mx) > abs(px-(mx+1))):
            return 3
        if(abs(px-mx) > abs(px-(mx-1))):
            return 2
    else:
        if(abs(py-my) > abs(py-(my+1))):
            return 1
        if(abs(py-my) > abs(py-(my-1))):
            return 0

