class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # Solution 1: 
        # https://blog.csdn.net/qq508618087/article/details/50336795
        # 使用正常思路去查找对应的bar，时间复杂度是O(N^2),另一种借助一个stack进行寻找合适的bar计算最小矩形面积。
        # 为了保证所有元素全部出栈,在列表中添加0。每次入栈前与栈顶元素进行对比，如果大于栈顶元素则持续入栈，如果小于或者等于栈顶元素,则开始计算矩形面积。将对应的矩形位置的bar进行出栈,直到栈空或者栈顶元素小于遍历元素为止。最优时间复杂度O(N),最坏时间复杂度O(N^2),空间复杂度O(N)。
        # https://www.cnblogs.com/boring09/p/4231906.html
        stack = []
        res = 0
        heights.append(0)
        L = len(heights)
        for i in range(L):
            if not stack or heights[i] > heights[stack[-1]]:
                stack.append(i)
            else:
                while stack and heights[i] <= heights[stack[-1]]:
                    h = heights[stack[-1]]
                    stack.pop()
                    w = i if not stack else i - stack[-1] - 1
                    res = max(res, h * w)
                stack.append(i)
        return res
