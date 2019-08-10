from calendar import monthrange
class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        return monthrange(Y, M)[1]
