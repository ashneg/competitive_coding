def shapeArea(n):
    area = 0
    for i in range(n-1):
        area += i*2 +1
    return (area*2 + n*2 -1)
