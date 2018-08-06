# -*- coding:utf-8 -*-


# brute force 暴力破解结果 时间复杂度为O(n三次方)
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    G = []
    Lk = set()
    L = []
    if sum(nums) == 0:
        return nums
    for i in nums:
        for j in nums:
            for k in nums:
                if i + j + k == 0:
                    if i not in Lk:    # 通过set集合排重 保证i,j,k不是同时出现在列表中 (起码有一个为新值 得到排重后的结果 组合为列表 返回到外部)
                        Lk.add(i)
                    if j not in Lk:
                        Lk.add(j)
                    if k not in Lk:
                        Lk.add(k)
                    else:
                        continue
                    D = [i, j, k]
                    G.append(D)
    return G


KG = []
def twosum(nums, i, target):
    left, right = i + 1, len(nums) - 2
    while left < right:
        if nums[left] + nums[right] == target:
            QT = [nums[i], nums[left], nums[right]]
            KG.append(QT)
            if left < right and nums[left] == nums[left + 1]:
                left += 1
            if right < right and nums[right] == nums[right - 1]:
                right -= 1
            left += 1
            right -= 1
        elif nums[left] + nums[right] + target < 0:
            left += 1
        else:
            right -= 1



# 将问题分解为2sum的问题 降低时间复杂度 (n平方) 空间为O(1)
def threesum(nums, K):
    for i in range(1, len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        twosum(nums, i, 0 - nums[i])
    print()



class Kpoo(object):
    def threesum(self, m):
        print(m)


def myreversed(L):
    return [x for x in L[::-1]]


def myreversed_02(L):
    L2 = []
    for i in L1[-1::-1]:
        L2.append(i)
    return L2


if __name__ == '__main__':
    L = [-1, 0, 1, -2, 4, 2]
    G = threeSum(L)
    KG = []
    L.sort()

    for i in range(len(L) - 2):
        if i > 0 and L[i] == L[i - 1]:
            continue
        left, right = i + 1, len(L) - 1
        target = L[i]
        while left < right:
            if L[left] + L[right] + target == 0:
                QT = [L[i], L[left], L[right]]
                KG.append(QT)
                while left < right and L[left] == L[left + 1]:
                    left += 1
                while right < right and L[right] == L[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif L[left] + L[right] + target < 0:
                left += 1
            else:
                right -= 1
    print(KG)
    print(G)
    L1 = [1, 2, 3, 4]
    L2 = myreversed(L1)
    L3 = myreversed_02(L1)
    print(L2, L1, L3)
