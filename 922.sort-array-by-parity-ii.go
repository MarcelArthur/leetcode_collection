/*
 * @lc app=leetcode id=922 lang=golang
 *
 * [922] Sort Array By Parity II
 */

// @lc code=start
func sortArrayByParityII(A []int) []int {
	if A == nil {
		return A
	}
	even, odd := 0, 1

	for even < len(A) && odd < len(A) {
		if A[even]%2 != 0 {
			A[even], A[odd] = A[odd], A[even]
			odd += 2
		} else {
			even += 2
		}

	}
	return A

}

// @lc code=end

