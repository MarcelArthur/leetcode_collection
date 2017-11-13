# !python3
def nextGreaterElement(findNums, nums):
    """
            :type findNums: List[int]
            :type nums: List[int]
            :rtype: List[int]
            """
    if not findNums:
        return []
    ynum = nums.index(findNums[0])
    print(ynum)
    for i in range(ynum, len(nums)):
        if findNums[0] < nums[i]:
            count = nums[i]
            break
    else:
        count = -1
    find, *findNum = findNums

    return [count] + nextGreaterElement(findNum, nums)

if __name__ =='__main__':
    print(nextGreaterElement([2, 4], [1, 2, 3, 4]))
