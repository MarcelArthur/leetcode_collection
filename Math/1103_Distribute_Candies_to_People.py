#!python3
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        # Time O(sqrt(candies)) Space O(N)
        res_sum = 0
        result = [0 for x in range(num_people)]
        n = 0
        while res_sum < candies:
            n += 1
            index = (n % num_people) - 1
            if n > (candies - res_sum):
                result[index] += candies - res_sum
                break
            result[index] += n
            res_sum += n
        return result
    
# simple version
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        i = 0
        res = [0] * num_people
        while candies > 0:
            res[i % num_people] += min(candies, i+1)
            candies -= i + 1
            i += 1
        return res
    
    
    
    
    
