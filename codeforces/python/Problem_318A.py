a,b=map(int,input().split());
c=b-(a+1)//2;
print([b*2-1,c*2][c>0])
