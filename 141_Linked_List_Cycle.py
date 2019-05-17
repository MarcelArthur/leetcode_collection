# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Solution 1
        # while head:
        #     if head.val == "#":
        #         return True
        #     head.val = "#"
        #     head = head.next
        # return False
        # Solution 2
        # 由于没有任何改值操作，只有遍历判断，效率Max
        root = head
        while head:
            if head.next == root:
                return True
            __next = head.next
            head.next = root
            head = __next
        return False
    
    
    
