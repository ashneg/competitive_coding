#we could also use if/ else approach but that is slower
class Solution:
    def intToRoman(self, num: int) -> str:
        cur_dict = {9:'IX', 8:'VIII', 7:'VII', 6:'VI', 5:'V', 4:'IV', 3:'III', 2:'II', 1:'I', 0:''}
        roman = cur_dict[num % 10]
        num = num // 10
        cur_dict = {9:'XC', 8:'LXXX', 7:'LXX', 6:'LX', 5:'L', 4:'XL', 3:'XXX', 2:'XX', 1:'X', 0:''}
        roman = cur_dict[num % 10] + roman
        num = num // 10
        cur_dict = {9:'CM', 8:'DCCC', 7:'DCC', 6:'DC', 5:'D', 4:'CD', 3:'CCC', 2:'CC', 1:'C', 0:''}
        roman = cur_dict[num % 10] + roman
        num = num // 10
        cur_dict = {3:'MMM', 2:'MM', 1:'M', 0:''}
        roman = cur_dict[num % 10] + roman
            
        return roman
