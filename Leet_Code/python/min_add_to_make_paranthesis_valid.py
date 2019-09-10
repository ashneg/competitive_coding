class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        
        cnt = 0
        
        stack = []
        
        for i in S:
            
            if i == '(':
                stack.append(i)
            
            elif i == ')':
                if not stack : cnt += 1
                else : stack.pop()
                    
        return len(stack) + cnt
