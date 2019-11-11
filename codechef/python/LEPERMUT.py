for _ in range(int(input())):
    n=int(input());mi,li=0,0;
    a=list(map(int,input().split()))
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if(a[i]>a[j]):
                mi+=1
        if(a[i]>a[i+1]):
            li+=1
    if(mi==li):
        print("YES")
    else:
        print("NO")
