# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# looks like a bad way
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # My Solution
        a, b = "", ""
        while l1:
            a += str(l1.val)
            l1 = l1.next
            
        while l2:
            b += str(l2.val)
            l2 = l2.next
        
        res = int(a[::-1]) + int(b[::-1])
        
        L = ListNode(0)
        restr = str(res)
        head = L
        for i in range(len(restr)):
            L.next = ListNode(int(restr[::-1][i]))
            L = L.next
        return head.next
    
        # Solution 1: Easy and Faster
        l1_result = l1
        overflow = 0
        while (l1 != None or l2 != None or overflow == 1):
            overflow, l1.val = divmod(l1.val + l2.val + overflow, 10)
            if l1.next != None or l2.next != None or overflow == 1:
                if l1.next == None:
                    l1.next = ListNode(0)
                if l2.next == None:
                    l2.next = ListNode(0)
            l1 = l1.next
            l2 = l2.next
        return l1_result
            
        
        
        
