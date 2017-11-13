# !python3
from collections import deque


def Average_of_Level_inBinary_Tree(root):
    if not root:
        return []
    results = []
    stack = deque()
    stack.append(root)
    while stack:
        sum = 0
        length = len(stack)
        for i in range(len(stack)):
            current = stack.popleft()
            sum += current.val
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        avg = float(sum) / float(length)
        results.append(avg)
    return results