class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # Solution 1: 时间复杂度O(M(M+N)) 空间复杂度O(N)
        # 我们使用一个height数组，保存到某一层的第i个位置为止，能向上构成的矩形的高度。而且需要对每层都做一个寻找面积的操作，最终选择所有层中能够成矩形面积最大值。
         
        if not matrix or not matrix[0]:
            return 0
        M, N = len(matrix), len(matrix[0])
        
        height = [0] * N
        res = 0
        for row in matrix:
            for i in range(N):
                if row[i] == '0':
                    height[i] = 0
                else:
                    height[i] += 1
            res = max(res, self.maxRectangleArea(height))
        return res
    def maxRectangleArea(self, height):
        if not height:
            return 0
        res = 0
        stack = list()
        height.append(0)
        for i in range(len(height)):
            cur = height[i]
            while stack and cur < height[stack[-1]]:
                w = height[stack.pop()]
                h = i if not stack else i - stack[-1] - 1
                res = max(res, w * h)
            stack.append(i)
        return res
        
        
        # Solution 2: DP动态规划
