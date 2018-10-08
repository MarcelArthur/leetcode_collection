# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        '''
        Solution 1:
        利用列表记录链表值翻转比对是否一致
        '''
        # res = []
        # while head:
        #     res.append(head.val)
        #     head = head.next
        # if res[::-1] != res:
        #     return False
        # return True
        
        '''
        Solution 2:
        首先利用快慢指针进行移动到链表的中间节点，同时将前半部分的链表进行逆置，再次移动一次慢指针，最后分为前后两部分的单链表, 对两链表进行比较，如果比较结果相同(遍历到尾结点)则返回True,如果翻转链表没有遍历到尾结点则返回False。
        '''
        rev = None
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and slow.val == rev.val:
            rev = rev.next
            slow = slow.next
        return not rev
            
