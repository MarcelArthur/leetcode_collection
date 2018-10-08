# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        '''
        遍历两次链表得到交点
        Solution1: 时间复杂度O(2N),空间复杂度O(1)，AC 332ms beats 14% (多次循环多次判断)
        Solution2(思路相同,修改结构,判断后再进行循环指针移动,返回值为链表headA当前指针的所指的节点-一次判断多次循环): AC 204ms beats 90%
        总体思路遍历一次链表A和链表B获取链表长度,已知有交点情况下，后半部分的长度一定相同，移动修正长链表长度，在长度相同情况下同时移动链表A和链表B,获得
        交点或者无交点情况返回None
        '''
        length1 = 0
        length2 = 0
        hA = headA
        hB = headB
        while headA:
            headA = headA.next
            length1 += 1
        while headB:
            headB = headB.next
            length2 += 1
        # while length1 != length2:
        #     if length1 > length2:
        #         hA = hA.next
        #         length1 -= 1
        #     elif length1 < length2:
        #         hB = hB.next
        #         length2 -= 1
        if length1 > length2:
            for i in range(length1 - length2):
                hA = hA.next
        elif length1 < length2:
            for i in range(length2 - length1):
                hB = hB.next
        while hA != hB:
            hA = hA.next
            hB = hB.next
        return hA
