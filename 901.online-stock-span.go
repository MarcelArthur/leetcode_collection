/*
 * @lc app=leetcode id=901 lang=golang
 *
 * [901] Online Stock Span
 */

// @lc code=start
type Pair struct {
	Val int
	Res int
}

type StockSpanner struct {
	Item []Pair
}

func Constructor() StockSpanner {
	stockspanner := StockSpanner{make([]Pair, 0)}
	return stockspanner
}

func (this *StockSpanner) Next(price int) int {
	res := 1
	for len(this.Item) > 0 && this.Item[len(this.Item)-1].Val <= price {
		res += this.Item[len(this.Item)-1].Res
		this.Item = this.Item[:len(this.Item)-1]
	}
	this.Item = append(this.Item, Pair{price, res})
	return res
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Next(price);
 */
// @lc code=end

