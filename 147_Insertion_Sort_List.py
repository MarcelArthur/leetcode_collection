# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 时间复杂度On2
class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head 
        helper = ListNode(0)
        helper.next = head 
        pre = head  # 排好序的最后一个节点
        cur = head.next  # 从第二个节点开始遍历
        
        while cur:
            if cur.val < pre.val:
                nextNode = cur.next
                cur2 = helper.next
                temp = helper
                while cur.val > cur2.val and cur2 != pre: # 遍历cur2的链表(过滤当前节点本身)
                    temp = cur2  # 记录前一个节点位置
                    cur2 = cur2.next # 记录后一个节点位置
                # 插入对应的链表位置 
                temp.next = cur
                cur.next = cur2
                pre.next = nextNode #更新当前节点位置
                cur = nextNode # 更新节点位置
            else:
                # 更新节点
                pre = cur
                cur = cur.next
        return helper.next
