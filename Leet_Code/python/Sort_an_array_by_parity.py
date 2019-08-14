class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        arr = []
        arr2 = []
        for i in A:
            if(i%2 == 0):
                arr.append(i)
            else:
                arr2.append(i)
        arr.extend(arr2)
        return arr
