import re
class Solution:
    def removeVowels(self, S: str) -> str:
        result = re.sub(r'[AEIOU]', '', S, flags=re.IGNORECASE)
        return result
