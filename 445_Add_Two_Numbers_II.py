# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def read(node):
            s = []
            while node:
                s.append(node.val)
                node = node.next
            return s
        s1, s2 = read(l1), read(l2)
        sum_val, ans = 0, ListNode(0)
        while s1 or s2:
            if s1:
                sum_val += s1.pop()
            if s2:
                sum_val += s2.pop()
            sum_val, ans.val = divmod(sum_val, 10)
            head = ListNode(sum_val)
            head.next, ans = ans, head
        return ans if ans.val else ans.next
        
        
        
