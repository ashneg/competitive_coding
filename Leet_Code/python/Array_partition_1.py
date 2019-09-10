class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(j for i,j in enumerate(sorted(nums)) if i%2==0)
