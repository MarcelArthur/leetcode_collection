#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#

# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # 排序+Hashset排重
        # 95% Time & 100% Memory
        # if len(arr) == 2 and arr[0] != arr[1]:
        #     return False
        # res = set()
        # arr_sorded = sorted(arr)
        # count = 0
        # for i in range(len(arr_sorded)):
        #     if count == 0:
        #         count += 1
        #         continue
        #     if arr_sorded[i] == arr_sorded[i-1]:
        #         count += 1
        #     else:
        #         if count in res:
        #             return False
        #         else:
        #             res.add(count)
        #         count = 1
        # return True
        # https://leetcode.com/problems/unique-number-of-occurrences/discuss/393086/Solution-in-Python-3-(one-line)-(beats-100.00-)
        return (lambda x: len(x) == len(set(x)))(Counter(arr).values())
# @lc code=end

