# python3
'''
No 1
Approach #2 HashSet [Accepted]

No 2 Bit Manipulation

'''
class Solution:
    def missingNumber(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number

# class Solution:
#     def missingNumber(self, nums):
#         missing = len(nums)
#         for i, num in enumerate(nums):
#             missing ^= i ^ num
#         return missing

