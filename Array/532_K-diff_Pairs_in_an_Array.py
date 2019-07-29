#!python3
# normal solution
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        nums = sorted(nums)
        order_t = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] - nums[i] > k:
                    break
                if nums[j] - nums[i] == k:
                    order_t.add((nums[i], nums[j]))
        return len(order_t)
    
# easy solution
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
    
        if k == 0:
            counter_nums = collections.Counter(nums)
            cnt = 0
            for i in counter_nums.values():
                if i > 1:
                    cnt += 1
            return cnt
        elif k < 0:
            return 0
        set_nums = set(nums)
        return sum(n + k in set_nums for n in set_nums)
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k > 0:
            return len(set(nums)&{n+k for n in nums})
        elif k == 0:
            return sum(v > 1 for v in collections.Counter(nums).values())
        else:
            return 0
