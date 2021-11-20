class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or not k:
            return 0
        word_count = defaultdict(int)
        n = len(s)
        result = 0
        left = right = 0
        while left < n and right < n:
            word_count[s[right]] += 1
            
            while len(word_count) > k:
                word_count[s[left]] -= 1
                if word_count[s[left]] <= 0:
                    word_count.pop(s[left], None)
                left += 1
                
            result = max(result, right - left + 1)
            right += 1
            
        return result
