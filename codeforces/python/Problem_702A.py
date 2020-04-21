input()
li = list(map(int,input().split(" ")))
curr,res = 1,1
for i in range(1,len(li)):
    if(li[i]>li[i-1]):
        curr+=1
        res = max(res,curr)
    else:
        curr = 1
print(res)
