#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        result, last_seen, max_last_seen, count = [], {}, 0, 0
        # explain: 寻找字母最晚出现的位置
        for i, char in enumerate(S):
            last_seen[char] = i

        for i, char in enumerate(S):
            max_last_seen = max(max_last_seen, last_seen[char])
            count += 1
            if i == max_last_seen:
                result.append(count)
                count = 0
        return result

        # optimization
        # 2.too fast
        last_seen = {c:i for i, c in enumerate(S)}
        result, count, max_last_seen = [], 0, 0
        
        for i in range(len(S)):
            max_last_seen = max(max_last_seen, last_seen[S[i]])
            if  i == max_last_seen:
                result.append(i - count + 1)
                count = i + 1
        return result
# @lc code=end

