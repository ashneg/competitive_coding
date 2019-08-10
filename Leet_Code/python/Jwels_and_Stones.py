class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for i in J:
            c = S.count(i)
            count+=c
        return count
