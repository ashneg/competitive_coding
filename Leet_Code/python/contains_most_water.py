class Solution:
    def maxArea(self, height: List[int]) -> int:
        low, high, max_area = 0, len(height) - 1, 0
        while low < high:
            max_area = max((high - low) * min(height[low], height[high]), max_area)
            low, high = low + (height[low] < height[high]), high - (height[low] >= height[high])
        return max_area
