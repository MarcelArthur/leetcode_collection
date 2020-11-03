/*
 * @lc app=leetcode id=941 lang=golang
 *
 * [941] Valid Mountain Array
 */

// @lc code=start
func validMountainArray(A []int) bool {
	i := 0
	n := len(A)

	if n < 3 {
		return false
	}

	for i+1 < n && A[i] < A[i+1] {
		i++
	}

	if i == 0 || i == n-1 {
		return false
	}
	for i+1 < n && A[i] > A[i+1] {
		i++
	}
	return i == n-1

}

// @lc code=end

