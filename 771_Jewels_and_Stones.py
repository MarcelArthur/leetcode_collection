class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # Solution 1: 通过hashset判重是否Stones字符串中是否存在符合Jewels的内容
        v = set(J)
        return sum([1 for x in S if x in v])
    
        
