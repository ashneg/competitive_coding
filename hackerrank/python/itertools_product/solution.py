import itertools
if __name__ == '__main__':
    a,b = list(map(int,input().strip().split())),list(map(int,input().strip().split()))
    print(*list(itertools.product(a, b)))
