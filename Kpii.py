# -*- coding:utf-8 -*-


# 达到运算目的 但是 时间复杂度 为O（n平方）, LeetCode大数组时耗时 > 1min
def MaxAres(height):
    if height == [] or len(height) < 3:
        return 0
    sum = 0
    for i in range(len(height)):
        for j in range(i, len(height)):
            he = min(height[j], height[i])
            kp = j - i
            sr = he * kp
            if abs(sr) > sum:
                sum = sr
    return sum


# 逻辑严谨 但是速度欠佳
def maxArea(height):
    left, right = 0, len(height) - 1
    maxAres = 0
    while (left < right) and (left >= 0) and (right <= len(height)-1):
        # ???为什么不在判断后计算得到相对
        maxAres = max(maxAres, min(height[left], height[right]) * (right - left))
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return maxAres


# 相比于前一个逻辑不太严谨，但是判断很少 而且很快算法速度较快 此处一切为了速度（减少了一部分逻辑性）
def maxA(height):
    left, right = 0, len(height) - 1
    volume = (right - left) * min(height[left], height[right])

    best = volume
    while left != right:
        if height[left] > height[right]:
            volume = (right - left) * height[right]
            right -= 1
        else:
            volume = (right - left) * height[left]
            left += 1

        if best < volume:
            best = volume

    return best

if __name__ == "__main__":
    L = [10, 5, 9, 33, 66, 8, 17, 65, 12]
    print(MaxAres(L))
    print(maxArea(L))
    print(maxA(L))


