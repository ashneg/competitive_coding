input()
li = list(map(int,input().split()))
if ( 0 in li):
    print(len(set(li))-1)
else:
    print(len(set(li)))
