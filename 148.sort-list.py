#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, h1, h2):
        dummy = tail = ListNode(None)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next, tail, h1 = h1, h1, h1.next
            else:
                tail.next, tail, h2 = h2, h2, h2.next
        tail.next = h1 or h2
        return dummy.next
        
    def getmid(self, head):
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return mid

        
    def sortList(self, head):
        if not head or not head.next:
            return head

        mid = self.getmid(head)
        h1 = self.sortList(head)
        h2 = self.sortList(mid)

        return self.merge(h1,h2)
        
            
# @lc code=end

