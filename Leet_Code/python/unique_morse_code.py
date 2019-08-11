class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        distinct,num = list(),0
        for i in words:
            t = ''
            for j in i:
                t = t+morse[ord(j)-97]
            if(t not in distinct):
                num+=1
                distinct.append(t)
        return num
