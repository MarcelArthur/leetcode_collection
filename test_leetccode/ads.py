import collections
class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isword = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        current = self.root
        for w in word:
            current = current.children[w]
        current.isword = True

if __name__ == '__main__':
    obj = WordDictionary()
    obj.addWord('abc')
    print(obj.root)
    print(obj.root.children)
    print(obj.root.children.values())
    # param_2 = obj.search('abc')
