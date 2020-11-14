#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next:
            return head
        head1, head2 = head, head.next
        head3 = head2

        while head2 and head2.next:
            head1.next = head1.next.next
            head2.next = head2.next.next
            head1 = head1.next
            head2 = head2.next

        head1.next = head3
        return head
# @lc code=end

