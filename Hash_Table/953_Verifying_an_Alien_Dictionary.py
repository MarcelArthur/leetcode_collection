#!python3
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """
        题目解析: 
            有一种外星人的字典需要校验，他们一样使用小写字母，但是顺序不同。根据给出的外形字典顺序order，校验给出的单词是否符合顺序。
        解法:
        https://blog.csdn.net/fuxuemingzhu/article/details/84924672
        依次判断前后两个单词是否符合条件 顺序(每一个单词字母都小于等于后一个单词字母同位置的顺序)
        """
        
        N = len(words)
        d = {c : i for i, c in enumerate(order)}
        for i in range(N-1):
            pre, after = words[i], words[i+1]
            if pre == after: continue
            _len = min(len(pre), len(after))
            for j in range(_len):
                if d[pre[j]] < d[after[j]]:
                    break
                elif d[pre[j]] > d[after[j]]:
                    return False
            if len(pre) > len(after) and pre[:_len] == after:
                return False
        return True
