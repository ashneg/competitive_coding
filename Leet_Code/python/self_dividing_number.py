class Solution:
	def selfDividingNumbers(self, left: int, right: int) -> List[int]:
		result = []
		for i in range(left, right + 1):
			count = 0
			string_num = str(i)
			length = len(string_num) 
			for digit in string_num:
				if int(digit) != 0 and i % int(digit) == 0:
					count += 1
				else:
					break
			if count == length:
				result.append(i)
		return result
