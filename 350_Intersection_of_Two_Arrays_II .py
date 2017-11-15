# python3
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
         description: 做一个hashtable实现的数据字典
        """
        # a,b = map(collections.Counter, (nums1,nums2))
        # return list((a & b).elements())
        result = []
        stack = {}
        for num in nums2:
            stack[num] = stack.get(num, 0) + 1

        for num in nums1:
            if num in stack and stack[num] > 0:
                result.append(num)
                stack[num] -= 1
        return result

if __name__ == '__main__':
    Su = Solution()
    print(Su.intersect([1,2,2,4], [2,2,2]))