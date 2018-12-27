# C++
class Solution {
public:
    int maxCoins(vector<int>& nums) {
        int arr[nums.size()+2];
        
        for(int i=1;i<nums.size()+1;++i)arr[i] = nums[i-1];
        arr[0] = arr[nums.size()+1] = 1;
        
        int dp[nums.size()+2][nums.size()+2]={};
        int n = nums.size()+2;
        
        for(int k=2;k<n;++k)
        {
            for(int left = 0;left<n-k;++left){
                int right = left + k;
                for(int i=left+1;i< right; ++i)
                {
                    dp[left][right] = max(dp[left][right],arr[left]*arr[i]*arr[right] + dp[left][i] + dp[i][right]);
                }
            }    
        }
        return dp[0][n-1];
    }
};
# Python
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Good Solution 
        # https://leetcode.com/problems/burst-balloons/discuss/76257/Python-solution%3A-beats-98.31
        nums = [1] + nums + [1] 
        table = [[0 for x in range(len(nums))] for y in range(len(nums))]
        # initialize solutions (table) for 3 consecutive elements
        k = 0
        while k + 2 < len(nums):
            left, right = k, k + 2
            table[left][right] = nums[k] * nums[k + 1] * nums[k + 2]
            k += 1
        for l in range(3, len(nums)):
            k = 0
            while k + l < len(nums):
                left, right = k, k + l
                solutions = []
                for i in range(left + 1, right):
                    ans = table[left][i] + nums[left] * nums[i] * nums[right] + table[i][right]
                    solutions.append(ans)
                solution = max(solutions)
                table[left][right] = solution
                k += 1
        return table[0][-1]

