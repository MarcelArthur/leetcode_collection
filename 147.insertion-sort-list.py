#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        helper = ListNode(0)
        helper.next = head
        pre = head # 排好序的最后一个结点
        cur = head.next  # 从第二个结点开始遍历

        while cur:
            if cur.val < pre.val:
                nextNode = cur.next
                cur2 = helper.next
                temp = helper
                while cur.val > cur2.val and cur2 != pre:
                    temp = cur2
                    cur2 = cur2.next
                temp.next = cur
                cur.next = cur2
                pre.next = nextNode
                cur = nextNode
            else:
                pre = cur
                cur = cur.next
        return helper.next
        
# @lc code=end

