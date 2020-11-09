#
# @lc app=leetcode id=327 lang=python3
#
# [327] Count of Range Sum
#

# @lc code=start
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # # Prefix-sum + Hashmap
        # cumsum = [0]
        # for n in nums:
        #     cumsum.append(cumsum[-1]+n)
        
        # record = defaultdict(int)

        # res = 0
        # for cum in cumsum:
        #     for target in range(lower,  upper+1):
        #         if cum - target in record:
        #             res += record[cum - target]
        #     record[cum] += 1
        # return res

        #  Prefix-sum + Merge-sort:
        if not nums:
            return 0
        cumsum = [0]
        for n in nums:
            cumsum.append(cumsum[-1]+n)

        def merge(l, r):
            if l == r:
                return 0
            
            mid = (l+r) // 2

            cnt = merge(l, mid) + merge(mid+1, r)

            i = j = mid + 1
            for left in cumsum[l:mid+1]:
                while i <= r and cumsum[i] - left < lower:
                    i+=1
                while j <= r and cumsum[j] - left <= upper:
                    j+=1
                cnt += j-i
                
            cumsum[l:r+1] = sorted(cumsum[l:r+1])
            return cnt
        return merge(0, len(cumsum)-1)



# @lc code=end

