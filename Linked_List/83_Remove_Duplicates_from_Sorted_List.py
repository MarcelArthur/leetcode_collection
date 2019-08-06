#!python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        head_set = set()
        cur = head
        prev = head
        while head:
            if head.val in head_set:
                prev.next = head.next
                head.next = None
                head = prev.next
            else:
                head_set.add(head.val)
                prev = head
                head = head.next
        return cur
    
    
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        temp = head
        while temp.next:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head
                
