class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # Solution1: 普通思路,遍历后排序,当数组长度达到对应的k值时返回数组最后一位的值 AC 66.07%
        if not matrix:
            return 
        mat_list = list()
        for mat_one in matrix:
            mat_list.extend(mat_one)
        mat_list.sort()
        print(mat_list)
        return mat_list[k-1]
                
