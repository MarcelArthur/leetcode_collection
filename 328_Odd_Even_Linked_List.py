# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 题目要求:将链表中位置为奇数的链表放到偶数前面(可以理解为将奇数单链表和偶数单链表组合返回新链表)
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        
        odd = head
        evenhead = head.next
        even = evenhead
        while even and even.next:
            odd.next = even.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = evenhead
        return head
