# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        '''
        解题思路来自糖梦梦是女侠的博客
        url: https://blog.csdn.net/tmylzq187/article/details/50913211
        主要是如何解决复制随机指针的问题。通过在原有的链表每个结点之间插入新链表,可以根据原有结点的随机指针的下一个结点依次复制到新链表中,再拆分原有链表的组合得到新链表
        '''
        
        
        if not head:
            return head
        p = head
        while p:
            rln = RandomListNode(p.label)
            rln.next = p.next
            rln.random = None
            p.next = rln
            p = p.next.next
        
        # 复制random指针
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        
        # 拆分成两个链表
        p = head
        new_List = p.next
        while p:
            p_next = p.next
            p.next = p_next.next
            if p_next.next:
                p_next.next = p_next.next.next
            else:
                p_next.next = None
            p = p.next
        return new_List
        
