class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # Solution 1: 使用两个1*26大小的list记录每个字符串出现的次数，字典映射26个小写字母对应的数字顺序，通过窗口滑动的思想判断是否有符合条件的连续子串可以在字符串s当中。
        if len(s) < len(p):
            return []
        
        Dict = {}
        for i in range(26):
            Dict[chr(ord('a') + i)] = i
        
        pfind = [0] * 26
        
        for i in p:
            pfind[Dict[i]] += 1
        
        sfind = [0] * 26
        
        np = len(p)
        ns = len(s)
        
        result = []
        for i in range(np):
            sfind[Dict[s[i]]] += 1
            if sfind == pfind:
                result.append(0)
        
        for i in range(1, ns - np + 1):
            sfind[Dict[s[i - 1]]] -= 1
            sfind[Dict[s[i + np - 1]]] += 1
            if sfind == pfind:
                result.append(i)
                
        return result
            
        
