class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        主要利用set集合(底层hashset原理实现)特性能够高效定位单词是否在set集合当中，同时进行利用pharse短语从短到长的排序后的方式，符合条件的依次添加进入集合，同时根据符合条件的结果依次更新各个结果集的符合条件的结果，之后进行反馈
        """
        res = ''
        s = set()
        words.sort()
        for word in words:
            if len(word) == 1 or word[:-1] in s:
                res = word if len(word) > len(res) else res
                s.add(word)
        return res
