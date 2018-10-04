# Easy
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        '''
        1 解题思路
        https://blog.csdn.net/fuxuemingzhu/article/details/80471765
        第一步，先假设在很远的位置有个C字符，那么从左到右开始遍历，找出每个字符到其最近的左边的字符C的距离； 
        第二步，先假设在很远的位置有个C字符，那么从右到左开始遍历，找出每个字符到其最近的右边的字符C的距离，并和第一步求出的距离进行比较，找出最小值为结果
        时间复杂度O(2N)
        空间复杂度O(N)
        '''
        pre = -100000
        res = []
        for i in range(len(S)):
            if S[i] == C:
                pre = i
            res.append(abs(i - pre))
        
        pre = -100000
        for i in range(len(S) - 1, -1, -1):
            if S[i] == C:
                pre = i 
            res[i] = min(abs(i - pre), res[i])
        return res
        
