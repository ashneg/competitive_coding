class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        max_row=[max(row) for row in grid]
        
        #Find the max element for each column, max_column
        max_column = [max(j) for j in zip(*grid)]
        
        return sum(min(max_row[r], max_column[c]) - val
                   for r, row in enumerate(grid)
                   for c, val in enumerate(row))
