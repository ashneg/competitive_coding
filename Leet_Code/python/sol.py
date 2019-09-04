class Solution:
    def twoSum(self, nums, target):
        dic = {}
        for index, num in enumerate(nums):
            if num in dic:
                return [dic[num], index]
            dic[target - num] = index

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    (Solution().twoSum(nums, target) == [0, 1])
    nums = [3, 2, 4]
    target = 6
(Solution().twoSum(nums, target) == [1, 2])
