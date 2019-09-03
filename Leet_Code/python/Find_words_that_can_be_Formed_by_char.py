class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = 0
        for w in words:
            included = True
            charsList = [c for c in chars]
            for c in w:
                if c in charsList:
                    charsList.remove(c)
                else:
                    included = False
                    break
            if included: counter = counter+len(w)
        return counter
                    
