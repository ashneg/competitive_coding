class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        net, res, start = 0 , '', 0
        for i in range(len(S)):
            
            if S[i] == '(':
                net += 1
            else:
                net -= 1
            
            if net == 0:
                res += S[start+1:i]
                start = i + 1
        return res
