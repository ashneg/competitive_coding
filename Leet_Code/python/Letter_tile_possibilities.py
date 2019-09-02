class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = 0
        for i in range(1,len(tiles)+1):
            count += len(set(itertools.permutations(tiles, i)))
        return count
