# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		if not l1 and not l2:
			return None
		num1 = ""
		while l1:
			num1 += str(l1.val)
			l1 = l1.next
		num2 = ""
		while l2:
			num2 += str(l2.val)
			l2 = l2.next
		num = int(num1[::-1]) + int(num2[::-1])
		num = str(num)[::-1]
		if not num:
			return None
		res = ListNode(int(num[0]))
		node = res
		for i in range(1, len(num)):
			node.next = ListNode(int(num[i]))
			node = node.next
		return res
