class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        res = []
        for row in A:
            res.append([1 if x==0 else 0 for x in row[::-1]])
        return res
