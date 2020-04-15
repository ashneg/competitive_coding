    a = input().split()
    for _ in range(int(input())):
        print(*a)
        c, d = input().split()
        a.remove(c)
        a.append(d)
    print(*a)
