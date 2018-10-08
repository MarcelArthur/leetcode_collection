from collecitons import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        '''
        根据排序后的值作为hash表的key值
        
        '''
        
        r = {}
        for i in strs:
            c = ''.join(sorted(i))
            if c in r:
                r[c].append(i)
            else:
                r[c] = [i]
        return [r[x] for x in r]
    
        '''
        官方实现
        依据第三方包的性质
        四行实现~
        '''
        # v = defaultdict(list)
        # for s in strs:
        #     v[tuple(sorted(s))].append(s)
        # return v.values()
        
