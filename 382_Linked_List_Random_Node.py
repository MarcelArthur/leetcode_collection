# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from random import randint
class Solution:
    # My Solution: 初始化里遍历链表太傻了= =, 内存滥用。O(1) time, O(N) space
#     def __init__(self, head: ListNode):
#         """
#         @param head The linked list's head.
#         Note that the head is guaranteed to be not null, so it contains at least one node.
#         """
#         self.count = 0
#         self.index = 0
#         self.node = list()
#         while head:
#             self.node.append(head.val)
#             head = head.next
#             self.count += 1
        
#     def getRandom(self) -> int:
#         """
#         Returns a random node's value.
#         """
#         if self.count == 0:
#             return None
#         idx = randint(0, self.count - 1)
#         self.index = idx
#         return self.node[self.index]
    
    # Simple Solution:
    # O(N) time, O(1) space
    def __init__(self, head: ListNode):
        """
        """
        self.head = head
        
    
    def getRandom(self) -> int:
        """
        """
        res, i, cur = None, 0, self.head
        while cur:
            
            if randint(0, i) == 0:
                res = cur.val
            cur, i = cur.next, i + 1
        return res
            
            
    


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()




