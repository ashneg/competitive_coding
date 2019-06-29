import itertools
if __name__ == '__main__':
    input = input().split()
    s, k = sorted(input[0]), int(input[1])
    print(*list(map(''.join, itertools.permutations(s, k))), sep='\n')
