class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs.pop(0)
        max_len = len(prefix)
        for string in strs:
            while(not (prefix[:max_len] == string[:max_len])):
                max_len -= 1
        return prefix[:max_len]
