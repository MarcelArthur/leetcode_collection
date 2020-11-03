/*
 * @lc app=leetcode id=94 lang=golang
 *
 * [94] Binary Tree Inorder Traversal
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func inorderTraversal(root *TreeNode) []int {
	// Approach 1:
	result := []int{}

	var inorder func(*TreeNode)

	inorder = func(root *TreeNode) {
		if root == nil {
			return
		}
		inorder(root.Left)
		result = append(result, root.Val)
		inorder(root.Right)
	}
	inorder(root)

	return result

	// Approach 2: Iterating method using Stack
	// var (
	// 	stack  []*TreeNode
	// 	result []int
	// 	cur    = root
	// )

	// for len(stack) > 0 || cur != nil {
	// 	for cur != nil {
	// 		stack = append(stack, cur)
	// 		cur = cur.Left
	// 	}
	// 	cur = stack[len(stack)-1]
	// 	stack = stack[:len(stack)-1]
	// 	result = append(result, cur.Val)
	// 	cur = cur.Right
	// }
	// return result

}

// @lc code=end

