# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        '''
        卧槽 单链表排序
        思路一: 遍历链表一记录位置和值，遍历之后链表的同时比对链表一中的值和位置，如果发现有符合条件的结点，断开连接插入链表一，直到所有链表全部插入为止
        Fail
        '''
        '''
        Solution 1:
        利用最小堆的解决多链表排序的问题，每次入堆链表首个结点元素值，最小堆排序后弹出最小值加入结果值中，之后再次入堆首个结点元素的下个元素。
        
        特别注意:由于Python3中的底层实现部分变动,关于heapq这个第三方包的实现也受到影响，这里的x是需要在链表结点val一致的情况下继续判断的key值。原因如下: 
        当对一个tuple排序时，python会从0开始对两个tuple的成员依次比较，如果两个成员相同就再比较下一个成员。问题中的tuple很有趣，前两个链表的第一项比较结果都相同（1），于是python开始比较第二个成员，第二个成员是一个ListNode，没有比较方法，在处理这个问题上py2和py3有了差异，py2随机瞎排，py3则是抛出异常。
        '''
        heap = []
        x = 0
        for l in lists:
            if l != None:
                heapq.heappush(heap, (l.val, x, l))
                x += 1
        heapq.heapify(heap)
        P = ListNode(0)
        cur = P
        while heap:
            i, _, k = heapq.heappop(heap)
            cur.next = k
            cur = cur.next
            if k.next:
                heapq.heappush(heap, (k.next.val, x, k.next))
                x += 1
        return P.next
        
        '''
        Solution 2:
        Divide and Conquer Approach
        比如k个链表先划分为合并两个k/2个链表的任务，再不停的往下划分，直到划分成只有一个或两个链表的任务，开始合并。举个例子来说比如合并6个链表，那么按照分治法，我们首先分别合并1和4,2和5,3和6。这样下一次只需合并3个链表，我们再合并1和3，最后和2合并就可以了。参见(C++)代码如下：
        url: http://www.cnblogs.com/grandyang/p/4606710.html
        
        '''
        
              
#         class Solution {
# public:
#     ListNode *mergeKLists(vector<ListNode *> &lists) {
#         if (lists.size() == 0) return NULL;
#         int n = lists.size();
#         while (n > 1) {
#             int k = (n + 1) / 2;
#             for (int i = 0; i < n / 2; ++i) {
#                 lists[i] = mergeTwoLists(lists[i], lists[i + k]);
#             }
#             n = k;
#         }
#         return lists[0];
#     }
    
#     ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
#         ListNode *head = new ListNode(-1);
#         ListNode *cur = head;
#         while (l1 && l2) {
#             if (l1->val < l2->val) {
#                 cur->next = l1;
#                 l1 = l1->next;
#             } else {
#                 cur->next = l2;
#                 l2 = l2->next;
#             }
#             cur = cur->next;
#         }
#         if (l1) cur->next = l1;
#         if (l2) cur->next = l2;
#         return head->next;
#     }
# };

        '''
        Solution 3: 对于多路归并排列，我们可以使用优先队列解决。我们首先想到的解法是，依次将list中的ListNode弹出，然后一次添加到一个优先队列中，最后将优先队列中ListNode依次弹出，并且添加到result中即可。实际就是利用优先队列的特性遍历链表再重做即可获得排序后的结果。时间复杂度O(2N),空间复杂度O(N).
        url: https://blog.csdn.net/qq_17550379/article/details/81151977
        '''
#         import heapq 
#         result = ListNode(-1)
#         cur = result
#         p = list()
#         for i in lists:
#             while i:
#                 heapq.heappush(p, (i.val, i))
#                 i = i.next

#         while p:
#             cur.next = heapq.heappop(p)[1]
#             cur = cur.next

#         return result.next




