def lateRide(n):
    a = n%60
    b = (n-a)/60
    return sum(list(map(int,list(str(a))+list(str(round(b))))))
