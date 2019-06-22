if __name__ == '__main__':
    n = int(input())
    res = []
    for _ in range(n):
        func, *parm = input().split()
        val = list(map(float, parm))
        if func == 'print':
            print(res)
        else:
            comp = 'res.' + func + "(" + ",".join(parm) + ")"
            eval(comp)

