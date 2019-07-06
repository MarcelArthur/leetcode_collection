#!python3
class Solution:
    def wordPattern(self, pattern: str, words: str) -> bool:
        """
        把字符串中的字母和对应的字符串构成map, 依次判断每一个字母是否之前构成映射，如果已经构成并且不符合则判断返回False。另外一种情况是，未构成映射，但是对应的单词之前出现过，同样不满足条件，返回False
        """
        if not words:
            return False
        word = words.split(" ")
        if len(pattern) != len(word):
            return False
        
        d = dict()
        c = set()
        for i in range(len(pattern)):
            if d.get(pattern[i]) is None and word[i] not in c:
                d[pattern[i]] = word[i]
                c.add(word[i])
            elif d.get(pattern[i]) != word[i]:
                return False
        return True

# Discuss solution
# 3 lines in python
# https://leetcode.com/problems/word-pattern/discuss/73433/Short-in-Python
class Solution:
    def wordPattern(self, pattern: str, words: str) -> bool:
        """大佬的解法"""
        s = pattern
        t = words.split()
        return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)


