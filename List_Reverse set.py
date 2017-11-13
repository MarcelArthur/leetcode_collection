# python3
'''
单链表逆置
'''


class ListObeject:
    def __init__(self, data =None, next=None):
        self.data = data
        self.next = next

Link = ListObeject(1,ListObeject(2, ListObeject(3, ListObeject(4))))

def rev(link):
    pre = link
    cur = link.next
    pre.next = None
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre

root = rev(Link)

while root:
    print(root.data, end=' ')
    root = root.next