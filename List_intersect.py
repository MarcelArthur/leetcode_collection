# !python3

'''
交叉链表求交点
githb面试题上的交叉链表求交点是错误的
'''
class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None


def node(l1, l2):
    length1, length2 = 0, 0
    wcx, Li = l1, l2
    while l1.next:
        l1 = l1.next
        length1 += 1
    while l2.next:
        l2 = l2.next
        length2 += 1
    # 如果相交

    if length1 > length2:
        for _ in range(length1 - length2):
            wcx = wcx.next
    elif length2 > length1:
        for _ in range(length2 - length2):
            Li = Li.next

    while wcx and Li:
        if wcx == Li:
            return Li
        else:
            wcx = wcx.next
            Li = Li.next


if __name__ == '__main__':
    L4 = ListNode(1)
    L5 = ListNode(2)
    L6 = ListNode(3)
    Lg = ListNode(10)
    L4.next = L5
    L6.next = L5
    Lg.next = L4
    L = node(Lg, L6)
    print(L.value)
