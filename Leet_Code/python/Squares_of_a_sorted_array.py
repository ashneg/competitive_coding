class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ret = [x*x for x in A]
        ret.sort()
        return ret
