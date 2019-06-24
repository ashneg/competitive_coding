def solve(s):
    return " ".join(list(str(c).capitalize() for c in s.split(" ")))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
