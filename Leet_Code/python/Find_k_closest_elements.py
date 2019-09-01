class Solution(object):
    def findClosestElements(self, arr, k, x):
        return sorted([item[1] for item in sorted([[abs(item-x), item] for item in arr], key = lambda x: (x[0], x))[:k]])
