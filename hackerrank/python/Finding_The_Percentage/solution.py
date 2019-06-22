from functools import reduce
if __name__ == '__main__':
    n = int(input())
    s = 0
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
print ('%.2f'%float(reduce(lambda a, b: a + b, student_marks[query_name]) / len(student_marks[query_name])))
