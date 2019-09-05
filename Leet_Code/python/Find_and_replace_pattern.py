class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
            res = []
            lp = len(pattern)
            for word in words:
                dic = {}
                i = 0
                b =True
                for w in word:
                    if w not in dic.keys():
                        if pattern[i] in dic.values():
                            b = False
                            break
                        dic[w] = pattern[i]
                    else:
                        if pattern[i] != dic[w]:
                            b = False
                            break
                    i += 1
                    if i==lp:break
                if b :res.append(word)
            return res
