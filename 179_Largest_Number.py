import functools
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(x) for x in sorted(nums, key=functools.cmp_to_key(self.componse))]
        
        result = "".join(nums)
        
        if result.startswith("0"):
            return "0"
        return result
        
    
    def componse(self, x, y):
        return -1 if str(x) + str(y) >= str(y) + str(x) else 1
    
    
# Sorting via Custom Comparator 
# 官方认可解答 大同小异
# class LargerNumKey(str):
#     def __lt__(x, y):
#         return x+y > y+x
        
# class Solution:
#     def largestNumber(self, nums: List[int]) ->  str:
#         largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
#         return '0' if largest_num[0] == '0' else largest_num
