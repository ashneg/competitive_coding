def minion_game(S):
    # your code goes here
    stuart,kevin = 0,0

    for i in range(len(S)):
        if S[i] in 'AEIOU':
            kevin += len(S) - i
        else:
            stuart += len(S) - i

    if kevin > stuart:
        print ('Kevin', kevin)
    elif stuart > kevin:
        print ('Stuart', stuart)
    else:
        print ('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
