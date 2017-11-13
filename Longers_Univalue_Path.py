# !python3
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def loopup(root):
    stack = [root]
    while stack:
        current = stack.pop(0)
        print(current.data)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
if __name__ == '__main__':
    tree = Node(1, Node(2, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))
    loopup(tree)