from itertools import product

class Solution(object):
    def letterCombinations(self, digits):
        nums = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' '
        }
        args = [nums[n] for n in digits]
        if args:
            return [''.join(a) for a in product(*args)]
        return []
