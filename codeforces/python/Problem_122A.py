    n = int(input())
    print('YES' if any(n%i==0 for i in [4, 7, 47, 74, 477, 744]) else 'NO')
