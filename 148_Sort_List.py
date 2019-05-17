# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    '''
    Solution1:
    实质上依然是mergeList的思路
    '''
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        '''
        时间复杂度O(NlogN), 空间复杂度O(1)
        '''
        if not head:
            return head
        p, n = head, 0
        while p:
            p = p.next
            n += 1
        prehead, prehead.next = ListNode(None), head
        for i in range(math.ceil(math.log2(n))):
            p, l, r = prehead, prehead.next, prehead.next
            for _ in range(1 << i):
                r = r.next
            while l and r:
                lc = rc = w = 1 << i
                while lc or rc:
                    if not rc or lc and l.val < r.val:
                        p.next, p, l, lc = l, l, l.next, lc - 1  # 折半mergesort 可以提高空间空间利用率
                    else:
                        p.next, p, r, rc = r, r, r.next, rc - 1 if r.next else 0 
                p.next = l = r
                while r and w:
                    r, w = r.next, w - 1
        return prehead.next             
    
    '''
    Solution2:
        分割链表，递归合并
    '''
    def merge(self, h1, h2):
        if not h1:
            return h2
        if not h2:
            return h1
        
        if h1.val < h2.val:
            h1.next = self.merge(h1.next, h2)
            return h1
        else:
            h2.next = self.merge(h1, h2.next)
            return h2
        
    def sort_list_solution(self, head):
        if not head or not head.next:
            return head

        p1, p2, pre = head, head, head

        while p2 and p2.next:
            pre = p1
            p1 = p1.next
            p2 = p2.next.next

        # change the bottom
        pre.next = None

        h1 = self.sortList(head)
        h2 = self.sortList(p1)

        return self.merge(h1, h2)

    '''
    Solution3:
    直接改链表中的值，不解释了= = 目测最快
    '''
    def sortList(self, head):
        __val = []
        p = head
        while p:
            __val.append(p.val)
            p = p.next

        __val.sort()

        p = head
        n = 0
        while p:
            p.val = __val[n]
            p = p.next
            n += 1
        return head
    
    
        
        
    

