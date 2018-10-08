class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        '''
        时间复杂度O(N + m)
        主要是根据规律判断,右侧的大于targe的行的坐标通常是收敛的,如果每一行的末尾元素都大于target,则target出现的位置一定小于等于坐标p。所以之后每一行只需要判断p坐标所在位置是否大于target即可,因此事件复杂度通常由O(m)决定最差的表现。
        '''
        if not matrix or not matrix[0]:
            return False
        p = -1
        for row in matrix:
            while p + len(row) and row[p] > target:
                p -= 1
            if row[p] == target:
                return True
        return False
        
        '''
        解题失败:
        深度搜索每次只遍历向右和向下查找，如果右边和下边都不存在数据,则祥左侧遍历回溯，再次通过向下查找直到能查找到目标或者结果为False
        '''
#         if not matrix:
#             return True
#         row = len(matrix)
#         col = len(matrix[0])
#         status = False
#         def dfs(matrix, target, cur, i, j):
#             if i < 0 or i >= row or j < 0 or j >= col or matrix[i][j] > target:
#                 return 
#             if matrix[i][j] == target:
#                 status = True
#             elif matrix[i][j] >= cur:
#                 cur = matrix[i][j]
                
#             dfs(matrix, target, cur, i, j + 1 )
#             dfs(matrix, target, cur, i + 1, j)
#             dfs(matrix, target, cur, i, j - 1)
#         dfs(matrix, target, 0, 0, 0)
#         return status
