class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isWord = False

# from collections import defaultdict
# class Trie:
#     # Solution 1:基于哈希表和hashset，以及高性能defaultdict的原理进行实现的Tire树(字典树结构)
      # AC 55%
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.letter = defaultdict(set)
        

#     def insert(self, word):
#         """
#         Inserts a word into the trie.
#         :type word: str
#         :rtype: void
#         """
#         if not word:
#             return False
        
#         self.letter[word[0]].add(word)
        

#     def search(self, word):
#         """
#         Returns if the word is in the trie.
#         :type word: str
#         :rtype: bool
#         """
#         if not word:
#             return False
#         if self.letter.get(word[0]):
#             if word in self.letter.get(word[0]):
#                 return True
#         return False
        
        

#     def startsWith(self, prefix):
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         :type prefix: str
#         :rtype: bool
#         """
#         if not prefix:
#             return False
#         if self.letter.get(prefix[0]):
#             for one in self.letter.get(prefix[0]):
#                 if one.startswith(prefix):
#                     return True
#         return False
        
class Trie:
    # Solution 2:实现TrieNode类, 构建Trie树,通过isWord判断当前节点是否存储了一个单词,children存储当前节点的后代节点。
    # AC 64%
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node  = self.root
        for letter in word:
            child = node.children.get(letter)
            if child is None:
                child = TrieNode()
                node.children[letter] = child
            node = child
        node.isWord = True
        
    
    
    def search(self, word):
        node = self.root
        for letter in word:
            node = node.children.get(letter)
            if node is None:
                return False
        return node.isWord

    
    def startsWith(self, prefix):
        node = self.root
        for letter in prefix:
            node = node.children.get(letter)
            if node is None:
                return False
        return True
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
