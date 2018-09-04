# 根据输入的值分类并且构建搜索二叉树, 并且最终层次遍历出二叉树结构进行返回
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        # 第一个思路构建一个有效的队列，对列表索引可以进行二分查找，再分成两部分进行递归直到所有结果值全部遍历完成，输出最后的二叉树结果，其中所有任意结果之间的空子树为None值。问题是这个是一个单链表，在遍历链表的时候不能获取到整个链表状态和长度，最好的状态是边遍历边构建树结构，最后进行输出。那么由于它是一个单链表可以利用快慢指针，进行访问递归。
        node, length = head, 0
        while node:
            node = node.next
            length += 1
        self.cur = head
        return self.__sortedListToBST(0, length - 1)
        
    def __sortedListToBST(self, left, right):
        if left > right:
            return None
        mid = int((left + right) // 2)
        left = self.__sortedListToBST(left, mid - 1)
        root = TreeNode(self.cur.val)
        root.left = left
        self.cur = self.cur.next
        right = self.__sortedListToBST(mid + 1, right)
        root.right = right
        return root
        
        
