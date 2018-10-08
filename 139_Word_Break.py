class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # if not s or not wordDict:
        #     return False
        # res = []
        # for word in wordDict:
        #     if word in s:
        #         wi = s.index(word)
        #         wl = len(word)
        #         s = s[wi+wl:]
        #         res.append(word)
        #     elif word in res:
        #         pass
        #     else:
        #         return False
        # return True
        
        '''
        Solution 1:
        朴素的动态规划
        思路来自: https://leetcode.com/problems/word-break/discuss/43808/Simple-DP-solution-in-Python-with-description
        简单来说是判断当单词位于字符串头部时返回匹配结果,之后会继续遍历直到字符串尾部查找到是否返回有匹配项，通过给每个位置字符标记的方式dp数组返回是否在上一位置返回True，如果所有位置全部匹配则可以认为结果为True,任意位置匹配失败则默认False。
        DP这里就是记录是否有能够返回的正确结果作为依据, dp[0]是当字符串位于头部需要判断为True才能继续判断是否匹配，符合DP需要初始化的预期~
        '''
        n = len(s)
        dp = [False for x in range(n + 1)]
        dp[0] = True
        
        for i in range(1, n + 1):
            for w in wordDict:
                wh = len(w)
                if dp[i - wh] and s[i - wh:i] == w:
                    dp[i] = True
                    break
        return dp[-1]
    
        '''
        Trie树
        又名字典树
        通常常用的数据结构之一
        (构造比较复杂？？？)
        以下实现来自于LeetCode-Discuss shiyanhui 
        https://leetcode.com/problems/word-break/discuss/44003/Very-clean-python-code-with-Trie
        '''
        # class TrieNode(object):
        #     def __init__(self, char=None, isWord=False):
        #         self.char = char
        #         self.isWord = isWord
        #         self.children = {}


        # class Trie(object):
        #     def __init__(self):
        #         self.root = TrieNode()
        #         self.cache = {}

        #     def insert(self, word):
        #         root = self.root
        #         for char in word:
        #             if char not in root.children:
        #                 root.children[char] = TrieNode(char)
        #             root = root.children[char]
        #         root.isWord = True

        #     def cache(f):
        #         def method(obj, s):
        #             if s not in obj.cache:
        #                 obj.cache[s] = f(obj, s)
        #             return obj.cache[s]
        #         return method

        #     @cache
        #     def search(self, s):
        #         root = self.root
        #         for i, char in enumerate(s):
        #             if char not in root.children:
        #                 return False

        #             if root.children[char].isWord:
        #                 if self.search(s[i + 1:]):
        #                     return True
        #             root = root.children[char]
        #         return root.isWord


        # class Solution(object):
        #     def wordBreak(self, s, wordDict):
        #         trie = Trie()
        #         [trie.insert(word) for word in wordDict]

        #         return trie.search(s)
        
        
