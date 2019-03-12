#Golang
func reverseBits(num uint32) uint32 {
    var res uint32
    for i := 0; i < 32; i++{
        res = res * 2 + (num >> uint(i)) & 1
    }
    return res
}
#Python
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int("{:032b}".format(n)[::-1], 2)

# Python Solution2
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res <<= 1
            res |= ((n >> i) & 1)
        return res
