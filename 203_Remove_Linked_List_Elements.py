# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummpy = ListNode(0)
        dummpy.next = head
        pre = dummpy
        while pre.next:
            if pre.next.val != val:
                pre = pre.next
            else:
                pre.next = pre.next.next
        return dummpy.next


# The optimal solution at present 72ms
# 与我本身的题解思路一样，但是没有注意到解决[1]的更好解决方案，所以构造了虚表头，这里其实只需要多判断一次状态即可达到最短耗时
# class Solution:
#     def removeElements(self, head, val):
#         """
#         :type head: ListNode
#         :type val: int
#         :rtype: ListNode
#         """
        
#         prev=None
#         cur=head
        
#         while cur != None:
#             if cur.val == val:
#                 # this is to account for [1] case.  prev is not initialized yet, and you need to move head after removing the first element.
#                 if prev != None:
#                     prev.next=cur.next
#                 else:
#                     head=cur.next
#             else:
#                 prev=cur
#             cur=cur.next
            
#         return head
