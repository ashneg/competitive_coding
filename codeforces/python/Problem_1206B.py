q = int(input())
l = list(map(int, input().split()))
 
 
steps = sum(abs(abs(x) - 1) for x in l)
minuses = sum(1 for x in l if x < 0)
zeroes = any(x == 0 for x in l)
 
if minuses % 2 == 1 and not zeroes:
    steps += 2
 
 
print(steps)
