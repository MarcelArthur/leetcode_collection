i# 正常思路: 1 二叉树递归实现 2 递归具体的条件需要思考下(什么条件下组合“左”or“右”括号)
# 优先判断终止条件如果（1 左边大于0的情况下，优先组合左括号 （2同时在左小于右的时候组合右括号 这样因为二叉树的递归效果，可以快速遍历到所有有可能的结果
# 此处不贴最优实现，仅记录最清晰的实现思路~
# 非常赞的题~
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return [""]
        
        ret_result = list()
        self.generate_dfs(ret_result, "", n, n)
        return ret_result
    
    def generate_dfs(self, ret_result, root, left,  right):
        if left == 0 and right == 0:
            ret_result.append(root)
            return 
        elif left > 0:
            self.generate_dfs(ret_result, root + '(', left - 1, right)
        
        if left < right:
            self.generate_dfs(ret_result, root + ')', left, right - 1)
            
# 突然发现一个很有意思的答案，思想上和二叉树递归是一样的，只不过变成循环遍历的方式，通过二维数组实现遍历出所有的有效结果值    
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]
