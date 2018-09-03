# C++
class Solution {
public:
    int largestPalindrome(int n) {
        if(n==1) return 9;
        int upper = pow(10, n) - 1;
        int lower = pow(10, n - 1);
        for (int i = upper; i > lower; --i) {
            long long cand = creatPalindrome(i);
            for (int j = upper; cand / j < j; --j) {
                if (cand % j == 0) return cand % 1337;
            }
        }
        return -1;
    }

private:
    long long creatPalindrome(int n) {
        string lastHalf = to_string(n);
        reverse(lastHalf.begin(), lastHalf.end());
        return stoll(to_string(n) + lastHalf);
    }
};

# Python 超时
# 输入数字大于4,超时，应该是性能问题，遍历和运算不高效
class Solution:
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 9
        max_num = 10**n - 1
        min_num = 10**(n - 1) - 1
        result = 0
        for m in range(max_num, min_num, -1):
            for n in range(max_num, min_num, -1):
                test = m * n
                test_len = len(str(test))
                test_slice = int(test_len / 2)
                if str(test)[:test_slice] == str(test)[test_slice:][::-1]:
                   
                    if test > result:
                        result = test
        result %= 1337
        return result
                    

# 填表法....不写了 没什么意思
