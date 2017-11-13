# !python3
# 二分查找
import math
class Solution(object):
    def constructRectangle(self, area):
        mid = int(math.sqrt(area)) # like floor
        while area % mid != 0:
            mid -= 1
        return [int(area/mid), mid]