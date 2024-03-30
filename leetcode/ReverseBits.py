class Solution:
    # leetcode 190
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            # get the first bit by right shift and doing an ANd
            bit = (n >> i) & 1
            # Now left shift that to its needed place which is 31 -i position and do an OR
            res = res | bit << (31 - i)
        return res
