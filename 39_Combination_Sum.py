class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        def dfs(remain, stack):
            if remain == 0:
                result.append(stack[:])
                return

            for item in candidates:
                if item > remain:
                    break
                if stack and item < stack[-1]:
                    continue
                else:
                    dfs(remain - item, stack + [item])
            return

        dfs(target, [])
        return result
