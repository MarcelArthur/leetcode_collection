# Hard
class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # O(N)时间复杂度内展示 未超时但是效率佳
        # Solution1: 优先算出第一次在框内的元素最大值，之后定位在左侧的第一个位置，依次遍历至结尾为止，中间通过max函数判断得到最大值。时间复杂度不是O(N),不过最后居然没有超时。= =这道题还是挺水的，要求并不高。
        # Solution2: 同样是优先算出框内的最大元素值，之后从末尾开始遍历至列表末尾，判断任意元素如果大于上次的最大值则直接替换，如果最小坐标为上次的最大值，则重新计算本组内的最大值再进行替换。比较好的思路,减少max函数的使用次数，时间复杂度接近O(N),但是实际上存在同组内有两个最大值的情况，因此还是会有不必要使用max函数的场景增加时间复杂度。
        # Solution3: 理想中的O(N)复杂度是什么样的呢？
        
        # Solution1
        if not nums:
            return []
        max_list = []
        nums_k = nums[:k]
        max_one = max(nums_k)
        max_list.append(max_one)
        for i in range(1, len(nums) + 1 - k):
            if i+k >= len(nums) + 1:
                break
            nums_index = max(nums[i:i+k])
            max_list.append(nums_index)
        return max_list

        # Solution2
        if not nums:
            return []
        max_c = max(nums[:k])
        ans = [max_c]

        for i in range(k, len(nums)):
            if max_c < nums[i]:
                max_c = nums[i]
            elif nums[i - k] == max_c:
                max_c = max(nums[i - k + 1:i+1])

            ans += max_c,
        return ans
        
        
