def merge_the_tools(s, k):
    for i in range(int(len(s) / k)):
        t = ''
        for c in s[i * k : (i + 1) * k]:
            if c in t:
                continue
            t += c
        print (t)
