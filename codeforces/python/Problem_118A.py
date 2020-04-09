word,ret = "AEIOUYyaeiou",[]
inpt = input()
for i in inpt:
    if(i not in word):
        ret.append('.')
        ret.append(i)
print("".join(ret).lower())
