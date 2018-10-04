class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        '''
        求极值问题 首选DP
        Solution 1:
        非常有意思的题目
        主要是依据动规思想，这里通过两次扫描高度实现。第一次记录从左到右每个水槽左边的最高高度是存入数组，第二次从右到左扫描每个水槽右侧高度和左侧高度的最小值(木桶效应),同时更新右侧高度的值进行下一位置水槽高度比较。在通过水槽短板高度和水槽深度的差值如果是正值则记录进结果，负值则为不能存水。
        '''
        res = 0
        # trap_map = [0 for x in height]
        # MAX = 0
        # for i in range(len(height)):
        #     trap_map[i] = MAX
        #     MAX = max(MAX, height[i])
        # MAX = 0   
        # for j in range(len(height) - 1, -1, -1):
        #     trap_map[j] = min(MAX, trap_map[j])
        #     MAX = max(MAX, height[j])
        #     if trap_map[j] > height[j]:
        #         res += trap_map[j] - height[j]
        #     else:
        #         res += 0
        # return res
    
        '''
        Solution 2:
        扫描一次，两指针向中间移动，同时记录计算水量
        url: https://blog.csdn.net/linhuanmars/article/details/20888505
        主要思路来自网络~
        '''
        h = height
        l = 0
        r = len(h) - 1
        while l < r:
            mr = min(h[l], h[r])
            if h[l] == mr:
                l += 1
                while l < r and h[l] < mr:
                    res += mr - h[l]
                    l += 1
            else:
                r -= 1
                while l < r and h[r] < mr:
                    res += mr - h[r]
                    r -= 1
        return res
        
