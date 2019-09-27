def isLuckyNumber(n):
    for i in (list(map(int,list(str(n))))):
        if ((i == 4) or (i==7)):
            continue
        else:
            return False
    return True
